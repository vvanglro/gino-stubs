# Stubs for gino (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import *
from .api import Gino as Gino
from .engine import GinoConnection as GinoConnection, GinoEngine as GinoEngine
from .strategies import GinoStrategy as GinoStrategy

from typing import Any

def create_engine(*args: Any, **kwargs: Any) -> Any: ...
