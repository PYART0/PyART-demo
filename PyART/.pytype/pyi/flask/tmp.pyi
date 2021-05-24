# (generated with --quick)

import click.testing
import contextlib
import flask.cli
from typing import Any, Callable, Dict, Iterator, Type, TypeVar, Union
import werkzeug.test

CliRunner: Type[click.testing.CliRunner]
Client: Type[werkzeug.test.Client]
ScriptInfo: Type[flask.cli.ScriptInfo]
_request_ctx_stack: Any
werkzeug: module

_T = TypeVar('_T')
_TFlaskClient = TypeVar('_TFlaskClient', bound=FlaskClient)

class EnvironBuilder(werkzeug.test.EnvironBuilder):
    app: Any
    def __init__(self, app, path = ..., base_url = ..., subdomain = ..., url_scheme = ..., *args, **kwargs) -> None: ...
    def json_dumps(self, obj, **kwargs) -> Union[bytes, str]: ...

class FlaskClient(werkzeug.test.Client):
    environ_base: Dict[str, str]
    preserve_context: bool
    session_transaction: Callable[..., contextlib._GeneratorContextManager]
    def __enter__(self: _TFlaskClient) -> _TFlaskClient: ...
    def __exit__(self, exc_type, exc_value, tb) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def open(self, *args, **kwargs) -> Any: ...

def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def json_dumps(obj, app = ..., **kwargs) -> Union[bytes, str]: ...
def url_parse(url, scheme = ..., allow_fragments: bool = ...) -> Any: ...
