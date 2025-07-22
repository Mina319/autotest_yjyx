from time import sleep

from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_001:
    name = '老师登录1_TC_LOGINLOGOUT_001'

    def teststeps(self):
        STEP(1, '老师登录')
        teacher_ui.open_browser()
        wd = teacher_ui.wd
        teacher_ui.login(username='sunny12', password='12sd8ndfd')
        sleep(0.2)
        mes = wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        wd.close()
        CHECK_POINT('提示框消息', mes == '登录失败 : 用户或者密码错误')




