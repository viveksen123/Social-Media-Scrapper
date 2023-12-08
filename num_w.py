from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("854x612")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 612,
    width = 854,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./media/n_background.png")
background = canvas.create_image(
    427, 300,
    image=background_img)

img0 = PhotoImage(file = f"./media/n_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 527, y = 468,
    width = 181,
    height = 43)

img1 = PhotoImage(file = f"./media/n_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 540, y =520,
    width = 154,
    height = 41)

window.resizable(False, False)
window.mainloop()
