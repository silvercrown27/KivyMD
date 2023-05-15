import sqlite3


def search(ext, folder_id=None):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    data = cursor.execute(f"SELECT name, path FROM files WHERE ext='{ext}'")
    data = data.fetchall()
    conn.close()
    return data