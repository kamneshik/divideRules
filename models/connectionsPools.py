import aioredis
import pymongo

from config import mongo_max_connections, mongo_host, mongo_port, mongo_min_connections
from config import redis_min_connections, redis_max_connections, redis_host, redis_port


class MongoPoolConnection:
    """Создаёт пулл соединений к базе данных монго, берёт информацию из файла config.py"""

    def __init__(self, uri=f'mongodb://{mongo_host}:{mongo_port}/',
                 min_connections=mongo_min_connections,
                 max_connections=mongo_max_connections
                 ):
        self.uri = uri
        self.min_connections = min_connections
        self.max_connections = max_connections
        self.connections = []

    def initialize_pool(self):
        for _ in range(self.min_connections, self.max_connections):
            connection = pymongo.MongoClient(self.uri)
            self.connections.append(connection)

    def get_connection(self):
        if not self.connections:
            self.initialize_pool()
        return self.connections.pop()

    def return_connection(self, connection):
        self.connections.append(connection)

    def close_all_connections(self):
        for connection in self.connections:
            connection.close()


class RedisConnectionPool:
    def __init__(self, uri=f"redis://{redis_host}:{redis_port}",
                 min_connections=redis_min_connections,
                 max_connections=redis_max_connections
                 ):
        self.uri = uri
        self.min_connections = min_connections
        self.max_connections = max_connections
        self.connections = None

    async def initialize_pool(self):
        self.connections = await aioredis.create_pool(
            self.uri,
            minsize=self.min_connections,
            maxsize=self.max_connections
        )

    async def get_connection(self) -> aioredis.Connection:
        if self.connections is None:
            await self.initialize_pool()
        return await self.connections.acquire()

    async def return_connection(self, connection: aioredis.Connection):
        await self.connections.realease(connection)

    async def close_all_connections(self):
        if self.connections is not None:
            self.connections.close()
            await self.connections.wait_closed()
