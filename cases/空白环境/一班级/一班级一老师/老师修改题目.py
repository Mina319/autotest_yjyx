from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_QUESTION_101:
    name = '修改题目1_TC_QUESTION_101'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, content=self.content, answer=[4, [0]], opt=2)
        CHECK_POINT('提示消息', res == '添加题目成功')
        STEP(3, '编辑题目')
        self.content = r"1. 函数\(y = \sin(2x + \frac{\pi}{3})\)的最小正周期是( ) A. \(\pi\) B. \(2\pi\)" \
                       r" C. \(\frac{\pi}{2}\) D. \(4\pi\) 2. 已知向量\(\vec{a}=(1,2)\),\(\\"
        res = teacher_ui.edit_question1(difflevel=1, content=self.content)
        CHECK_POINT('提示消息', res == '编辑题目成功')

    def teardown(self):
        # 删除题目
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()

