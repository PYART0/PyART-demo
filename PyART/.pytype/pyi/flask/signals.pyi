# (generated with --quick)

from typing import Any, NoReturn

Namespace: Any
_signals: Any
appcontext_popped: Any
appcontext_pushed: Any
appcontext_tearing_down: Any
before_render_template: Any
got_request_exception: Any
message_flashed: Any
request_finished: Any
request_started: Any
request_tearing_down: Any
signals_available: bool
template_rendered: Any

class _FakeSignal:
    __doc__: Any
    _fail: Any
    name: Any
    def __init__(self, name, doc = ...) -> None: ...
    def connect(self, *args, **kwargs) -> NoReturn: ...
    def connect_via(self, *args, **kwargs) -> NoReturn: ...
    def connected_to(self, *args, **kwargs) -> NoReturn: ...
    def disconnect(self, *args, **kwargs) -> NoReturn: ...
    def has_receivers_for(self, *args, **kwargs) -> NoReturn: ...
    def receivers_for(self, *args, **kwargs) -> NoReturn: ...
    def send(self, *args, **kwargs) -> None: ...
    def temporarily_connected_to(self, *args, **kwargs) -> NoReturn: ...
