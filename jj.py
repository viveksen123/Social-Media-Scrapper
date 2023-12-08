import tkinter
from threading import Thread
from tkinter import *
import re
import time
import csv_w
import  tkinter as tk
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
from tkinter import *
import csv_w
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
import datetime



def post_content():
    post=[]
    try:
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        content = soup.findAll("a",href=re.compile('/p/'))
        for lines in content:
            post.append('https://www.instagram.com' + str(lines.get('href')))
    except:
        pass
    x = datetime.datetime.now()
    with open(f'./instagram/{x.strftime("%d")}-{x.strftime("%m")}-{x.strftime("%Y")}--{x.strftime("%I")}-{x.strftime("%M")}-{x.strftime("%S")}.csv', mode="w", encoding="utf-8") as csvfile:
        fieldnames = ["S.no", "Post", "Likes"]
        writer = csv_w.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        try:
            for i in range(0, len(post)):
                likes = []
                time.sleep(10)
                driver.get(f'{post[i]}liked_by/')
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, "html.parser")

                content = soup.find_all("a",{"class":"x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"} )  # https://mbasic.facebook.com/story.php?story_fbid
                j = 0
                for lines in content:
                    likes.append(str(j) + ' ' + str(lines.text) + ': https://www.instagram.com' + str(
                        lines.get('href')) + "\n")
                    j = j + 1
        except:
            pass
        likes = ' '.join(likes)
        writer.writerow({"S.no": f'{i}', "Post": f'{post[i]}', "Likes": f'{likes}'})
        print(post[i])
        print(likes)






def btn_clicked():
    print("Button Clicked")
    Thread(target=post_content).start()




web="https://www.instagram.com/"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
driver.get(web)
wait = WebDriverWait(driver, 300)
mycookie={'name':'csrftoken','value':'zzks3DizJEk5fDVMDitcC70bFbbLBIro','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'sessionid','value':'58752565917%3AP0E2H2dou5CO5F%3A27%3AAYd1c91anmsaMtsAkkJ_hq7zEVOdnAVIa0OE3pGEcw','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'shbts','value':'\"1680464427\\0544271513322\\0541712000427:01f7413289fa431f2f7206c94acb6c63f552f17d4b4ec2380a5c1ba1bb5b02af13ac9c63\"','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'rur','value':'\"CCO\\05458752565917\\0541712172280:01f7112f253a209b8ad63e708af1ce5185bfca3afa587d63a74fb9a7212eb09f76f9a62b\"','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'shbid','value':'\"2980\\0544271513322\\0541712000427:01f771809ad5cfe8a629c34142605759f1316b4f60eb18d706e4d686126b1bcc425b8a60\"','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'ig_nrcb','value':'1','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'datr','value':'Xj0lZFoBOiuAi8FNEbeqw4zi','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'ds_user_id','value':'58752565917','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'ig_did','value':'80A1F4CF-325F-4A3D-918E-1F4A62AD9EF7','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'mid','value':'ZCU9YAALAAF01vv0FTF57GRd4m5r','domain':'.instagram.com'}
driver.add_cookie(mycookie)

mycookie={'name':'dpr','value':'1.25','domain':'.instagram.com'}
driver.add_cookie(mycookie)
driver.refresh()
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

background_img = PhotoImage(file = f"media/i_background.png")
background = canvas.create_image(
    418, 220,
    image=background_img)

img0 = PhotoImage(file = f"media/f_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x =470, y = 390,
    width = 281,
    height = 61)

window.resizable(False, False)
window.mainloop()
