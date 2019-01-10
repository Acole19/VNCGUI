import Tkinter
from Tkinter import *
from PIL import Image
root = Tk()
canvas = Canvas(root, width=240, height = 242)
canvas.create_oval(10, 10, 80, 80, outline="#f11",
            width=2)
z = [1,5,7,9]
v = 0
a = 1
b = 1
c = 2
while v <= 3:
    z.append(c)
    a = b + c
    b = a + c
    c = a + b
    v += 1
    z.append(a)
canvas.create_line(z)
canvas.pack()
root.mainloop()
