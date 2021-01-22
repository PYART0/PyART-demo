# (generated with --quick)

from typing import Any, NoReturn
import werkzeug.local

BadRequest: Any
RequestBase: Any
ResponseBase: Any
_JSONMixin: Any
current_app: werkzeug.local.LocalProxy
json: module

class JSONMixin(Any):
    json_module: module
    def on_json_loading_failed(self, e) -> NoReturn: ...

class Request(Any, JSONMixin):
    __doc__: str
    blueprint: Any
    endpoint: Any
    max_content_length: Any
    routing_exception: None
    url_rule: None
    view_args: None
    def _load_form_data(self) -> None: ...

class Response(Any, JSONMixin):
    __doc__: str
    default_mimetype: str
    max_cookie_size: Any
    def _get_data_for_json(self, cache) -> Any: ...
