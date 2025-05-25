from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException


class TeacherUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        wd = webdriver.Chrome(options=options)
        wd.implicitly_wait(10)
        #  使用 Hytest 的全局变量 GSTORE，把浏览器实例 wd 存进去，方便其他函数拿来用
        GSTORE['wd'] = wd

    def login(self, username, password='888888'):
        wd = GSTORE['wd']
        wd.get(g_ui_url_teacher)
        wd.find_element(By.ID, 'username').send_keys(username)
        wd.find_element(By.ID, 'password').send_keys(password)
        # 点击登录
        (wd.find_element(By.ID, 'submit')).click()



t_ui = TeacherUI()
