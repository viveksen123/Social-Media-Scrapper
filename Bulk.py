import os
from threading import Thread
from tkinter import *


def threading():
    t1 = Thread(target=group_contact)
    t1.start()

def group_contact():
    os.system('py csv_w.py')


window = Tk()
window.title('Bulk Message Sender')
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

background_img = PhotoImage(file = f"./media/b_background.png")
background = canvas.create_image(
    410,270,
    image=background_img)



img1 = PhotoImage(file = f"./media/b_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = threading,
    relief = "flat")

b1.place(
    x = 460, y =350,
    width = 309,
    height = 59)



canvas.create_text(
    600, 280,
    text = "Send whatsaap Messages without saving number",
    fill = "#000000",
    font = ("Anybody-Bold", int(14.0)))

window.resizable(False, False)
window.mainloop()




'''from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

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

background_img = PhotoImage(file = f"./media/b_background.png")
background = canvas.create_image(
   418, 264,
    image=background_img)

img0 = PhotoImage(file = f"./media/b_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 470, y = 420,
    width = 292,
    height = 50)

img1 = PhotoImage(file = f"./media/b_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 460, y =350,
    width = 309,
    height = 59)

canvas.create_text(
    600, 280,
    text = "Send whatsaap Messages without saving number",
    fill = "#000000",
    font = ("Anybody-Bold", int(14.0)))

window.resizable(False, False)
window.mainloop()'''
