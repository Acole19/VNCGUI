import Tkinter as tk
from PIL import Image
import time

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open('twosidesheadsnb.pbm'))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback():
    global start_time
    global timemult
    timecurrent = time.time() - start_time
    if timecurrent % 2 == 0:
        img2 = ImageTk.PhotoImage(Image.open('twosidesheadsnb.pbm'))
        panel.configure(image=img2)
        panel.image = img2
    else:
        img2 = ImageTk.PhotoImage(Image.open('twosidestails.pbm'))
        panel.configure(image=img2)
        panel.image = img2
    root.after(2505, callback)

start_time = time.time()
timemult = start_time % 5
root.mainloop()
root.after(5000, callback)
