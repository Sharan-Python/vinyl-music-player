from tkinter import *
from tkinter import ttk
import pygame
from tkinter import filedialog
import os
from tinytag import TinyTag
from PIL import ImageTk, Image

win = Tk()
win.geometry("500x300")
win.resizable(width=False, height=False)
win.title("Vinyl Music Player")
win["bg"] = "White"
menubar = Menu(win)
win.config(menu=menubar)
pygame.mixer.init()


# class for About us
class Popup(Toplevel):
    def __init__(self, title='', message='', master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title(title)

        lbl = Label(self, text=message, font=('bold', 14))
        lbl.pack()
        btn = ttk.Button(self, text="OK", command=self.destroy)
        btn.pack()

        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)


def about():
    Popup("About Us",
          "Powered By Python \n Version 1.0 \n Problems? Feel free to create an issue on Github \n Do fork your own version...")


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
    try:
        global w, img, rp
        global r
        global k
        w = filedialog.askopenfilename()
        k = TinyTag.get(w)
        gr = k.title
        pl = os.path.basename(w)
        rp = w.strip(pl)
        win.update()
        win.update_idletasks()
        pygame.mixer.init()
        Button(win, image=q, borderwidth=0, command=main_play).place(x=20, y=20)
        Label(win, text=gr + "\t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN,
              anchor=W).place(x=0, y=280)
        list1.insert(END, pl)
    except FileNotFoundError or NameError or OSError:
        Label(win, text="You didn't choose a file \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN,
              anchor=W).place(x=0,
                              y=280)
    try:
        img = Image.open(rp + "cover.jpg")

        # resize the image and apply a high-quality down sampling filter
        img = img.resize((110, 110), Image.ANTIALIAS)

        # PhotoImage class is used to add image to widgets, icons etc
        img = ImageTk.PhotoImage(img)

        # create a label
        panel = Label(win, image=img)

        # set the image as img
        panel.image = img
        panel.place(x=35, y=160)
    except FileNotFoundError or NameError or OSError:
        ko = Image.open("Vinyl Music Player icon.png")

        # resize the image and apply a high-quality down sampling filter
        ko = ko.resize((110, 110), Image.ANTIALIAS)

        # PhotoImage class is used to add image to widgets, icons etc
        ko = ImageTk.PhotoImage(ko)

        # create a label
        kok = Label(win, image=ko)

        # set the image as img
        kok.image = ko
        kok.place(x=35, y=160)


def play():
    pygame.mixer.music.unpause()
    win.update()
    win.update_idletasks()


def pause():
    pygame.mixer.music.pause()
    win.update()
    win.update_idletasks()


def main_play():
    try:
        wer = rp + list1.get(END)
        pygame.mixer.init()
        pygame.mixer.music.load(wer)
        pygame.mixer.music.play()
        Button(win, image=q, borderwidth=0, command=play).place(x=20, y=20)
        win.update()
        win.update_idletasks()
    except pygame.error or OSError:
        Label(win,
              text="Sorry, Vinyl could not read this song. Try playing some other song? \t \t \t \t \t \t \t \t \t \t \t \t",
              bd=1, relief=SUNKEN, anchor=W).place(x=0,
                                                   y=280)


q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")

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
subMenu.add_command(label="About Us", command=about)

statusbar = Label(win, text="Open an audio file... \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN, anchor=W)
statusbar.place(x=0, y=280)

scale = Scale(from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.7)
scale.place(x=35, y=90)

list1 = Listbox(win, bg="dark grey", fg="black", width=40)
list1.place(x=210, y=10)

Button(win, image=q, borderwidth=0, command=main_play).place(x=20, y=20)
Button(win, image=t, borderwidth=0, command=pause).place(x=100, y=20)

win.mainloop()
