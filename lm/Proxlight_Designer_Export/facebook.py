from tkinter import *
import re
import time
import csv_w

import requests
from bs4 import BeautifulSoup



def post_content():
    REQUEST_URL = f'https://mbasic.facebook.com/search/posts/?q=masterofcomputerapplication'
    mycookie = requests.session()
    mycookie.cookies.set('m_page_voice', '100091311618677', domain='.facebook.com')

    mycookie.cookies.set('fr', '0YFbqeLck4ICfhJbV.AWX3_IgEM1fCYpYwYVjhbB9WX9Y.BkJ-gx.tX.AAA.0.0.BkJ-gx.AWV6qLICPWM',
                         domain='.facebook.com')

    mycookie.cookies.set('xs', '49%3AK8rS3Oo8jS_pzw%3A2%3A1680336945%3A-1%3A-1', domain='.facebook.com')

    mycookie.cookies.set('c_user', '100091311618677', domain='.facebook.com')

    mycookie.cookies.set('IDE', 'AHWqTUlumNu1s141QQBBqRETJZ1M2Wu2p09HSV21S6tzrLoZ7YtCfwH0oa2SKZoo',
                         domain='.facebook.com')

    mycookie.cookies.set('sb', 'A-gnZPrQPwvaLUHZDGg8MEgZ', domain='.facebook.com')

    mycookie.cookies.set('datr', '_ecnZE52CH7rn97VpKMCEWAt', domain='.facebook.com')
    post_content = []
    post = []
    post_ad = []

    for k in range(0, 5):
        try:
            if k == 0:
                r = requests.get(REQUEST_URL, cookies=mycookie.cookies)
            else:
                time.sleep(10)
                r = requests.get(str(post_content[k - 1]), cookies=mycookie.cookies)
            soup = BeautifulSoup(r.content, "html.parser")
            print(soup)
            content = soup.findAll('div', {'class': 'bg bh', 'id': "see_more_pager"})
            for lines in content:
                post_content.append(str(lines.find('a').get('href')) + "\n")
        except:
            break

    for k in range(0, 5):
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
    post = [*set(post)]
    post_content = ' '.join(post_content)
    print(len(post))
    with open("names.csv", mode="w", encoding="utf-8") as csvfile:
        fieldnames = ["S.no", "Post", "Likes"]
        writer = csv_w.DictWriter(csvfile, fieldnames=fieldnames)
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
            writer.writerow({"S.no": f'{i}', "Post": f'{post[i]}', "Likes": f'{likes}'})
            print(post[i])
            print(post_ad[i])

    return post_content


def btn_clicked():
    print("Button Clicked")
    print(post_content())


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
    x =470, y = 420,
    width = 281,
    height = 61)

window.resizable(False, False)
window.mainloop()
