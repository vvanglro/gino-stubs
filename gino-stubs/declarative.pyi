# Stubs for gino.declarative (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, TypeVar, Callable, Dict, Tuple, Type, Generic, TypeVar, Iterator, overload
from sqlalchemy import MetaData, Column, Table
from collections import OrderedDict

_FuncType = Callable[..., Any]
_F = TypeVar('_F', bound=_FuncType)
_T = TypeVar('_T')

class ColumnAttribute(Generic[_T]):
    prop_name: str = ...
    column: Column[_T] = ...
    def __init__(self, prop_name: str, column: Column[_T]) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Any) -> Column[_T]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: _T) -> None: ...
    def __delete__(self, instance: Any) -> None: ...

class ModelType(type):
    def __iter__(self) -> Iterator[Column[Any]]: ...
    def __getattr__(self, item: Any) -> Any: ...
    @classmethod
    def __prepare__(mcs: Any, name: Any, bases: Any, **kwargs: Any) -> OrderedDict[Any, Any]: ...
    def __new__(mcs: Any, name: Any, bases: Any, namespace: Any, **kwargs: Any) -> Any: ...

def declared_attr(m: _F) -> _F: ...

class Model:
    __metadata__: MetaData = ...
    __table__: Table = ...
    __attr_factory__: Any = ...
    __values__: Dict[str, Any] = ...
    def __init__(self) -> None: ...

def declarative_base(metadata: MetaData, model_classes: Tuple[Type[Any], ...] = ..., name: str = ...) -> Any: ...
