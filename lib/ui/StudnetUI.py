from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep


class StudentUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.wd = webdriver.Chrome(options=options)  # 保存为 self.wd
        self.wd.implicitly_wait(10)

    def login(self, username, password='888888'):
        self.wd.get(g_ui_url_student)
        self.wd.find_element(By.ID, 'username').send_keys(username)
        self.wd.find_element(By.ID, 'password').send_keys(password)
        self.wd.find_element(By.ID, 'submit').click()


s_ui = StudentUI()
