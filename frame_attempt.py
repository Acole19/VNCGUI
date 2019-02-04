from Tkinter import *
from PIL import Image
import time
import random
from random import seed
from random import randint
from random import choice
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(frame)
bottomframe.pack( side = BOTTOM )
frame.canvas = Canvas(frame, width=240, height = 242)
frame.img = PhotoImage(file="dice1.pbm")
frame.imgArea = frame.canvas.create_image(5,10, anchor=NW, image=frame.img)
frame.canvas.create_image(0,0, anchor=NW, image=frame.img)
frame.canvas.pack( side = LEFT)
global incre
incre = 0
def update():
    global incre
    incre += 1
    if incre == 1:
        frame.img = PhotoImage(file="dice1.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
    elif incre == 2:
        frame.img = PhotoImage(file="dice2.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
    elif incre == 3:
        frame.img = PhotoImage(file="dice3.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
    elif incre == 4:
        frame.img = PhotoImage(file="dice4.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
    elif incre == 5:
        frame.img = PhotoImage(file="dice5.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
    else:
        frame.img = PhotoImage(file="dice6.pbm")
        frame.canvas.itemconfig(frame.imgArea, image = frame.img)
        incre = 0
    frame.after(1000, update)
xbound = 240
ybound = 242
points = Canvas(frame, width=xbound, height = ybound)
point = []
h = []
random.seed()
n = 0
while n <= 100:
    n += 1
    s = randint(0,1000)
    h.append(s)
    if n == 100:
        rs = choice(h)
        seed(rs)
global z
z = 0
while z <= 100:
    z += 1
    if z < 10:
        y = randint(0,ybound)
        x = randint(0,xbound)
    else:
        y = randint(1,ybound)
        x = randint(1,xbound)
        point.append(x)
        point.append(y)
frame.after(0,update)
points.create_line(point)
points.pack( side = RIGHT)
root.mainloop()
