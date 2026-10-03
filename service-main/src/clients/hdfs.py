from hdfs import InsecureClient

from src.core.config import settings


def get_client() -> InsecureClient:
    return InsecureClient(settings.hdfs_url, user=settings.hdfs_user)  # who fucking cares about this? it's a small assignment.
