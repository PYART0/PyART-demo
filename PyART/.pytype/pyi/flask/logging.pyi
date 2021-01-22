# (generated with --quick)

from typing import Type
import werkzeug.local

LocalProxy: Type[werkzeug.local.LocalProxy]
default_handler: logging.StreamHandler
logging: module
request: werkzeug.local.LocalProxy
sys: module
wsgi_errors_stream: werkzeug.local.LocalProxy

def create_logger(app) -> logging.Logger: ...
def has_level_handler(logger) -> bool: ...
