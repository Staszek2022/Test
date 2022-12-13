from tkinter import *

window = Tk()
window.minsize(522, 565)
window.maxsize(522, 565)
window.geometry("522x565")

photo = PhotoImage(file="samolot.png")


mainFrame = Label(window,
                  text="Samolot",
                  font = ("Arial", 28),
                  bd=10,
                  bg="black",
                  fg="white",
                  image=photo,
                  compound="top")
mainFrame.pack()

window.mainloop()

