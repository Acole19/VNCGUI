import pygame
from tkinter import *
root = Tk()
pygame.init()
def play():
    pygame.mixer.music.load("ticking.mp3") #Loading File Into Mixer
    pygame.mixer.music.play(loops = 10) #Playing It In The Whole Device
Button(root,text="Play",command=play).pack()
root.mainloop()
