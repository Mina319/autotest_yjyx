from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException


class StudentUI:

    def mgr_login(self):
        wd = GSTORE['wd']
        wd.get('http://127.0.0.1/mgr/sign.html')
        wd.find_element(By.ID, 'username').send_keys('byhy')
        wd.find_element(By.ID, 'password').send_keys('88888888')
        # 点击登录
        (wd.find_element(By.CLASS_NAME, 'btn-flat')).click()