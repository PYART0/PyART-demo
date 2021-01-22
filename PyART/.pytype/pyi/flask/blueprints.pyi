# (generated with --quick)

import flask.scaffold
from typing import Any, Callable, Sequence, Type, TypeVar

Scaffold: Type[flask.scaffold.Scaffold]
_sentinel: Any

_T0 = TypeVar('_T0')

class Blueprint(flask.scaffold.Scaffold):
    __doc__: str
    _got_registered_once: bool
    cli_group: Any
    deferred_functions: list
    import_name: None
    json_decoder: None
    json_encoder: None
    name: Any
    root_path: None
    subdomain: Any
    template_folder: None
    url_prefix: Any
    url_values_defaults: Any
    warn_on_modifications: bool
    def __init__(self, name, import_name, static_folder = ..., static_url_path = ..., template_folder = ..., url_prefix = ..., subdomain = ..., url_defaults = ..., root_path = ..., cli_group = ...) -> None: ...
    def _is_setup_finished(self) -> bool: ...
    def add_app_template_filter(self, f, name = ...) -> None: ...
    def add_app_template_global(self, f, name = ...) -> None: ...
    def add_app_template_test(self, f, name = ...) -> None: ...
    def add_url_rule(self, rule, endpoint = ..., view_func = ..., **options) -> None: ...
    def after_app_request(self, f: _T0) -> _T0: ...
    def app_context_processor(self, f: _T0) -> _T0: ...
    def app_errorhandler(self, code) -> Callable[[Any], Any]: ...
    def app_template_filter(self, name = ...) -> Callable[[Any], Any]: ...
    def app_template_global(self, name = ...) -> Callable[[Any], Any]: ...
    def app_template_test(self, name = ...) -> Callable[[Any], Any]: ...
    def app_url_defaults(self, f: _T0) -> _T0: ...
    def app_url_value_preprocessor(self, f: _T0) -> _T0: ...
    def before_app_first_request(self, f: _T0) -> _T0: ...
    def before_app_request(self, f: _T0) -> _T0: ...
    def make_setup_state(self, app, options, first_registration = ...) -> BlueprintSetupState: ...
    def record(self, func) -> None: ...
    def record_once(self, func) -> Any: ...
    def register(self, app, options, first_registration = ...) -> None: ...
    def teardown_app_request(self, f: _T0) -> _T0: ...

class BlueprintSetupState:
    __doc__: str
    app: Any
    blueprint: Any
    first_registration: Any
    options: Any
    subdomain: Any
    url_defaults: dict
    url_prefix: Any
    def __init__(self, blueprint, app, options, first_registration) -> None: ...
    def add_url_rule(self, rule, endpoint = ..., view_func = ..., **options) -> None: ...

def _endpoint_from_view_func(view_func) -> Any: ...
def update_wrapper(wrapper: Callable, wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable: ...