# (generated with --quick)

import jinja2.loaders
import threading
from typing import Any, Callable, Dict, Generator, Iterable, List, Optional, Sequence, Type, TypeVar, Union
import werkzeug.datastructures
import werkzeug.exceptions
import werkzeug.local
import werkzeug.routing
import werkzeug.wsgi

BadRequest: Type[werkzeug.exceptions.BadRequest]
BuildError: Type[werkzeug.routing.BuildError]
FileSystemLoader: Type[jinja2.loaders.FileSystemLoader]
Headers: Type[werkzeug.datastructures.Headers]
NotFound: Type[werkzeug.exceptions.NotFound]
RLock: Type[threading._RLock]
RequestedRangeNotSatisfiable: Type[werkzeug.exceptions.RequestedRangeNotSatisfiable]
_app_ctx_stack: werkzeug.local.LocalStack
_missing: Any
_os_alt_seps: List[Optional[str]]
_request_ctx_stack: werkzeug.local.LocalStack
current_app: werkzeug.local.LocalProxy
io: module
message_flashed: Any
mimetypes: module
os: module
pkgutil: module
posixpath: module
request: werkzeug.local.LocalProxy
session: werkzeug.local.LocalProxy
socket: module
sys: module
unicodedata: module

_T0 = TypeVar('_T0')

def adler32(__data: bytes, __value: int = ...) -> int: ...
def flash(message, category = ...) -> None: ...
def get_debug_flag() -> bool: ...
def get_env() -> str: ...
def get_flashed_messages(with_categories = ..., category_filter = ...) -> Any: ...
def get_load_dotenv(default: _T0 = ...) -> Union[bool, _T0]: ...
def get_template_attribute(template_name, attribute) -> Any: ...
def make_response(*args) -> Any: ...
def send_file(filename_or_fp, mimetype = ..., as_attachment = ..., attachment_filename = ..., add_etags = ..., cache_timeout = ..., conditional = ..., last_modified = ...) -> None: ...
def stream_with_context(generator_or_function) -> Union[Callable, Generator[None, Any, None]]: ...
def time() -> float: ...
def update_wrapper(wrapper: Callable, wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable: ...
def url_for(endpoint, **values) -> Any: ...
def url_quote(string, charset: str = ..., errors: str = ..., safe: str = ..., unsafe: str = ...) -> Any: ...
def wrap_file(environ: Dict[str, Any], file: werkzeug.wsgi._Readable, buffer_size: int = ...) -> Iterable[bytes]: ...
