from motor.motor_asyncio import AsyncIOMotorClient
from code.core.config import settings


class MongoDB:

    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]


mongodb = MongoDB(settings.mongo_uri, "chat_db")
