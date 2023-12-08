import time
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

web="https://www.instagram.com/explore/tags/masterofcomputerapplication/"
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
while True:
    wait = WebDriverWait(driver, 300)
