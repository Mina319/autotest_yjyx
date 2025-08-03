from cfg.cfg import gradeToId, subjectToId
from lib.api.SClass import getFirstClass
from lib.ui.TeacherUI import teacher_ui
from lib.api.Teacher import teacher
from lib.webui import *

parms = []
textbook = []

for jc in range(2):
    for nianji in range(6):
        for ce in range(2):
            textbook.append([jc, nianji, ce])

INFO(f'textbook: {textbook}')


def suite_setup():
    # 创建一题目
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    m = 0
    for i in range(2):
        # type： 0 选择题， 1 填空题
        for j in range(3):
        # difflevel：0 简单， 1 中等， 2 难
            for t in range(len(textbook)):
                if i == 0:
                    answer = [5, [0, 2, 3]]
                else:
                    answer = [5, [str(i) for i in range(1, 6)]]
                c = f'哈哈{m}'
                m += 1
                p = [i, c, answer]
                INFO(f'p: {p}')
                parms.append(p)
                res = teacher_ui.create_questions(type=i, difflevel=j, textbook=[textbook[t]], content=c, answer=answer, opt=2)
                INFO(f'创建题目是否成功：{res}')
    teacher_ui.wd.quit()


# 套件清除，只执行一次
def suite_teardown():
    # 删除题目
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    teacher_ui.del_all_questions(flag=True, type=0)
    teacher_ui.del_all_questions(flag=True, type=1)
    teacher_ui.wd.quit()
