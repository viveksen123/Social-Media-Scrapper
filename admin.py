import os
from threading import Thread
from tkinter import *

def run_fac():
    Thread(target=run_fac_t1).start()
def run_fac_t1():
    os.system('py facebook.py')

def run_wa():
    Thread(target=run_wa_t1).start()
def run_wa_t1():
    os.system('py whatsapp.py')

def run_in():
    Thread(target=run_in_t1).start()
def run_in_t1():
    os.system('py instagram.py')

def run_bon():
    Thread(target=run_bon_t1).start()
def run_bon_t1():
    s=str("Bulk.py")
    os.system(f'py {s}')

window = Tk()
window.title('Vraag Scrapper')
window.geometry("820x526")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 526,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"media/ad_background.png")
background = canvas.create_image(
    430.5, 227.0,
    image=background_img)

img0 = PhotoImage(file = f"media/ad_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = run_fac,
    relief = "flat")

b0.place(
    x = 430, y = 220,
    width = 354,
    height = 61)

img1 = PhotoImage(file = f"media/ad_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    command=run_in,
    highlightthickness = 0,
    relief = "flat")

b1.place(
    x = 432, y = 310,
    width = 354,
    height = 61)

img2 = PhotoImage(file = f"media/ad_img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    command=run_wa,
    highlightthickness = 0,
    relief = "flat")

b2.place(
    x = 432, y =395,
    width = 354,
    height = 61)

img5 = PhotoImage(file = f"./media/img11.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command=run_bon,
    relief = "flat")

b5.place(
    x = 460, y =460,
    width = 309,
    height = 59)

window.resizable(False, False)
window.mainloop()
