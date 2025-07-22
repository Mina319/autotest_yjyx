from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_302:
    name = '学生登出2_TC_LOGINLOGOUT_302'

    def teststeps(self):
        STEP(1, '学生A登录web系统并退出')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        student_ui.logout()
        mes = student_ui.wd.find_element(By.XPATH, '//*[@id="page-container"]/h1').text
        INFO(f'mes：{mes}')
        CHECK_POINT('检查是否登出成功，登录页面', mes == '学生登录')
        STEP(2, '学生B登录web系统并退出')
        student_ui.login(username='hongyu')
        student_ui.logout()
        mes = student_ui.wd.find_element(By.XPATH, '//*[@id="page-container"]/h1').text
        student_ui.wd.close()
        INFO(f'mes：{mes}')
        CHECK_POINT('检查是否登出成功，登录页面', mes == '学生登录')
