"""DML - Data Manipulation Language."""
import sqlite3
from functools import wraps
from typing import Any

import logging

log_format = 'IN %(filename)s LINE %(lineno)s (%(levelname)s) "%(message)s"'

logging.basicConfig(
    filename='log.log', level=logging.DEBUG, filemode="w", format=log_format
)

# C - CREATE
# R - READ
# U - UPDATE
# D - DELETE


def commit(function: callable) -> callable:
    @wraps(function)
    def decorator(*args: tuple, **kwargs: dict) -> None:
        connect = sqlite3.connect('base.db')
        cursor = connect.cursor()
        sql = function(*args, **kwargs)
        cursor.execute(sql)
        connect.commit()
        connect.close()

    return decorator


@commit
def insert(name, phone, email) -> str:
    return f"""
    INSERT INTO users (name, phone, email)
        VALUES('{name}', '{phone}', '{email}')"""


@commit
def update(name, email) -> str:
    return f"""
    UPDATE users SET name = '{name}' WHERE email = '{email}'"""


@commit
def delete(email) -> str:
    return f"""
    DELETE FROM users WHERE email='{email}'"""


def select(field, data, fetch='all') -> Any:
    connect = sqlite3.connect('a.db')
    cursor = connect.cursor()

    sql = f"""
    SELECT id, name, phone, email FROM users WHERE {field}={data}
    """
    cursor.execute(sql)

    if fetch == 'all':
        data = cursor.fetchall()
    elif fetch == 'one':
        data = cursor.fetchone()
    else:
        logging.debug(f'Invalid option: {fetch}')
        raise Exception('Invalid option to fetch!')
    connect.close()
    return data
