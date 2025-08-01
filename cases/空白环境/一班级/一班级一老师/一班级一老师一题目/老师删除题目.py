from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_QUESTION_201:
    name = '删除题目1_TC_QUESTION_201'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '删除题目')
        self.content = '哈哈' * 10
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        CHECK_POINT('是否删除成功', res)

    def teardown(self):
        # 增加回来
        res = teacher_ui.create_questions(type=0, content=self.content, answer=[4, [0]], opt=2)
        INFO(f'创建题目是否成功：{res}')
        teacher_ui.wd.quit()




