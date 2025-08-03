from time import sleep
from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *

taskid = None


def suite_setup():
    # 存在 已发布作业
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    STEP(2, '发布作业')
    global taskid
    taskid = teacher_ui.publish_process(taskname='哈哈1', taskdec='作业' + '哈' * 8, mes1='作业已发布给学生', checkall=True)
    teacher_ui.wd.quit()


class TC_HOMEWORK_151:
    name = '学生完成作业1_TC_HOMEWORK_151'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        acc, b, e, complete_time, time, mes1 = student_ui.do_homework(taskid=taskid, num=1)
        CHECK_POINT('检查', mes1 == '尚未做完，确定提交吗？')
        sleep(0.5)


# class TC_HOMEWORK_152:
#     name = '学生完成作业2_TC_HOMEWORK_152'
#
#     def teststeps(self):
#         STEP(1, '学生登录web系统')
#         student_ui.open_browser()
#         student_ui.login(username='qinsang')
#         student_ui.do_homework(taskid=taskid, mes='超时，自动提交', sleeptime=31)


class TC_HOMEWORK_153:
    name = '学生完成作业3_TC_HOMEWORK_153'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='wukong')
        acc, b, e, complete_time, time, mes1 = student_ui.do_homework(taskid=taskid, num=10)
        CHECK_POINT('检查', mes1 == '提交后，将不能再修改，确定提交吗?')


class TC_HOMEWORK_154:
    name = '学生完成作业4_TC_HOMEWORK_154'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='wuneng')
        acc, b, e, complete_time, time, mes1 = student_ui.do_homework(taskid=taskid, num=1)
        CHECK_POINT('检查', mes1 == '尚未做完，确定提交吗？')

