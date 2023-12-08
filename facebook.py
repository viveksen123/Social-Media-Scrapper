import tkinter
from threading import Thread
from tkinter import *
import re
import time
import csv
import  tkinter as tk
from tkinter import ttk

import requests
from bs4 import BeautifulSoup
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
import datetime

def post_content():
    frame = Frame(window, width=350, height=480, bg="white")
    frame.place(x=440, y=456)
    p = ttk.Progressbar(frame, orient='horizontal', mode='indeterminate', length=300)
    p.grid(column=0, row=0, columnspan=2, padx=20, pady=20)
    p.start()
    REQUEST_URL=''
    if r1_v.get()==0:
        REQUEST_URL = f'https://mbasic.facebook.com/search/posts/?q={entry0.get()}&source=filter&isTrending=0&paipv=0&eav=AfbFkOA34Ulew4XDWObbl7-w4wEIjOmVtk3nVVH-qUtpBE03fyb-KQhbeP3ho8LreRo&filters=eyJyZWNlbnRfcG9zdHM6MCI6IntcIm5hbWVcIjpcInJlY2VudF9wb3N0c1wiLFwiYXJnc1wiOlwiXCJ9IiwicnBfYXV0aG9yOjAiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0ifQ%3D%3D'
    if r1_v.get() == 1:
        REQUEST_URL = f'https://mbasic.facebook.com/search/posts/?q={entry0.get()}&source=filter&isTrending=0&paipv=0&eav=AfbFkOA34Ulew4XDWObbl7-w4wEIjOmVtk3nVVH-qUtpBE03fyb-KQhbeP3ho8LreRo&filters=eyJycF9jcmVhdGlvbl90aW1lOjAiOiJ7XCJuYW1lXCI6XCJjcmVhdGlvbl90aW1lXCIsXCJhcmdzXCI6XCJ7XFxcInN0YXJ0X3llYXJcXFwiOlxcXCIyMDIzXFxcIixcXFwic3RhcnRfbW9udGhcXFwiOlxcXCIyMDIzLTFcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMjNcXFwiLFxcXCJlbmRfbW9udGhcXFwiOlxcXCIyMDIzLTEyXFxcIixcXFwic3RhcnRfZGF5XFxcIjpcXFwiMjAyMy0xLTFcXFwiLFxcXCJlbmRfZGF5XFxcIjpcXFwiMjAyMy0xMi0zMVxcXCJ9XCJ9In0%3D'
    if r1_v.get() == 2:
        REQUEST_URL = f'https://mbasic.facebook.com/search/posts/?q={entry0.get()}&source=filter&isTrending=0&paipv=0&eav=AfbFkOA34Ulew4XDWObbl7-w4wEIjOmVtk3nVVH-qUtpBE03fyb-KQhbeP3ho8LreRo&filters=eyJycF9jcmVhdGlvbl90aW1lOjAiOiJ7XCJuYW1lXCI6XCJjcmVhdGlvbl90aW1lXCIsXCJhcmdzXCI6XCJ7XFxcInN0YXJ0X3llYXJcXFwiOlxcXCIyMDIyXFxcIixcXFwic3RhcnRfbW9udGhcXFwiOlxcXCIyMDIyLTFcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMjJcXFwiLFxcXCJlbmRfbW9udGhcXFwiOlxcXCIyMDIyLTEyXFxcIixcXFwic3RhcnRfZGF5XFxcIjpcXFwiMjAyMi0xLTFcXFwiLFxcXCJlbmRfZGF5XFxcIjpcXFwiMjAyMi0xMi0zMVxcXCJ9XCJ9In0%3D'

    mycookie = requests.session()
    mycookie.cookies.set('m_page_voice', '100091311618677', domain='.facebook.com')
    mycookie.cookies.set('presence', 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1684406170152%2C%22v%22%3A1%7D',
                         domain='.facebook.com')
    mycookie.cookies.set('fr', '0h2kqk7sHPkLlSWZq.AWXlSxNYAV-z5gozdjRFK67X9M8.BkZf1b.wY.AAA.0.0.BkZf-S.AWXh7Ej5dQ8',
                         domain='.facebook.com')
    mycookie.cookies.set('xs', '24%3Arw0Yw1Ksz6KeSw%3A2%3A1684406158%3A-1%3A-1', domain='.facebook.com')
    mycookie.cookies.set('c_user', '100091311618677', domain='.facebook.com')
    mycookie.cookies.set('wd', '1536x714', domain='.facebook.com')
    mycookie.cookies.set('dpr', '1.25', domain='.facebook.com')
    mycookie.cookies.set('datr', 'CXc6ZLhliJoUI3wWecCtShZf', domain='.facebook.com')
    mycookie.cookies.set('sb', 'B3c6ZGrWco4WFpDcpQVJF9Po', domain='.facebook.com')

    post_content = []
    post = []
    post_ad = []


    for k in range(0, 4):
        try:
            if k == 0:
                r = requests.get(REQUEST_URL, cookies=mycookie.cookies)

            else:
                time.sleep(10)
                r = requests.get(str(post_content[k - 1]), cookies=mycookie.cookies)
            soup = BeautifulSoup(r.content, "html.parser")
            print(soup)
            content = soup.findAll('div', {'class': 'bh bi', 'id': "see_more_pager"})
            for lines in content:
                post_content.append(str(lines.find('a').get('href')) + "\n")
        except:
            break



    for k in range(0, 4):
        try:
            time.sleep(10)
            print(post_content[k])
            r = requests.get(post_content[k], cookies=mycookie.cookies)
            soup = BeautifulSoup(r.content, "html.parser")

            content = soup.find_all("a",
                                    href=re.compile('story_fbid'))  # https://mbasic.facebook.com/story.php?story_fbid
            for lines in content:
                post.append('https://mbasic.facebook.com' + str(lines.get('href')) + "\n")
        except:
            break
    var = ''
    likes = []
    post=list(dict.fromkeys(post))
    post_content = ' '.join(post_content)
    print(len(post))
    date = []

    for q in post:
        time.sleep(5)
        print(q)
        r = requests.get(q, cookies=mycookie.cookies)
        soup = BeautifulSoup(r.content, "html.parser")
        date.append(soup.find('abbr').text)
        print("l")

    x = datetime.datetime.now()

    with open(f'./facebook/{entry0.get()}--{x.strftime("%d")}-{x.strftime("%m")}-{x.strftime("%Y")}--{x.strftime("%I")}-{x.strftime("%M")}-{x.strftime("%S")}.csv', mode="w", encoding="utf-8") as csvfile:
        fieldnames = ["S.no","Post","Date","Likes"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(post)):
            likes = []
            var = post[i].split('story_fbid=')[1]
            post_ad.append(var.split('&')[0])

            try:
                time.sleep(10)
                r = requests.get(
                    f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?ft_ent_identifier={post_ad[i]}&limit=50&reaction_type=1&reaction_id=1635855486666999&total_count=9&paipv=0&eav=AfZMrg5dldr_TUip0tY2qnAaXFlbdn4KKCVNpJrNdEA-aM_K_UI6kfkZmJ_VS_qzsKs',
                    cookies=mycookie.cookies)
                soup = BeautifulSoup(r.content, "html.parser")

                content = soup.find_all("a", href=re.compile(
                    str('&eav=')))  # https://mbasic.facebook.com/story.php?story_fbid


                j = 0
                for lines in content:
                    likes.append(str(j) + ' ' + str(lines.text) + ': https://mbasic.facebook.com' + str(
                        lines.get('href')) + "\n")
                    j = j + 1

            except:
                pass

            likes = ' '.join(likes)
            writer.writerow({"S.no": f'{i}', "Post": f'{post[i]}',"Date":f'{date[i]}', "Likes": f'{likes}'})
            print(post[i])
            print(post_ad[i])
    p.stop()
    frame.destroy()
    tkinter.messagebox.showinfo("Completed",
                                        "Scrapping is done")



