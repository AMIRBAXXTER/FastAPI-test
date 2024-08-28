from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
from beanie import init_beanie
from .models import *


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def init_beanie(self):
        await init_beanie(database=self.db, document_models=[User, Message, Group])


mongodb = MongoDB(settings.mongo_uri, "chat_db")
