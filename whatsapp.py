from tkinter import *
import csv
from threading import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import time
import tkinter.messagebox
from selenium import webdriver
from tkinter import ttk



def threading():
    t1=Thread(target=printel)
    t1.start()


def group_contact(target_text):

        try:
            frame = Frame(window, width=350, height=480, bg="white")
            frame.place(x=440, y=456)
            p = ttk.Progressbar(frame, orient='horizontal', mode='indeterminate', length=300)
            p.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
            p.start()
            rb_results = []
            time.sleep(5)
            elm = WebDriverWait(driver, 70000).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span'))).text

            if elm == "click here for contact info" or elm == None:
                rb_results.append("0")
                print("end")

            else:
                rb_results.append(elm)
                print("go on...")

            with open("group_contact/rb_results.csv", "w", newline='') as resultFile:
                print("process go on ")
                writer = csv.DictWriter(resultFile, fieldnames=["Rb Results"], delimiter=',')
                writer.writeheader()
                writer.writerows({'Rb Results': item} for item in rb_results)
                resultFile.close()
            df = pd.read_csv("group_contact/rb_results.csv")
            rf = df.loc[0, 'Rb Results']
            rf = rf.replace(",", "\n")
            x = rf.split("\n")
            rf = ''
            im = 1
            for el in x:
                if (el.startswith(' +')):
                    rf = rf + str(target_text) + str(im) + ",* myContacts," + str(el) + "\n"
                    im = im + 1
            f = open('group_contact/' + target_text + '.csv', 'w', encoding="utf-8")
            f.write("Name,Group Membership,Phone 1 - Value\n")
            f.write(rf)
            f.close()
            if rb_results != "0" or len(rb_results) != 0:
                p.stop()
                frame.destroy()
                tkinter.messagebox.showinfo("Success!!",
                                            "Number is saved in group contact file and the file name is same as your typed name")
        except:
            pass


def printel():
    target = entry0.get()
    print("go on....")
    time.sleep(5)
    group_contact(target)




options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)
window = Tk()
window.title('Vraag Whatsapp Scrapper')
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

background_img = PhotoImage(file = f"media/w_background.png")
background = canvas.create_image(
    418, 264,
    image=background_img)

img0 = PhotoImage(file = f"media/w_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = threading,
    relief = "flat")

b0.place(
    x = 485, y = 330,
    width = 292,
    height = 50)

entry0_img = PhotoImage(file = f"media/w_img_textBox0.png")
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
