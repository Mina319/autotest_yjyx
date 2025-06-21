import string
import random

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


def generate_mixed_string(length=100):
    # 定义字符集
    chinese_chars = [chr(i) for i in range(0x4e00, 0x9fa5 + 1)]  # 常用汉字范围
    english_chars = string.ascii_letters  # 所有英文字母
    special_chars = "*()"  # 特殊字符

    # 组合所有可能的字符
    all_chars = chinese_chars + list(english_chars) + list(special_chars)

    # 随机选择字符直到达到指定长度
    result = []
    for _ in range(length):
        char = random.choice(all_chars)
        result.append(char)

    return ''.join(result)
