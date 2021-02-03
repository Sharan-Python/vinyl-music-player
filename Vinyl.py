from tkinter import *
from tkinter import ttk
import pygame
from tkinter import filedialog
from PIL import ImageTk, Image
from tinytag import TinyTag
import os


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
          "Powered By Python \n Version 1.0 \n Problems? Feel free to create an issue on Github \n Do fork your own "
          "version... to contribute")


def set_vol(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)


def dark():
    win["bg"] = "Black"
    status(status_="Dark mode \t\t\t\t\t\t\t\t\t\t\t\t")


def white():
    win["bg"] = "White"
    status(status_="Light mode \t\t\t\t\t\t\t\t\t\t\t\t")


def delete():
    try:
        cursel = list1.curselection()
        list1.delete(cursel[0])
        status(status_="Deleted \t\t\t\t\t\t\t\t\t\t\t\t")
    except IndexError:
        status(status_="There is no song, please add a song to delete it \t\t\t\t\t\t\t\t\t\t\t")


def delete_all():
    list1.delete(0, END)
    status(status_="Deleted all \t\t\t\t\t\t\t\t\t\t\t\t")


def open_last_inst():
    try:
        pope = open("DUMP.txt", "r")
        rope = pope.readlines()
        var = rope[-1]
        list_dir_os = os.listdir(var)
        for item in list_dir_os:
            list1.insert(END, var + "/" + item)
        if str(list_dir_os[any(list_dir_os)]).endswith('.mp3'):
            pygame.mixer.init()
            list1.selection_set(END)
            status(status_="Opened a Music directory from previously opened folder\t\t\t\t\t\t\t\t\t\t\t\t")
    except FileNotFoundError or IndexError:
        pass
    try:
        ima = var + "/" + "cover.jpg"
        imgp = Image.open(ima)

        # resize the image and apply a high-quality down sampling filter
        imgp = imgp.resize((110, 110), Image.ANTIALIAS)

        # PhotoImage class is used to add image to widgets, icons etc
        imgp = ImageTk.PhotoImage(imgp)

        # create a label
        panel = Label(win, image=imgp)

        # set the image as img
        panel.image = imgp
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


def open_():
    try:
        global w, img, rp
        global r
        global k
        global ll, pp
        w = filedialog.askopenfilename(initialdir='', title="Choose A Song", filetypes=(("Music Files", "*.mp3 *.wav "
                                                                                                        "*.ogg *.mx "
                                                                                                        "*.mod"),))
        # ll = os.listdir(w)
        if w != "":
            list1.insert(END, w)
        if str(w).endswith('.mp3'):
            pygame.mixer.init()
            list1.selection_set(END)
            tag = TinyTag.get(w)
            Label(win, text=tag.title + " \t \t \t \t \t \t \t \t \t \t \t \t", bd=1, relief=SUNKEN,
                  anchor=W).place(x=0, y=280)
    except FileNotFoundError or NameError or OSError:
        status(status_="You didn't choose a file \t\t\t\t\t\t\t\t\t\t\t\t")
    try:
        img = Image.open(w.strip(os.path.basename(w)) + "cover.jpg")

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


def open_fol():
    try:
        global w, img, rp
        global r
        global k
        global ll, pp
        w = filedialog.askdirectory()
        pope = open("DUMP.txt", "w")
        pope.write(w)
        list_dir_os = os.listdir(w)
        for item in list_dir_os:
            list1.insert(END, w + "/" + item)
        if str(list_dir_os[any(list_dir_os)]).endswith('.mp3'):
            pygame.mixer.init()
            list1.selection_set(END)
            status(status_="Opened a Music directory \t\t\t\t\t\t\t\t\t\t\t\t")
    except FileNotFoundError or NameError or OSError:
        status(status_="Open a file/folder \t\t\t\t\t\t\t\t\t\t\t\t")
    try:
        ima = w + "/" + "cover.jpg"
        img = Image.open(ima)

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


def next_():
    try:
        currsel = list1.curselection()
        aa = int(currsel[0])
        next_one = aa + 1
        next_one_int = int(next_one)
        list1.selection_clear(aa)
        list1.selection_set(next_one_int)
        pygame.mixer.init()
        pygame.mixer.music.load(list1.get(next_one_int))
        pygame.mixer.music.play()
        base = os.path.basename(list1.get(next_one_int))
        status(status_=base + "\t\t\t\t\t\t\t\t\t\t\t")
    except pygame.error or IndexError:
        pass


def prev_():
    try:
        currsel = list1.curselection()
        aa = int(currsel[0])
        next_one = aa - 1
        (type(next_one))
        next_one_int = int(next_one)
        list1.selection_clear(aa)
        list1.selection_set(next_one_int)
        # Add One To The Current Song Number Tuple/lis
        pygame.mixer.init()
        pygame.mixer.music.load(list1.get(next_one_int))
        pygame.mixer.music.play()
        base = os.path.basename(list1.get(next_one_int))
        status(status_=base + "\t\t\t\t\t\t")
    except pygame.error or IndexError:
        pass


def play():
    pygame.mixer.music.unpause()
    win.update()
    win.update_idletasks()


def pause():
    pygame.mixer.music.pause()
    Button(win, image=q, borderwidth=0, command=play).place(x=20, y=20)
    win.update()
    win.update_idletasks()


def main_play():
    try:
        global lpp
        pygame.mixer.init()
        pygame.mixer.music.load(list1.get(0))
        list1.selection_set(0)
        pygame.mixer.music.play()
        Button(win, image=q, borderwidth=0, command=play).place(x=20, y=20)

    except pygame.error or OSError or TypeError:
        status(status_="Sorry, Vinyl could not read this song \t\t\t\t\t\t\t\t\t\t\t\t")


q = PhotoImage(file="PlayButton.png")
t = PhotoImage(file="PauseButton.png")
o = PhotoImage(file="Forward.png")
p = PhotoImage(file="Rewind.png")

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open a Song", command=open_)
subMenu.add_command(label="Open a Music folder", command=open_fol)
subMenu.add_command(label="Exit", command=win.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Modes", menu=subMenu)
subMenu.add_command(label="Light", command=white)
subMenu.add_command(label="Dark", command=dark)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Delete", menu=subMenu)
subMenu.add_command(label="Delete a song", command=delete)
subMenu.add_command(label="Delete all songs", command=delete_all)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about)


def status(status_):
    statusbar = Label(win, text=status_, bd=1, relief=SUNKEN, anchor=W)
    statusbar.place(x=0, y=280)


status(status_="Open an audio file \t\t\t\t\t\t\t\t\t\t\t\t")

scale = Scale(from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
pygame.mixer.music.set_volume(0.10)
scale.place(x=35, y=90)

Button(win, image=q, borderwidth=0, command=main_play).place(x=20, y=20)
Button(win, image=o, borderwidth=0, command=next_).place(x=360, y=200)
Button(win, image=t, borderwidth=0, command=pause).place(x=100, y=20)
Button(win, image=p, borderwidth=0, command=prev_).place(x=280, y=200)

list1 = Listbox(win, bg="dark grey", fg="black", width=40)
list1.place(x=210, y=10)

open_last_inst()
win.mainloop()
