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
        SELECT
            urls.id,
            urls.name,
            urls.created_at,
            MAX(url_checks.created_at) AS last_check_at
        FROM urls
        LEFT JOIN url_checks
            ON url_checks.url_id = urls.id
        GROUP BY
            urls.id,
            urls.name,
            urls.created_at
        ORDER BY urls.id DESC
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

def get_url_checks(url_id):
    query = """
        SELECT
            id,
            url_id,
            status_code,
            h1,
            title,
            description,
            created_at
        FROM url_checks
        WHERE url_id = %s
        ORDER BY id DESC
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            (url_id,),
        ).fetchall()

def create_url_check(url_id):
    query = """
        INSERT INTO url_checks (url_id)
        VALUES (%s)
        RETURNING
            id,
            url_id,
            status_code,
            h1,
            title,
            description,
            created_at
    """

    with get_connection() as connection:
        return connection.execute(
            query,
            (url_id,),
        ).fetchone()
