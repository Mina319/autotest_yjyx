from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_QUESTION_001:
    name = '创建题目1_TC_QUESTION_001'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, content=self.content, answer=[4, [0]])
        CHECK_POINT('提示消息', res == '添加题目成功')
        teacher_ui.wd.close()

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.del_questions(type=0, content=self.content)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.close()


class TC_QUESTION_002:
    name = '创建题目2_TC_QUESTION_002'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=1, difflevel=1, knowleadege=3,
                                          textbook=[[0, 1, 1], [1, 0, 1]],
                                          content=self.content, answer=[4, ['1', '2', '3', '4']])
        CHECK_POINT('提示消息', res == '添加题目成功')
        teacher_ui.wd.close()

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.del_questions(type=1, content=self.content)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.close()


class TC_QUESTION_003:
    name = '创建题目3_TC_QUESTION_003'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=1, difflevel=1, knowleadege=4,
                                          textbook=[[0, 1, 1], [1, 0, 1]],
                                          content=None, answer=[4, ['1', '2', '3', '4']])
        CHECK_POINT('提示消息', res == '题目内容不能为空')
        teacher_ui.wd.close()


class TC_QUESTION_004:
    name = '创建题目4_TC_QUESTION_004'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, answer=[100, [None]])
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')
        teacher_ui.wd.close()


class TC_QUESTION_005:
    name = '创建题目5_TC_QUESTION_005'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[-1, [1]])
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')
        teacher_ui.wd.close()


class TC_QUESTION_006:
    name = '创建题目6_TC_QUESTION_006'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[1.5, [0]], content='哈哈')
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')
        teacher_ui.wd.close()

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.del_questions(type=0, content='哈哈')
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.close()

class TC_QUESTION_007:
    name = '创建题目7_TC_QUESTION_007'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[2, [None]])
        CHECK_POINT('提示消息', res == '题目答案不能为空')
        teacher_ui.wd.close()


class TC_QUESTION_008:
    name = '创建题目8_TC_QUESTION_008'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        content = '老师登录web系统老师登录web系统'*100
        res = teacher_ui.create_questions(type=0, answer=[2, [None]], content=content)
        CHECK_POINT('提示消息', res == '题目内容过长')
        teacher_ui.wd.close()




