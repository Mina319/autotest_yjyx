from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_HOMEWORK_451:
    name = '查询已创建作业1_TC_HOMEWORK_451'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '查询已创建作业')
        len1 = teacher_ui.query_created_homework()
        CHECK_POINT('核实已创建作业数量', len1 == 3)


class TC_HOMEWORK_452:
    name = '查询已创建作业2_TC_HOMEWORK_452'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '查询已创建作业，搜索1')
        len1 = teacher_ui.query_created_homework1('1')
        CHECK_POINT('核实已创建作业数量', len1 == 1)


class TC_HOMEWORK_453:
    name = '查询已创建作业3_TC_HOMEWORK_453'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '查询已创建作业，搜索哈哈')
        len1 = teacher_ui.query_created_homework1('哈哈')
        CHECK_POINT('核实已创建作业数量', len1 == 3)
