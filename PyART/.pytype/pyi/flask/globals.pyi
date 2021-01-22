# (generated with --quick)

import functools
from typing import Any, Type
import werkzeug.local

LocalProxy: Type[werkzeug.local.LocalProxy]
LocalStack: Type[werkzeug.local.LocalStack]
_app_ctx_err_msg: str
_app_ctx_stack: werkzeug.local.LocalStack
_request_ctx_err_msg: str
_request_ctx_stack: werkzeug.local.LocalStack
current_app: werkzeug.local.LocalProxy
g: werkzeug.local.LocalProxy
partial: Type[functools.partial]
request: werkzeug.local.LocalProxy
session: werkzeug.local.LocalProxy

def _find_app() -> Any: ...
def _lookup_app_object(name) -> Any: ...
def _lookup_req_object(name) -> Any: ...
