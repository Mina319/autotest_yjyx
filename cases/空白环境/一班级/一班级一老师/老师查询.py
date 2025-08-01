from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOMEWORK_454:
    name = '查询已创建作业4_TC_HOMEWORK_454'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '查询已创建作业')
        len1 = teacher_ui.query_created_homework()
        CHECK_POINT('核实已创建作业数量', len1 == 0)
        teacher_ui.wd.quit()


