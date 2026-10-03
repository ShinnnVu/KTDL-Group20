from pymongo import MongoClient

from src.core.config import settings


def get_client() -> MongoClient:
    uri = (
        f"mongodb://{settings.mongo_user}:{settings.mongo_password}"
        f"@{settings.mongo_host}:{settings.mongo_port}/"
    )
    return MongoClient(uri)
