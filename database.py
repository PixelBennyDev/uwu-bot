import aioredis
import asyncio
from utils import parse_redis_url
from storage import Storage


class Db(object):
    def __init__(self, redis_url, mongo_url, loop):
        self.loop = loop
        self.redis_url = redis_url
        self.mongo_url = mongo_url
        self.loop.create_task(self.create())
        self.redis_address = parse_redis_url(redis_url)

    async def create(self):
        self.redis = await aioredis.create_redis(
            self.redis_address,
            encoding='utf8'
        )

    async def get_storage(self, server):
        namespace = "{}.{}:".format(
            server.id,
            "_"
        )
        storage = Storage(namespace, self.redis)
        return storage
