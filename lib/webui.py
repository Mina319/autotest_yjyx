from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException


def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    #  使用 Hytest 的全局变量 GSTORE，把浏览器实例 wd 存进去，方便其他函数拿来用
    GSTORE['wd'] = wd


def mgr_login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.find_element(By.ID, 'username').send_keys('byhy')
    wd.find_element(By.ID, 'password').send_keys('88888888')
    # 点击登录
    (wd.find_element(By.CLASS_NAME, 'btn-flat')).click()

