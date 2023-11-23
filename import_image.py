import sqlite3
from tkinter import *
from tkinter import filedialog

root = Tk()


def filedialogs():
    global get_image
    get_image = filedialog.askopenfilenames(title="PILIH GAMBAR", filetypes=(
        ("png", "*.png"), ("jpg", "*.jpg"), ("Allfile", "*.*")))


def conver_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image


def insert_image():
    image_database = sqlite3.connect("bottle_imaginary.db")
    data = image_database.cursor()

    for image in get_image:
        insert_photo = conver_image_into_binary(image)
        data.execute("INSERT INTO botol(gambar_botol) Values(:image)",
                     {'image': insert_photo})

    image_database.commit()
    image_database.close()


def __init__(self):
    self.conn = sqlite3.connect("bottle_imaginary.db")
    self.cursor = self.conn.cursor()


select_image = Button(root, text="PILIH GAMBAR", command=filedialogs)
select_image.grid(row=0, pady=(100, 0), padx=100)

save_image = Button(root, text="SIMPAN", command=insert_image)
save_image.grid(row=1, column=0)

root = mainloop()
