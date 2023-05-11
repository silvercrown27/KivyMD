import sqlite3
import os

mydb = sqlite3.connect("appdb.sqlite3")

mycursor = mydb.cursor()
mycursor.execute("""create table if not exists files(
                    id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    ext TEXT,
                    size INT NOT NULL,
                    path TEXT NOT NULL
                    );""")

extensions = (
    '.mp3', '.wav', '.ogg', '.m4a',
    '.mp4', '.mkv', '.gif',
    '.jpg', '.png', '.jfif', '.jpeg',
    '.pdf', '.doc', '.docx', '.txt')


def get_file_size(path):
    try:
        with open(path, 'rb') as f:
            fs = len(f.read()) / (1024 * 1024)
            return round(fs, 3)
    except PermissionError:
        return 0


files = []
DIRS = []

# traverse directory tree and find all files
for dirpath, dirnames, filenames in os.walk('C:/Users/USER/Documents') or os.walk('/'):
    for dirname in dirnames:
        DIRS.append(dirname)
    for filename in filenames:
        if filename.endswith(extensions):
            file_path = os.path.join(dirpath, filename)
            name = os.path.basename(file_path)
            file_details = []
            ext = [x for x in extensions if filename.endswith(x)][0]
            size = get_file_size(file_path)
            file_details.append(name)
            file_details.append(ext)
            file_details.append(size)
            file_details.append(file_path)
            f = tuple(file_details)
            print(f)
            files.append(f)
            file_details.pop()

print(files[:5])
print(DIRS)

# mydb.execute(f"INSERT INTO files (name, ext, size, path) VALUES {tuple(files)};")
files.pop()