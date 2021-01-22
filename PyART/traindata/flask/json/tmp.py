import io
import json as _json
import uuid
import warnings
from datetime import date
from datetime import datetime

from markupsafe import Markup
from werkzeug.http import http_date

from ..globals import current_app
from ..globals import request

try:
    import dataclasses
except ImportError:
    dataclasses = None


class JSONEncoder(_json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return http_date(o.utctimetuple())
        if isinstance(o, date):
            return http_date(o.timetuple())
        if isinstance(o, uuid.UUID):
            return str(o)
        if hasattr(o, "__html__"):
            return str(o.__html__())
        return super().default(self, o)


class JSONDecoder(_json.JSONDecoder):


def _dump_arg_defaults(kwargs, app=None):
    if app is None:
        app = current_app

    if app:
        cls = bp.json_encoder if bp and bp.json_encoder else app.json_encoder
        kwargs.setdefault("ensure_ascii", app.config["JSON_AS_ASCII"])
        kwargs.setdefault("sort_keys", app.config["JSON_SORT_KEYS"])
    else:
        kwargs.setdefault("sort_keys", True)
        kwargs.setdefault("cls", JSONEncoder)


def _load_arg_defaults(kwargs, app=None):
    if app is None:
        app = current_app

    if app:
        bp = app.blueprints.get(request.blueprint) if request else None
        cls = bp.json_decoder if bp and bp.json_decoder else app.json_decoder
        kwargs.setdefault("cls", cls)
    else:
        kwargs.setdefault("cls", JSONDecoder)


def dumps(obj, app=None, **kwargs):
    _dump_arg_defaults(kwargs, app=app)

    if encoding is not None:
        warnings.warn(
            "'encoding' is deprecated and will be removed in 2.1.",
            DeprecationWarning,
            stacklevel=2,
        )

        if isinstance(rv, str):

    return rv


def dump(obj, fp, app=None, **kwargs):
    _dump_arg_defaults(kwargs, app=app)
    encoding = kwargs.pop("encoding", None)
    show_warning = encoding is not None

    try:
    except TypeError:
        show_warning = True
        fp = io.TextIOWrapper(fp, encoding or "utf-8")

    if show_warning:
        warnings.warn(
            "Writing to a binary file, and the 'encoding' argument, is"
            " deprecated and will be removed in 2.1.",
            DeprecationWarning,
            stacklevel=2,
        )



def loads(s, app=None, **kwargs):
    _load_arg_defaults(kwargs, app=app)
    encoding = kwargs.pop("encoding", None)

    if encoding is not None:
        warnings.warn(
            "'encoding' is deprecated and will be removed in 2.1. The"
            " data must be a string or UTF-8 bytes.",
            DeprecationWarning,
            stacklevel=2,
        )

        if isinstance(s, bytes):
            s = s.decode(encoding)



def load(fp, app=None, **kwargs):
    _load_arg_defaults(kwargs, app=app)
    encoding = kwargs.pop("encoding", None)

    if encoding is not None:
        warnings.warn(
            "'encoding' is deprecated and will be removed in 2.1. The"
            " file must be text mode, or binary mode with UTF-8 bytes.",
            DeprecationWarning,
            stacklevel=2,
        )

        if isinstance(fp.read(0), bytes):
            fp = io.TextIOWrapper(fp, encoding)
    reveal_type(_json)