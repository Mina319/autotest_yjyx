
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass, sclass


class TC_HOME_112:
    name = '学生首页信息12_TC_HOME_112'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        sleep(0.5)
        STEP(2, '更改为不存在的班级')
        mes = student_ui.change_class(newclass='123456')
        student_ui.wd.quit()
        CHECK_POINT('检查首页信息', mes == '错误 : 您输入的班级邀请码不存在')


class TC_HOME_113:
    name = '学生首页信息13_TC_HOME_113'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        sleep(0.5)
        STEP(2, '更改为存在的班级')
        r = sclass.list_class()
        invitecode = r.json()['retlist'][1]['invitecode']
        mes = student_ui.change_class(newclass=invitecode)
        student_ui.wd.quit()
        CHECK_POINT('检查首页信息', mes == '修改班级成功')
