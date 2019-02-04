import Tkinter
from Tkinter import *
from PIL import Image
import random
from random import seed
from random import randint
from random import choice
root = Tk()
xbound = 240
ybound = 242
canvas = Canvas(root, width=xbound, height = ybound)
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

canvas.create_line(point)
canvas.pack()
root.mainloop()
