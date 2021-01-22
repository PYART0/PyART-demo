import io
import mimetypes
import os
import pkgutil
import posixpath
import socket
import sys
import unicodedata
from functools import update_wrapper
from threading import RLock
from time import time
from zlib import adler32

from jinja2 import FileSystemLoader
from werkzeug.datastructures import Headers
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import RequestedRangeNotSatisfiable
from werkzeug.routing import BuildError
from werkzeug.urls import url_quote
from werkzeug.wsgi import wrap_file

from .globals import _app_ctx_stack
from .globals import _request_ctx_stack
from .globals import current_app
from .globals import request
from .globals import session
from .signals import message_flashed

_missing = object()


_os_alt_seps = list(
    sep for sep in [os.path.sep, os.path.altsep] if sep not in (None, "/")
)


def get_env():
    return os.environ.get("FLASK_ENV") or "production"


def get_debug_flag():
    val = os.environ.get("FLASK_DEBUG")

    if not val:
        return get_env() == "development"

    return val.lower() not in ("0", "false", "no")


def get_load_dotenv(default=True):
    val = os.environ.get("FLASK_SKIP_DOTENV")

    if not val:
        return default

    return val.lower() in ("0", "false", "no")


def stream_with_context(generator_or_function):
    try:
        gen = iter(generator_or_function)
    except TypeError:

        def decorator(*args, **kwargs):
            gen = generator_or_function(*args, **kwargs)
            return stream_with_context(gen)

        return update_wrapper(decorator, generator_or_function)

    def generator():
        ctx = _request_ctx_stack.top
        if ctx is None:
            raise RuntimeError(
                "Attempted to stream with context but "
                "there was no context in the first place to keep around."
            )
        with ctx:
            yield None

            try:
                yield from gen
            finally:
                if hasattr(gen, "close"):
                    gen.close()

    wrapped_g = generator()
    next(wrapped_g)
    return wrapped_g


def make_response(*args):
    if not args:
        return current_app.response_class()
    if len(args) == 1:
        args = args[0]
    return current_app.make_response(args)


def url_for(endpoint, **values):
    appctx = _app_ctx_stack.top
    reqctx = _request_ctx_stack.top

    if appctx is None:
        raise RuntimeError(
            "Attempted to generate a URL without the application context being"
            " pushed. This has to be executed when application context is"
            " available."
        )

    if reqctx is not None:
        url_adapter = reqctx.url_adapter
        blueprint_name = request.blueprint

        if endpoint[:1] == ".":
            if blueprint_name is not None:
                endpoint = f"{blueprint_name}{endpoint}"
            else:
                endpoint = endpoint[1:]

        external = values.pop("_external", False)

    else:
        url_adapter = appctx.url_adapter

        if url_adapter is None:
            raise RuntimeError(
                "Application was not able to create a URL adapter for request"
                " independent URL generation. You might be able to fix this by"
                " setting the SERVER_NAME config variable."
            )

        external = values.pop("_external", True)

    anchor = values.pop("_anchor", None)
    method = values.pop("_method", None)
    scheme = values.pop("_scheme", None)
    appctx.app.inject_url_defaults(endpoint, values)

    old_scheme = None
    if scheme is not None:
        if not external:
            raise ValueError("When specifying _scheme, _external must be True")
        old_scheme = url_adapter.url_scheme
        url_adapter.url_scheme = scheme

    try:
        try:
            rv = url_adapter.build(
                endpoint, values, method=method, force_external=external
            )
        finally:
            if old_scheme is not None:
                url_adapter.url_scheme = old_scheme
    except BuildError as error:
        values["_external"] = external
        values["_anchor"] = anchor
        values["_method"] = method
        values["_scheme"] = scheme
        return appctx.app.handle_url_build_error(error, endpoint, values)

    if anchor is not None:
        rv += f"#{url_quote(anchor)}"
    return rv


def get_template_attribute(template_name, attribute):
    return getattr(current_app.jinja_env.get_template(template_name).module, attribute)


def flash(message, category="message"):
    flashes = session.get("_flashes", [])
    flashes.append((category, message))
    session["_flashes"] = flashes
    message_flashed.send(
        current_app._get_current_object(), message=message, category=category
    )


def get_flashed_messages(with_categories=False, category_filter=()):
    flashes = _request_ctx_stack.top.flashes
    if flashes is None:
        _request_ctx_stack.top.flashes = flashes = (
            session.pop("_flashes") if "_flashes" in session else []
        )
    if category_filter:
        flashes = list(filter(lambda f: f[0] in category_filter, flashes))
    if not with_categories:
        return [x[1] for x in flashes]
    return flashes


def send_file(
    filename_or_fp,
    mimetype=None,
    as_attachment=False,
    attachment_filename=None,
    add_etags=True,
    cache_timeout=None,
    conditional=False,
    last_modified=None,
):
    mtime = None
    fsize = None

    if hasattr(filename_or_fp, "__fspath__"):
        filename_or_fp = os.fspath(filename_or_fp)

    if isinstance(filename_or_fp, str):
        filename = filename_or_fp
        if not os.path.isabs(filename):
            reveal_type(os.path)