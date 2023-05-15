import sqlite3
import os
import psutil

def create_database():
    mydb = sqlite3.connect("db.sqlite3")

    mycursor = mydb.cursor()

    mycursor.execute("""create table if not exists drives(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        size INT NOT NULL
                        );""")

    mycursor.execute("""create table if not exists folders(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        path TEXT NOT NULL,
                        folder_id INT,
                        FOREIGN KEY (folder_id) REFERENCES folders(id)
                        );""")

    mycursor.execute("""create table if not exists files(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        ext TEXT,
                        size INT NOT NULL,
                        path TEXT NOT NULL,
                        folder_id INT,
                        FOREIGN KEY (folder_id) REFERENCES folders(id) 
                        );""")

    def get_file_size(path):
        try:
            with open(path, 'rb') as f:
                fs = len(f.read()) / (1024 * 1024)
                return round(fs, 3)
        except PermissionError:
            return 0


    for partition in psutil.disk_partitions():
        if 'cdrom' in partition.opts or partition.fstype == '':
            # skip CD-ROM drives and unmounted partitions
            continue
        drive = partition.device.split(':')[0]
        total_size = psutil.disk_usage(partition.mountpoint).total
        mycursor.execute("INSERT INTO drives (name, size) VALUES (?, ?)", (drive, total_size / (1024 ** 3)))

    # traverse directory tree and find all files
    for dirpath, dirnames, filenames in os.walk('C:/Users/USER/Documents/GitHub') or os.walk('/'):
        directories = os.path.normpath(dirpath).split(os.sep)
        parent_dir, current_dir = os.path.split(dirpath)

        for dirname in dirnames:
            dirid = mycursor.execute(
                f"SELECT id FROM folders WHERE path='{parent_dir}' AND name='{directories[-1]}'")
            dirid_row = dirid.fetchone()
            dirid = None if dirid_row is None else dirid_row[0]
            mycursor.execute("INSERT OR IGNORE INTO folders "
                             "(name, path, folder_id) VALUES (?, ?, ?)", (dirname, dirpath, dirid))

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            name = filename
            ext = os.path.splitext(filename)[1]
            size = get_file_size(file_path)
            dirid = mycursor.execute(
                f"SELECT id FROM folders WHERE path='{parent_dir}' AND name='{directories[-1]}'") or None
            dirid_row = dirid.fetchone()
            dirid = None if dirid_row is None else dirid_row[0]
            mycursor.execute("INSERT INTO files (name, ext, size, path, folder_id) VALUES (?, ?, ?, ?, ?)",
                             (name, ext, size, file_path, dirid))
    def check_for_duplicates(table, column1, column2):
        data = mycursor.execute(f"SELECT {column1} FROM {table}")
        data = data.fetchall()
        for i in data:
            d_values = mycursor.execute(f"SELECT {column2} FROM {table} WHERE {column1}=?", (i[0],))
            d_values = d_values.fetchall()
            for d in d_values:
                dp = mycursor.execute(f"SELECT {column1}[1:] FROM {table} WHERE {column2}=?", (d[0],))
                dp = dp.fetchall()
                for x in dp:
                    deleted = mycursor.execute(f"SELECT * FROM {table} WHERE {column1}=? AND {column2}=?", (x[0], d[0]))
                    deleted = deleted.fetchall()
                    print(deleted)
                    mycursor.execute(f"DELETE FROM {table} WHERE {column1}=? AND {column2}=?", (x[0], d[0]))


    # check_for_duplicates("folders", "name", "path")
    # check_for_duplicates("files", "name", "folder_id")

    data = mycursor.execute("SELECT * FROM folders WHERE folder_id IS NULL")
    rows = data.fetchall()

    for row in rows:
        print(row)

    mydb.commit()
    mydb.close()