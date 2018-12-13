import Tkinter
from Tkinter import *
from PIL import Image
import time
root = Tk()
root.canvas = Canvas(root, width=810, height = 460)
root.img = PhotoImage(file="GUIPRES1.pbm")
root.imgArea = root.canvas.create_image(5,10, anchor=NW, image=root.img)
root.canvas.create_image(0,0, anchor=NW, image=root.img)
root.canvas.pack()
global incre
incre = 0
def update():
    global incre
    incre += 1
    if incre == 1:
        root.img = PhotoImage(file="GUIPRES1.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 2:
        root.img = PhotoImage(file="GUIPRES2.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 3:
        root.img = PhotoImage(file="GUIPRES3.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    elif incre == 4:
        root.img = PhotoImage(file="GUIPRES4.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
    else
        root.img = PhotoImage(file="GUIPRES5.pbm")
        root.canvas.itemconfig(root.imgArea, image = root.img)
        incre = 0
    root.after(1000, update)
root.after(0, update)
root.mainloop()
