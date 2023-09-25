from redis.asyncio import ConnectionPool
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
