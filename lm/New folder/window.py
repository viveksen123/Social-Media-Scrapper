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
    410,270,
    image=background_img)

window.resizable(False, False)
window.mainloop()
