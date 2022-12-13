from tkinter import *
import threading
import time

def okno():
    for i in range(50):
        time.sleep(0.1)
        print(window.winfo_geometry())

window = Tk()
window.geometry("429x557")
threading.Thread(target=okno).start()
window.mainloop()

