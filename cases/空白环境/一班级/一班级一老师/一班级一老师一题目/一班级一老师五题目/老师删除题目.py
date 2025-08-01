from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_QUESTION_202:
    name = '删除题目2_TC_QUESTION_202'
    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '删除题目')
        for i in range(5):
            res = teacher_ui.mul_questions(type=0, content=f'哈哈{i}', opt=3)
            CHECK_POINT('是否删除成功', res)

    def teardown(self):
        # 增加回来
        for i in range(5):
            res = teacher_ui.create_questions(type=0, content=f'哈哈{i}', answer=[5, [0, 2, 3]], opt=2)
            INFO(f'创建题目是否成功：{res}')


