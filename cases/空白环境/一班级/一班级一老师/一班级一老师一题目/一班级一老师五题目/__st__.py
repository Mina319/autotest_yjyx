from cfg.cfg import gradeToId, subjectToId
from lib.api.SClass import getFirstClass
from lib.ui.TeacherUI import teacher_ui
from lib.api.Teacher import teacher
from lib.webui import *

parms = []


def suite_setup():
    # 创建一题目
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    for i in range(5):
        c = f'哈哈{i}'
        answer = [5, [0, 2, 3]]
        p = [0, c, answer]
        parms.append(p)
        res = teacher_ui.create_questions(type=0, content=c, answer=answer, opt=2)
        INFO(f'创建题目是否成功：{res}')
    teacher_ui.wd.quit()


# 套件清除，只执行一次
def suite_teardown():
    # 删除题目
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    sleep(0.2)

    for i, p in enumerate(parms):
        t, c, answer = p
        res = teacher_ui.mul_questions(type=t, content=c, opt=3)
        INFO(f'删除题目是否成功：{res}')
    teacher_ui.wd.quit()
