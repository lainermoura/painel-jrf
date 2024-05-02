import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('painel-jrf.db')
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    return conn

def create_files_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS files (
                    id integer PRIMARY KEY,
                    file_name text NOT NULL,
                    file_data BLOB NOT NULL
                );'''
        conn.execute(sql)
    except Error as e:
        print(e)

def save_file_to_db(conn, file_data, file_name):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM files WHERE file_name = ?", (file_name,))
        data = cursor.fetchone()
        if data is None:
            cursor.execute("INSERT INTO files(file_name, file_data) VALUES (?, ?)", (file_name, file_data))
            conn.commit()
            return True
        else:
            return False
    except Error as e:
        print(e)
        return False
