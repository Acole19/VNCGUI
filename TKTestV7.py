import Tkinter
from Tkinter import *
from PIL import Image
import time
root = Tk()
root.canvas = Canvas(root, width=240, height = 242)
root.img = PhotoImage(file="dice1.pbm")
root.imgArea = root.canvas.create_image(5,10, anchor=NW, image=root.img)
root.canvas.create_image(0,0, anchor=NW, image=root.img)
root.canvas.pack()
global incre
incre = 0
def update():
    global incre
    incre += 1
    if incre == 1:
        root.img = PhotoImage(file="dice1.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 2:
        root.img = PhotoImage(file="dice2.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 3:
        root.img = PhotoImage(file="dice3.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 4:
        root.img = PhotoImage(file="dice4.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 5:
        root.img = PhotoImage(file="dice5.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    else:
        root.img = PhotoImage(file="dice6.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
        incre = 0
    root.after(1000, update)
root.after(0, update)
root.mainloop()
