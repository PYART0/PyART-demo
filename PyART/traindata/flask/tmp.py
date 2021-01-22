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
        reveal_type(current_app)