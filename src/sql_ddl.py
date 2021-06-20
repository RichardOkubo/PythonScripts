"""DDL - Data Definition Language."""
import sqlite3

connect = sqlite3.connect('base.db')

cursor = connect.cursor()

sql = """
CREATE TABLE users (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL)"""

cursor.execute(sql)
connect.commit()
connect.close()
