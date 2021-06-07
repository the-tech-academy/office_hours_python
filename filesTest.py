
import sqlite3

conn = sqlite3.connect("Files.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect("Files.db")
files_tuple = ("information.docx","Hello.txt","myImage.png","myMovie.mpg","World.txt","data.pdf","myPhoto.jpg")
for x in files_tuple:
    if x.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files(col_file) VALUES (?)", (x,))
            print(x)

conn.close()
