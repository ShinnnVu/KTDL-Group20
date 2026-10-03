import psycopg2
from psycopg2.extensions import connection as Connection

from src.core.config import settings


def get_connection() -> Connection:
    return psycopg2.connect(
        host=settings.postgres_host,
        port=settings.postgres_port,
        user=settings.postgres_user,
        password=settings.postgres_password,
        dbname=settings.postgres_db,
    )
