from tkinter import *


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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    418, 264,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 485, y = 330,
    width = 292,
    height = 50)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    630, 268,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#a6a1cc",
    highlightthickness = 0)

entry0.place(
    x = 500, y = 250,
    width = 240.0,
    height = 36)

canvas.create_text(
    590, 238,
    text = "ENTER CSV FILE NAME",
    fill = "#000000",
    font = ("Anybody-Bold", int(13.0)))

window.resizable(False, False)
window.mainloop()
