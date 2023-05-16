import sqlite3


def search(ext, folder_id=None):
    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        data = cursor.execute(f"SELECT name, path FROM files WHERE ext='{ext}'")
        data = data.fetchall()
    return data