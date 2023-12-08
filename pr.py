import re
import time
import csv_w

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from csv_w import DictReader
import browser_cookie3
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class FaceBookBot():
    login_basic_url = 'https://mbasic.facebook.com/login'
    login_mobile_url = 'https://m.facebook.com/login'
    payload = {
    }

    post_ID = ""

    def parse_html(self, request_url):
        with requests.Session() as session:
            post = session.post(self.login_basic_url, data=self.payload)
            parsed_html = session.get(request_url)
        return parsed_html

    def post_content(self):
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

                content = soup.find_all("a", href=re.compile(
                    'story_fbid'))  # https://mbasic.facebook.com/story.php?story_fbid
                for lines in content:
                    post.append('https://mbasic.facebook.com' + str(lines.get('href')) + "\n")
            except:
                break
        var = ''
        post = [*set(post)]
        post_content = ' '.join(post_content)
        print(len(post))
        with open("names.csv", mode="w") as csvfile:
            fieldnames = ["S.no", "Post", "pid"]
            writer = csv_w.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0, len(post)):
                var = post[i].split('story_fbid=')[1]
                post_ad.append(var.split('&')[0])

                writer.writerow({"S.no": f'{i}', "Post": f'{post[i]}', "pid": f'{post_ad[i]}'})
                print(post[i])
                print(post_ad[i])

        return post_content

    def date_posted(self):
        REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'

        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        date_posted = soup.find('abbr')
        return date_posted.text

    def post_likes(self):
        limit = 200
        REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit={limit}&total_count=17&ft_ent_identifier={self.post_ID}'

        soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
        names = soup.find_all('h3')
        people_who_liked = []
        for name in names:
            people_who_liked.append(name.text)
        people_who_liked = [i for i in people_who_liked if i]
        return people_who_liked

    def post_shares(self):
        REQUEST_URL = f'https://m.facebook.com/browse/shares?id={self.post_ID}'

        with requests.Session() as session:
            post = session.post(self.login_mobile_url, data=self.payload)
            parsed_html = session.get(REQUEST_URL)

        soup = BeautifulSoup(parsed_html.content, "html.parser")
        names = soup.find_all('span')
        people_who_shared = []
        for name in names:
            people_who_shared.append(name.text)
        return people_who_shared


'''def pr():
    elm = WebDriverWait(driver, 70000).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]'))).text

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\jaind\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
driver.get("https://mbasic.facebook.com/search/posts/?q=masterofcomputerapplication")
wait = WebDriverWait(driver, 300)
print(driver.get_cookies())
mycookie={'name':'m_page_voice','value':'100091311618677','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'fr','value':'0YFbqeLck4ICfhJbV.AWX3_IgEM1fCYpYwYVjhbB9WX9Y.BkJ-gx.tX.AAA.0.0.BkJ-gx.AWV6qLICPWM','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'xs','value':'49%3AK8rS3Oo8jS_pzw%3A2%3A1680336945%3A-1%3A-1','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'c_user','value':'100091311618677','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'IDE','value':'AHWqTUlumNu1s141QQBBqRETJZ1M2Wu2p09HSV21S6tzrLoZ7YtCfwH0oa2SKZoo','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'sb','value':'A-gnZPrQPwvaLUHZDGg8MEgZ','domain':'.facebook.com'}
driver.add_cookie(mycookie)

mycookie={'name':'datr','value':'_ecnZE52CH7rn97VpKMCEWAt','domain':'.facebook.com'}
driver.add_cookie(mycookie)
driver.refresh()
print(driver.get_cookies())
'''
bot = FaceBookBot()

bot.post_ID = "2987237771603619"

print(bot.post_content())
