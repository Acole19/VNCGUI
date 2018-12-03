import Tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
img = ImageTk.PhotoImage(Image.open('twosidesheadsnb.pbm'))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    global count
    if count % 2 == 0:
        img2 = ImageTk.PhotoImage(Image.open('twosidesheadsnb.pbm'))
        panel.configure(image=img2)
        panel.image = img2
        count +=1
    else:
        img2 = ImageTk.PhotoImage(Image.open('twosidestails.pbm'))
        panel.configure(image=img2)
        panel.image = img2
        count +=1

count = 0
root.bind("<Return>", callback)
root.mainloop()
