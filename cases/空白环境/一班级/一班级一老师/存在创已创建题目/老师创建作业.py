from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_HOMEWORK_051:
    name = '创建作业51_TC_HOMEWORK_051'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='')
        teacher_ui.wd.quit()


class TC_HOMEWORK_052:
    name = '创建作业52_TC_HOMEWORK_052'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname=None)
        teacher_ui.wd.quit()


class TC_HOMEWORK_053:
    name = '创建作业53_TC_HOMEWORK_053'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='z', mes='作业名称长度应为2~105个字符')

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('z')
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()

