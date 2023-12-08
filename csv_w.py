from selenium.webdriver.support.wait import WebDriverWait
try:
    import Tkinter as tk
except:
    import tkinter as tk
from threading import Thread
from tkinter import filedialog as fd
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from threading import Thread
from tkinter import *
from selenium.webdriver.support.wait import WebDriverWait
try:
    import Tkinter as tk
except:
    import tkinter as tk
from tkinter import filedialog as fd

name=[]
attach=[]
message= Text
def threading():
        t1 = Thread(target=group_contact)
        t1.start()

def save_unsavedContact(unsaved_contact, length, i,target_text,message):
        if len(attach) > 0 or len(message) > 0:
            try:
                link = "https://web.whatsapp.com/send?phone={}&text&source&data&app_absent".format(unsaved_contact)
                # driver  = webdriver.Chrome()
                driver.get(link)
                l3 = Label(text=target_text+":  "+str(i + 1) + "/" + str(length), font=('Helvetica', 12, "bold"))
                l3.place(x=450, y=425)
                try:
                    time.sleep(5)
                    driver.implicitly_wait(10)
                    if len( attach) >0:
                        for x in  attach:
                            time.sleep(2)
                            attachment_box = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH,'//div[@title = "Attach"]')))
                            attachment_box.click()
                            image_box = WebDriverWait( driver, 300).until(EC.presence_of_element_located((By.XPATH,
                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
                            image_box.send_keys(x)
                            time.sleep(3)
                            send_button = WebDriverWait( driver, 300).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
                            send_button.click()
                            time.sleep(2)
                    if len(message) > 0:
                        input_box = WebDriverWait( driver, 300).until(EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')))
                        """for ch in message:
                            if ch == "\n":
                                ActionChains( driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
                                    Keys.ENTER).key_up(
                                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                            else:
                                input_box.send_keys(ch)
                        input_box.send_keys(Keys.ENTER)"""
                        input_box.send_keys(Keys.CONTROL + "v")
                        time.sleep(2)
                        input_box.send_keys(Keys.ENTER)
                        time.sleep(10)

                except Exception as e:
                     pass
                time.sleep(3)
            except:
                pass

def group_contact():

        window.clipboard_append(message.get("1.0", "end-1c"))
        for j in range(0,len(name)):
            target_text=name[j]
            time.sleep(5)
            df = pd.read_csv(target_text)
            length = len(df.axes[0])

            for i in range(0, length):
                rf = df.loc[i, 'Phone 1 - Value']
                save_unsavedContact(rf, length, i,target_text,message.get("1.0", "end-1c"))

def btn_clicked():
    print("Button Clicked")
    '''Thread(target=group_contact).start()'''

def callback():
        wa = fd.askopenfilename()
        name.append(wa)
        l2 = Label( text=wa, font=('Helvetica', 12, "bold"),bg="#a6a1cc")
        l2.place(
            x=485, y=200,

        )

def attachments():
        d = fd.askopenfilename()
        attach.append(d)
        l4 = Label(text=attach, font=('Helvetica', 12, "bold"),bg="#a6a1cc")
        l4.place(
            x=480, y=400
        )

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)

window = Tk()
window.title('Send by CSV')
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

background_img = PhotoImage(file = f"./media/c_background.png")
background = canvas.create_image(
    418,240,
    image=background_img)

img0 = PhotoImage(file = f"./media/c_img0.png")#send
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = threading,
    relief = "flat")

b0.place(
    x=470, y=470,
    width = 283,
    height = 35)

message = Text(height=6,width=52,border=5,bg = "#a6a1cc")
message.place(x=390, y=280)

img1 = PhotoImage(file = f"./media/c_img1.png")#attac
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = attachments,
    relief = "flat")

b1.place(
    x=480, y=430,
    width = 269,
    height = 31)

img2 = PhotoImage(file = f"./media/c_img2.png")#choose
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = callback,
    relief = "flat")

b2.place(
    x = 520, y = 235,
    width = 157,
    height = 40)

window.resizable(False, False)
window.mainloop()
