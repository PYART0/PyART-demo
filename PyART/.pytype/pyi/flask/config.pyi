# (generated with --quick)

from typing import Any

errno: module
os: module
types: module

class Config(dict):
    __doc__: str
    root_path: Any
    def __init__(self, root_path, defaults = ...) -> None: ...
    def __repr__(self) -> str: ...
    def from_envvar(self, variable_name, silent = ...) -> Any: ...
    def from_file(self, filename, load, silent = ...) -> Any: ...
    def from_mapping(self, *mapping, **kwargs) -> bool: ...
    def from_object(self, obj) -> None: ...
    def from_pyfile(self, filename, silent = ...) -> bool: ...
    def get_namespace(self, namespace, lowercase = ..., trim_namespace = ...) -> dict: ...

class ConfigAttribute:
    __doc__: str
    def __get__(self, obj, type = ...) -> Any: ...
    def __init__(self, name, get_converter = ...) -> None: ...
    def __set__(self, obj, value) -> None: ...
    def get_converter(self, _1) -> Any: ...

def import_string(import_name, silent: bool = ...) -> Any: ...