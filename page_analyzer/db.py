import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("Переменная DATABASE_URL не установлена")

    return psycopg.connect(
        database_url,
        row_factory=dict_row,
    )

def get_urls():
    query = """
        SELECT id, name, created_at
        FROM urls
        ORDER BY id DESC
    """

    with get_connection() as connection:
        return connection.execute(query).fetchall()

def get_url(url_id):
    query = """
        SELECT id, name, created_at
        FROM urls
        WHERE id = %s
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            (url_id,),
        ).fetchone()

def get_url_by_name(name):
    query = """
        SELECT id, name, created_at
        FROM urls
        WHERE name = %s
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            (name,),
        ).fetchone()

def create_url(name):
    query = """
        INSERT INTO urls (name)
        VALUES (%s)
        RETURNING id, name, created_at
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            (name,),
        ).fetchone()