def btn_clicked():
    print("Button Clicked")
    Thread(target=post_content).start()




window = Tk()
window.title('Vraag Facebook Scrapper')
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

background_img = PhotoImage(file = f"media/f_background.png")
background = canvas.create_image(
    418, 264,
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

entry0_img = PhotoImage(file = f"media/w_img_textBox0.png")
entry0_bg = canvas.create_image(
    610, 268,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#a6a1cc",
    highlightthickness = 0)

entry0.place(
    x = 480, y = 250,
    width = 240.0,
    height = 36)

canvas.create_text(
    530, 238,
    text = "Search Post",
    fill = "#000000",
    font = ("Anybody-Bold", int(13.0)))

r1_v = IntVar()

r1 = Radiobutton (text='Recent Post', variable=r1_v, value=0,bg = "#a6a1cc")
r1.place(

    x = 405, y = 320,
    width = 160.0,
    height = 36)

r2 = Radiobutton(text='2023', variable=r1_v, value=1,bg = "#a6a1cc")
r2.place(
    x = 535, y = 320,
    width = 160.0,
    height = 36)

r3 = Radiobutton( text='2022', variable=r1_v, value=2,bg = "#a6a1cc")
r3.place(
    x = 645, y = 320,
    width = 160.0,
    height = 36)


window.resizable(False, False)
window.mainloop()

