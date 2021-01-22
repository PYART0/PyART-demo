# (generated with --quick)

import flask.app
import flask.blueprints
from typing import Any, Generator, Optional, Type
import werkzeug.local

Blueprint: Type[flask.blueprints.Blueprint]
Flask: Type[flask.app.Flask]
_request_ctx_stack: werkzeug.local.LocalStack
os: module

class DebugFilesKeyError(KeyError, AssertionError):
    __doc__: str
    msg: str
    def __init__(self, request, key) -> None: ...
    def __str__(self) -> str: ...

class FormDataRoutingRedirect(AssertionError):
    __doc__: str
    def __init__(self, request) -> None: ...

class UnexpectedUnicodeError(AssertionError, UnicodeError):
    __doc__: str

def _dump_loader_info(loader) -> Generator[str, Any, None]: ...
def attach_enctype_error_multidict(request) -> None: ...
def explain_ignored_app_run() -> None: ...
def explain_template_loading_attempts(app, template, attempts) -> None: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...