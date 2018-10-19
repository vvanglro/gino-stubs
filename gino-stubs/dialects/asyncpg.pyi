# Stubs for gino.dialects.asyncpg (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from . import base
from sqlalchemy.dialects.postgresql.base import ENUM, PGCompiler, PGDialect, PGExecutionContext
from typing import Any, Optional, Generator
import asyncpg
import asyncpg.pool

class AsyncpgDBAPI(base.BaseDBAPI):
    Error: Any = ...

class AsyncpgCompiler(PGCompiler):  # type: ignore
    @property
    def bindtemplate(self): ...
    @bindtemplate.setter
    def bindtemplate(self, val: Any) -> None: ...

class AsyncpgExecutionContext(base.ExecutionContextOverride, PGExecutionContext): ...  # type: ignore

class AsyncpgIterator:
    def __init__(self, context: Any, iterator: Any) -> None: ...
    async def __anext__(self): ...

class AsyncpgCursor(base.Cursor):
    def __init__(self, context: Any, cursor: Any) -> None: ...
    async def many(self, n: Any, *, timeout: Any = ...) -> Any: ...
    async def next(self, *, timeout: Any = ...) -> Any: ...
    async def forward(self, n: Any, *, timeout: Any = ...) -> None: ...

class PreparedStatement(base.PreparedStatement):
    def __init__(self, prepared: Any, clause: Optional[Any] = ...) -> None: ...

class DBAPICursor(base.DBAPICursor):
    def __init__(self, dbapi_conn: Any) -> None: ...
    async def prepare(self, context: Any, clause: Optional[Any] = ...) -> PreparedStatement: ...
    async def async_execute(self, query: Any, timeout: Any, args: Any, limit: int = ..., many: bool = ...) -> Any: ...
    @property
    def description(self): ...
    def get_statusmsg(self): ...

class Pool(base.Pool[asyncpg.pool.Pool, asyncpg.pool.PoolConnectionProxy]):
    def __init__(self, url: Any, loop: Any, **kwargs: Any) -> None: ...
    def __await__(self) -> Generator[Any, None, Pool]: ...
    @property
    def raw_pool(self) -> asyncpg.pool.Pool: ...
    async def acquire(self, *, timeout: Optional[Any] = ...) -> asyncpg.pool.PoolConnectionProxy: ...
    async def release(self, conn: Any) -> None: ...
    async def close(self) -> None: ...

class Transaction(base.Transaction):
    def __init__(self, tx: Any) -> None: ...
    @property
    def raw_transaction(self): ...
    async def begin(self) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...

class AsyncEnum(ENUM):  # type: ignore
    async def create_async(self, bind: Optional[Any] = ..., checkfirst: bool = ...) -> None: ...
    async def drop_async(self, bind: Optional[Any] = ..., checkfirst: bool = ...) -> None: ...

class AsyncpgDialect(PGDialect, base.AsyncDialectMixin):  # type: ignore
    driver: str = ...
    supports_native_decimal: bool = ...
    dbapi_class: Any = ...
    statement_compiler: Any = ...
    execution_ctx_cls: Any = ...
    cursor_cls: Any = ...
    dbapi_type_map: Any = ...
    init_kwargs: Any = ...
    colspecs: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def init_pool(self, url: Any, loop: Any) -> Pool: ...
    def transaction(self, raw_conn: Any, args: Any, kwargs: Any) -> Transaction: ...
    def on_connect(self): ...
    async def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    async def get_isolation_level(self, connection: Any) -> str: ...
    async def has_schema(self, connection: Any, schema: Any) -> bool: ...
    async def has_table(self, connection: Any, table_name: Any, schema: Optional[Any] = ...) -> bool: ...
    async def has_sequence(self, connection: Any, sequence_name: Any, schema: Optional[Any] = ...) -> bool: ...
    async def has_type(self, connection: Any, type_name: Any, schema: Optional[Any] = ...) -> bool: ...
