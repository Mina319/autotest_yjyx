from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_QUESTION_024:
    name = '创建题目24_TC_QUESTION_024'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, content=self.content, answer=[4, [0]])
        CHECK_POINT('提示消息', res == '添加题目成功')
        teacher_ui.wd.quit()

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_025:
    name = '创建题目25_TC_QUESTION_025'

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
        teacher_ui.wd.quit()

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=1, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_026:
    name = '创建题目26_TC_QUESTION_026'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=1, difflevel=1, knowleadege=4,
                                          textbook=[[0, 1, 1], [1, 0, 1]],
                                          content=None, answer=[4, ['1', '2', '3', '4']])
        CHECK_POINT('提示消息', res == '题目内容不能为空')
        teacher_ui.wd.quit()


class TC_QUESTION_027:
    name = '创建题目27_TC_QUESTION_027'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, answer=[100, [None]])
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')
        teacher_ui.wd.quit()


class TC_QUESTION_028:
    name = '创建题目28_TC_QUESTION_028'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[-1, [1]])
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')
        teacher_ui.wd.quit()


class TC_QUESTION_029:
    name = '创建题目29_TC_QUESTION_029'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[1.5, [0]], content='哈哈')
        sleep(0.4)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, content='哈哈', opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_030:
    name = '创建题目30_TC_QUESTION_030'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[2, [None]])
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '题目答案不能为空')


class TC_QUESTION_031:
    name = '创建题目31_TC_QUESTION_031'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        content = '老师登录web系统老师登录web系统' * 100
        res = teacher_ui.create_questions(type=0, answer=[2, [None]], content=content)
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '题目内容过长')


class TC_QUESTION_032:
    name = '创建题目32_TC_QUESTION_032'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[1, 1])
        res = teacher_ui.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '人教版 已经存在了')


class TC_QUESTION_033:
    name = '创建题目33_TC_QUESTION_033'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[0, 0])
        res = teacher_ui.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '浙教版 已经存在了')


class TC_QUESTION_034:
    name = '创建题目34_TC_QUESTION_034'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[0, 1])
        num, num1 = teacher_ui.del_textbook([0, 1])
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('检查是否成功删除', num1 == num - 2)


class TC_QUESTION_035:
    name = '创建题目35_TC_QUESTION_035'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=1, answer=[3, ['1', '2', '3']], content=self.content, textbook=14)
        CHECK_POINT('提示消息', res == '添加题目成功')
        STEP(3, '检查创建后信息')
        # 查看刚刚创建的题目
        type,diff,content,ans,video,textbook = teacher_ui.mul_questions(type=1, opt=1, content=self.content)
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('检查信息', type == '填空题' and diff == '简单' and content == self.content
                    and ans == ['1', '2', '3'] and textbook == [['七年级', '', '']])

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, opt=3, content=self.content)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_036:
    name = '创建题目36_TC_QUESTION_036'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=1, difflevel=1, knowleadege=3,
                                          answer=[4, ['1', '2', '3', '987gs^&']],
                                          content=self.content, textbook=[[0, 0, 0], [1, 1, 0]],
                                          video=[r'C:\Users\Administrator\evVedios\wvct3-qp8r0.gif',
                                                 r'C:\Users\Administrator\evVedios\333.mp4'])
        CHECK_POINT('提示消息', res == '添加题目成功')
        STEP(3, '检查创建后信息')
        # 查看刚刚创建的题目
        type, diff, content, ans, video, textbook = teacher_ui.mul_questions(type=1, content=self.content, opt=1)
        sleep(0.5)
        teacher_ui.wd.quit()
        # 需要添加视频上传检查
        CHECK_POINT('检查信息', type == '填空题' and diff == '中等' and content == self.content
                    and ans == ['1', '2', '3', '987gs^&'] and textbook == [['七年级', '上册', ''],
                                                                           ['八年级', '上册', '']]
                    )

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=1, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_037:
    name = '创建题目37_TC_QUESTION_037'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈δΔ让we are one. 然后，还有什么呢?'
        res = teacher_ui.create_questions(type=0, difflevel=0,
                                          answer=[4, [0, 2, 3]],
                                          content=self.content)
        CHECK_POINT('提示消息', res == '添加题目成功')
        STEP(3, '检查创建后信息')
        # 查看刚刚创建的题目
        type, diff, content, ans, video, textbook = teacher_ui.mul_questions(type=0, content=self.content, opt=1)
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('检查信息', type == '选择题' and diff == '简单' and content == self.content
                    and ans == ['A', 'C', 'D'])

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_038:
    name = '创建题目38_TC_QUESTION_038'

    def setup(self):
        # 创建多个选择题
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        self.contens = [generate_mixed_string() for i in range(5)]
        for i, c in enumerate(self.contens):
            teacher_ui.create_questions(type=0, difflevel=1, content=c, answer=[4, [i % 4]])
            sleep(0.4)

    def teststeps(self):
        STEP(1, '查询')
        num = teacher_ui.mul_questions(type=0, opt=4)
        CHECK_POINT('检查信息', num == 5)

    def teardown(self):
        # 删除题目
        teacher_ui.del_all_questions()
        teacher_ui.wd.quit()


class TC_QUESTION_039:
    name = '创建题目39_TC_QUESTION_039'

    def teststeps(self):
        STEP(1, '登录并创建题目')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        self.content = '@#￥%……函数f(x) = 2x^2 - 3x + 1在x=2时的值。答案：将x=2代入函数f(x) = 2x^2 - 3x + 1，得到f(2)' \
                       ' = 2(2)^2 - 3(2) + 1 = 8 - 6 + 1 = 3。2. 题目：解方程3x - 5 = 2'
        teacher_ui.create_questions(type=0, difflevel=1, content=self.content, answer=[4, [2]])
        sleep(0.2)

        STEP(3, '检查创建后信息')
        # 查看刚刚创建的题目
        type, diff, content, ans, video, textbook = teacher_ui.mul_questions(type=0, content=self.content, opt=1)
        CHECK_POINT('检查信息', type == '选择题' and diff == '中等' and content == self.content
                    and ans == ['C'])

    def teardown(self):
        # 删除题目
        teacher_ui.del_all_questions()
        teacher_ui.wd.quit()
