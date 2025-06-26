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

    def do_homework(self):
        # 做作业
        self.wd.switch_to.window(self.wd.window_handles[-1])
        # 点击 消息
        self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown > a > i.fa-tasks').click()
        # 点击 查看所有任务
        self.wd.find_element(By.CSS_SELECTOR, 'li.last').click()

        # 点击 去做
        self.wd.find_element(By.CSS_SELECTOR, 'table.table td:last-child > button').click()
        # 默认全都点击 C
        c_eles = self.wd.find_elements(By.XPATH, '//div//button[3]')
        for e in c_eles:
            e.click()
        # 点击 提交
        self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[3]/button').click()
        # 点击 确定
        self.wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-footer-buttons > button:last-child').click()
        # 执行 JavaScript 来点击页面的某个位置
        self.wd.execute_script("document.elementFromPoint(100, 100).click();")
        # 获取信息：正确率
        acc_element = self.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[1]/div[2]/span[2]')
        acc_text = acc_element.text
        acc = float(acc_text[4:-1].strip()) / 100
        self.wd.close()
        return acc


s_ui = StudentUI()
