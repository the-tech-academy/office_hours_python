
import sqlite3
#Open database connection
conn = sqlite3.connect("Files.db")

with conn:
    #Create a variable for controlling the cursor
    cur = conn.cursor()
    #Creating a table to store the files
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()
conn.close()
#Closing connection

#Reinstantiating the connection
conn = sqlite3.connect("Files.db")
#Creating a tuple containing the relevant files
files_tuple = ("information.docx","Hello.txt","myImage.png","myMovie.mpg","World.txt","data.pdf","myPhoto.jpg")
#Creating a "For" loop that will iterate until a ".txt" file is found, and will then insert it
for x in files_tuple:
    if x.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files(col_file) VALUES (?)", (x,))
            print(x)

conn.close()
