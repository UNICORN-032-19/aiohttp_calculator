from aiopg.sa import SAConnection
from aiopg.sa.result import RowProxy

from aiohttp_calculator.main.tables import result


__all__ = ['save_result', ]


async def save_result(conn: SAConnection, string: str, res: str, error: str) -> None:
    query = 'INSERT INTO result (string, result, error) VALUES (%s, %s, %s)'
    return await conn.execute(query, (string, res, error))


async def get_results(conn: SAConnection) -> None:
    query = result\
        .select()\
        .order_by(result.c.id)
    cursor = await conn.execute(query)

    return await cursor.fetchall()
