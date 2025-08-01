from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_0xxx:

    ddt_cases = [
        {
            'name': '老师登录5_TC_LOGINLOGOUT_005',
            'para': ['', '88888888', '请输入用户名']
        },
        {
            'name': '老师登录6_TC_LOGINLOGOUT_006',
            'para': ['zhangming', '', '请输入密码']
        },
        {
            'name': '老师登录7_TC_LOGINLOGOUT_007',
            'para': ['', '', '请输入密码']
        },
        {
            'name': '老师登录8_TC_LOGINLOGOUT_008',
            'para': ['zhangmin', '888888', '登录失败 : 用户或者密码错误']
        },
        {
            'name': '老师登录9_TC_LOGINLOGOUT_009',
            'para': ['zhangming', '88888', '登录失败 : 用户或者密码错误']
        },
        {
            'name': '老师登录10_TC_LOGINLOGOUT_010',
            'para': ['zhangmin', '8888888', '登录失败 : 用户或者密码错误']
        }
    ]

    def teststeps(self):
        # 取出参数
        username, password, info = self.para
        STEP(1, '老师登录')
        teacher_ui.open_browser()
        wd = teacher_ui.wd
        teacher_ui.login(username=username, password=password)
        sleep(0.2)
        mes = wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        INFO(f'mes:{mes}')
        wd.quit()
        CHECK_POINT('提示框消息是否正确', mes == info)

