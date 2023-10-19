import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('bottle.db')


class bottle:
    def __init__(self):
        self.conn = sqlite3.connect("bottle.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open('database.sql') as sqlfile:
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

   # def user_list(request):
       # posts =

# Membuat kursor
# cursor = conn.cursor()

# Menjalankan pernyataan SQL mentah
# cursor.execute("SELECT * FROM user")

# Mengambil hasil
# results = cursor.fetchall()


# Menutup koneksi
conn.close()
