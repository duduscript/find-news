from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
import json

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password


class Crawler(object):
    def __init__(self):
        self.USER_AGENTS = (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
            'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
            'Chrome/19.0.1084.46 Safari/536.5'),
            ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46''Safari/536.5')
        )
        self.url = "https://bbs.byr.cn"
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.s = None
        time.sleep(3)
        print('--------get--------')
    def login(self,user):
        username = self.driver.find_element_by_id('id')
        password = self.driver.find_element_by_id('pwd')
        username.send_keys(user.username)
        password.send_keys(user.password)
        self.driver.find_element_by_id('b_login').click()
        time.sleep(5)
    def get_top_ten(self):
        soup = BeautifulSoup(self.driver.page_source,'lxml')
        topten_ul = soup.find('li',id='topten').ul
        for li in topten_ul.find_all('li'):
            print(self.url+li.a['href'])
            r = self.s.get(self.url+li.a['href'])
            #print(r.text)
    def changetorequests(self):
        cookies = self.driver.get_cookies()
        self.s = requests.Session()
        for cookie in cookies:
            self.s.cookies.set(cookie['name'],cookie['value'])
        print(self.s.cookies)
        


if __name__ == '__main__':
    username = os.environ.get('BYR_USERNAME')
    password = os.environ.get('BYR_PASSWORD')
    user = User(username,password)
    crawler = Crawler()
    crawler.login(user)
    #crawler.get_top_ten()
    crawler.changetorequests()
    crawler.get_top_ten()