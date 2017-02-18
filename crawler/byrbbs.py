from bs4 import BeautifulSoup
import requests
import os
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password


class Crawler(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("https://bbs.byr.cn/login")
        time.sleep(3)
        print('--------get--------')
    def login(self,user):
        username = self.driver.find_element_by_id('u_login_id')
        password = self.driver.find_element_by_id('u_login_passwd')
        username.send_keys(user.username)
        password.send_keys(user.password)
        self.driver.find_element_by_id('u_login_submit').click()
        time.sleep(3)


if __name__ == '__main__':
    username = os.environ.get('BYR_USERNAME')
    password = os.environ.get('BYR_PASSWORD')
    print(username,password)
    user = User(username,password)
    crawler = Crawler()
    crawler.login(user)
