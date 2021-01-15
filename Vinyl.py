from tkinter import *
import pygame
from tkinter import filedialog
import os
from tinytag import TinyTag

win = Tk()
win.geometry("500x300")
win.resizable(width=False, height=False)
win.title("Vinyl Music Player")
win["bg"] = "White"
menubar = Menu(win)
win.config(menu=menubar)
pygame.mixer.init()


def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)


def dark():
    win["bg"] = "Black"
    Label(win, text="Dark Mode \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN, anchor=W).place(x=0, y=280)


def white():
    win["bg"] = "White"
    Label(win, text="Light mode \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN, anchor=W).place(x=0, y=280)


def open_():
    global w
    global r
    global k
    w = filedialog.askopenfilename()
    r = os.path.basename(w)
    k = TinyTag.get(w)
    win.update()
    win.update_idletasks()
    pygame.mixer.init()
    Button(win, image=q, borderwidth=0, command=main_play).place(x=20, y=20)


def play():
    pygame.mixer.music.unpause()
    win.update()
    win.update_idletasks()


def pause():
    pygame.mixer.music.pause()
    win.update()
    win.update_idletasks()


def main_play():
    pygame.mixer.init()
    pygame.mixer.music.load(w)
    pygame.mixer.music.play()
    Button(win, image=q, borderwidth=0, command=play).place(x=20, y=20)
    win.update()
    win.update_idletasks()


q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")
o = PhotoImage(file="Forward.png")
p = PhotoImage(file="Rewind.png")

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=open_)
subMenu.add_command(label="Exit", command=win.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Modes", menu=subMenu)
subMenu.add_command(label="Light", command=white)
subMenu.add_command(label="Dark", command=dark)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us")

statusbar = Label(win, text="Open an audio file... \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN, anchor=W)
statusbar.place(x=0, y=280)

scale = Scale(from_=100, to=0, orient=VERTICAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.place(x=725, y=655)

Button(win, image=q, borderwidth=0, command=main_play).place(x=20, y=20)
Button(win, image=t, borderwidth=0, command=pause).place(x=100, y=20)
Button(win, image=p, borderwidth=0).place(x=180, y=20)
win.mainloop()
