from threading import Thread
from threading import Thread
from tkinter import *
import re
import time
import csv_w
import  tkinter as tk
from tkinter import ttk


def tm():
    lpm = 5
    lpm=lpm+1

def btn_clicked(t):
    print("Button Clicked")
    Thread(target=tm).start()

    t.title('Progress Bar')
    t.geometry('300x100')
    t.grid()
    p = ttk.Progressbar(t, orient='horizontal', mode='indeterminate', length=300)
    p.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
    p.start()
    t.mainloop()


t = tk.Tk()
btn_clicked(t)
t.destroy()




