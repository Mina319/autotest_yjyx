from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId, g_ui_url_teacher
from lib.api.Teacher import teacher
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class student:
    name = '老师登出2_TC_LOGINLOGOUT_102'

    def teststeps(self):
        STEP(1, '老师A登录web系统并退出')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        teacher_ui.logout()
        mes = teacher_ui.wd.find_element(By.XPATH, '//*[@id="teacher-page"]/h2').text
        INFO(f'mes：{mes}')
        CHECK_POINT('检查是否登出成功，登录页面', mes == '老师登录')
        STEP(2, '老师B登录web系统并退出')
        teacher_ui.login(username='tangsen')
        teacher_ui.logout()

        mes = teacher_ui.wd.find_element(By.XPATH, '//*[@id="teacher-page"]/h2').text
        teacher_ui.wd.close()
        INFO(f'mes：{mes}')
        CHECK_POINT('检查是否登出成功，登录页面', mes == '老师登录')

