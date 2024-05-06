import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
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
    
def create_turma_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS links (
            id integer PRIMARY KEY,
            link_reuniao VARCHAR(1000) NOT NULL,
            id_turma VARCHAR(2) NOT NULL
    );'''
        conn.execute(sql)
        print("Conexão estabelecida!")
    except Error as e:
        print(e)

def save_link_to_db(conn, link_reuniao, id_turma):
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM links WHERE id_turma = ?", (id_turma,))

            data = cursor.fetchone()
            if data is not None:
                cursor.execute("UPDATE links SET link_reuniao = ? WHERE id_turma = ?", (link_reuniao, id_turma))
            else:
                cursor.execute("INSERT INTO links(link_reuniao, id_turma) VALUES (?, ?)", (link_reuniao, id_turma))
            conn.commit()
            return True
    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

