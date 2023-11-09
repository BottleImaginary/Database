import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('bottle.db')

cursor = conn.cursor()


class bottle:
    def __init__(self):
        self.conn = sqlite3.connect("bottle.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open('bottle_imaginary.sql') as sqlfile:
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()

    def save_user(self, id_user, nama_user):
        try:
            self.cursor.execute(
                "INSERT INTO user (id_user, nama_user) VALUES (?,?)"), (id_user, nama_user)
            self.conn.commit()
            return True
        except Exception as f:
            print("Error", str(f))
            return False

data = cursor.fetchall()
for row in data:
    print(row)

conn.commit()
conn.close()
