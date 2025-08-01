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
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '添加题目成功')

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


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
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '添加题目成功')

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=1, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


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
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '题目内容不能为空')


class TC_QUESTION_004:
    name = '创建题目4_TC_QUESTION_004'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, answer=[100, [None]], content=self.content)
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')


class TC_QUESTION_005:
    name = '创建题目5_TC_QUESTION_005'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        self.content = '哈哈'
        res = teacher_ui.create_questions(type=0, answer=[-1, [1]], content=self.content)
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')


class TC_QUESTION_006:
    name = '创建题目6_TC_QUESTION_006'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[1.5, [0]], content='哈哈')
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '选择题最多提供10个选项')

    def teardown(self):
        # 删除题目
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res = teacher_ui.mul_questions(type=0, content='哈哈', opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_007:
    name = '创建题目7_TC_QUESTION_007'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        res = teacher_ui.create_questions(type=0, answer=[2, [None]], content='哈哈')
        sleep(0.5)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '题目答案不能为空')


class TC_QUESTION_008:
    name = '创建题目8_TC_QUESTION_008'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        content = '老师登录web系统老师登录web系统' * 100
        res = teacher_ui.create_questions(type=0, answer=[2, [None]], content=content)
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '题目内容过长')


class TC_QUESTION_011:
    name = '创建题目11_TC_QUESTION_011'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[1, 1])
        res = teacher_ui.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '人教版 已经存在了')


class TC_QUESTION_012:
    name = '创建题目12_TC_QUESTION_012'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[0, 0])
        res = teacher_ui.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('提示消息', res == '浙教版 已经存在了')


class TC_QUESTION_013:
    name = '创建题目13_TC_QUESTION_013'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建题目')
        teacher_ui.check_textbook(type=1, difflevel=2, textbook=[0, 1])
        num, num1 = teacher_ui.del_textbook([0, 1])
        sleep(0.2)
        teacher_ui.wd.quit()
        CHECK_POINT('检查是否成功删除', num1 == num - 2)


class TC_QUESTION_014:
    name = '创建题目14_TC_QUESTION_014'

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
        type, diff, content, ans, video, textbook = teacher_ui.mul_questions(type=1, content=self.content, opt=1)
        sleep(0.2)
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


class TC_QUESTION_020:
    name = '创建题目20_TC_QUESTION_020'

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
        # 需要添加视频上传检查
        sleep(0.2)
        teacher_ui.wd.quit()
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


class TC_QUESTION_021:
    name = '创建题目21_TC_QUESTION_021'

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
        CHECK_POINT('检查信息', type == '选择题' and diff == '简单' and content == self.content
                    and ans == ['A', 'C', 'D'])

    def teardown(self):
        # 删除题目
        res = teacher_ui.mul_questions(type=0, content=self.content, opt=3)
        INFO(f'删除题目是否成功：{res}')
        teacher_ui.wd.quit()


class TC_QUESTION_022:
    name = '创建题目22_TC_QUESTION_022'

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
        INFO(f'num:{num}')
        CHECK_POINT('检查信息', num == 5)

    def teardown(self):
        # 删除题目
        teacher_ui.del_all_questions()
        teacher_ui.wd.quit()


class TC_QUESTION_023:
    name = '创建题目23_TC_QUESTION_023'

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
