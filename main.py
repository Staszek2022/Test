from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

window = Tk()
# window.minsize(522, 565)
# window.maxsize(522, 565)
# window.geometry("522x565")

photo = None

def select_files():
    filetypes = (
        ('Wszystkie pliki obrazów', '*.bmp *.dib *.jpg *.jpeg;*.jpe *.jfif *.gif *.tif *.tiff *.png *.ico *.heic *.hif *.webp'),
        ('Wszystkie pliki', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Wybirz ikonkę',
        initialdir='/',
        filetypes=filetypes)
    return filenames[0]


def dodaj_do():
    img2 = ImageTk.PhotoImage(Image.open(select_files()))
    mainFrame.configure(image=img2)
    mainFrame.image = img2

frame1 = Frame(window, bg="black", height=50)
frame1.pack()

addButton = Button(frame1, text="dodaj obrazek", font=("Arial", 24), command=dodaj_do)
addButton.pack()

mainFrame = Label(window,
                  text="Samolot",
                  font = ("Arial", 28),
                  bd=10,
                  bg="black",
                  fg="white",
                  image=photo,
                  compound="top")
mainFrame.pack(expand = "yes")

window.mainloop()

