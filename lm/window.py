from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("820x526")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 526,
    width = 820,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    418, 220,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 470, y = 420,
    width = 232,
    height = 46)

window.resizable(False, False)
window.mainloop()
