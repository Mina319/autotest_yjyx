from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_QUESTION_102:
    name = '修改题目2_TC_QUESTION_102'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '编辑题目')
        self.content = '哈哈' * 10
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        self.content1 = r"嘻嘻嘻"
        res = teacher_ui.edit_question1(difflevel=1, content=self.content1)
        CHECK_POINT('提示消息', res == '编辑题目成功')

    def teardown(self):
        # 修改题目修改回来
        teacher_ui.mul_questions(type=0, content=self.content1, opt=2)
        teacher_ui.edit_question1(difflevel=0, content=self.content)
        teacher_ui.wd.quit()


class TC_QUESTION_103:
    name = '修改题目3_TC_QUESTION_103'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '编辑题目')
        self.content = '哈哈' * 10
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        self.content1 = r"嘻嘻嘻"
        res = teacher_ui.edit_question1(answer=[5, [1, 2]], content=self.content1)
        CHECK_POINT('提示消息', res == '编辑题目成功')

    def teardown(self):
        # 修改题目修改回来
        teacher_ui.mul_questions(type=0, content=self.content1, opt=2)
        teacher_ui.edit_question1(answer=[4, [0]], content=self.content)
        teacher_ui.wd.quit()


class TC_QUESTION_105:
    name = '修改题目5_TC_QUESTION_105'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '编辑题目')
        self.content = '哈哈' * 10
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        res = teacher_ui.edit_question1(answer=[5, [1, 2]])
        CHECK_POINT('提示消息', res == '编辑题目成功')

    def teardown(self):
        # 修改题目修改回来
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        teacher_ui.edit_question1(answer=[4, [0]])
        teacher_ui.wd.quit()


class TC_QUESTION_106:
    name = '修改题目6_TC_QUESTION_106'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        STEP(3, '编辑题目')
        self.content = '哈哈' * 10
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        res = teacher_ui.edit_question1(desc='撒过的痕迹啊考试大纲')
        CHECK_POINT('提示消息', res == '编辑题目成功')

    def teardown(self):
        # 修改题目修改回来
        teacher_ui.mul_questions(type=0, content=self.content, opt=2)
        teacher_ui.edit_question1(desc='')
        teacher_ui.wd.quit()
