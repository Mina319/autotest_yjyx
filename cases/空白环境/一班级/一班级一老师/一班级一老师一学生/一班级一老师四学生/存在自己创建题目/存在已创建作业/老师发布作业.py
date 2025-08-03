from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_HOMEWORK_101:
    name = '发布作业1_TC_HOMEWORK_101'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='作业'+'哈'*8, mes1='您还没有选择接收任务的学生！')

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_102:
    name = '发布作业2_TC_HOMEWORK_102'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        mes = teacher_ui.publish_process(taskname='哈哈1', taskdec='作业'+'哈'*8, mes1='', time=-1, checkall=True)
        teacher_ui.wd.quit()
        CHECK_POINT('检查:', mes == '建议完成时间错误！')

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        teacher_ui.revoke_homework('哈哈1')
        teacher_ui.wd.quit()


class TC_HOMEWORK_103:
    name = '发布作业3_TC_HOMEWORK_103'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='作业'+'哈'*8, mes1='', time=0, num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_104:
    name = '发布作业4_TC_HOMEWORK_104'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        mes = teacher_ui.publish_process(taskname='哈哈2', taskdec='作业'+'哈'*8, mes1='建议完成时间错误', time='ss', num=1)
        CHECK_POINT('检查:', mes == '建议完成时间错误！')

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈哈2')
        teacher_ui.wd.quit()


class TC_HOMEWORK_105:
    name = '发布作业5_TC_HOMEWORK_105'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='作业'+'哈'*8, mes1='作业已发布给学生', time=90, num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_106:
    name = '发布作业6_TC_HOMEWORK_106'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='作业'+'哈'*8, mes1='作业已发布给学生', time=999, num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_107:
    name = '发布作业7_TC_HOMEWORK_107'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='作业'+'哈'*8, mes1='作业已发布给学生', time=90, num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_111:
    name = '发布作业11_TC_HOMEWORK_111'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='哈'*20, mes1='作业已发布给学生', num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_112:
    name = '发布作业12_TC_HOMEWORK_112'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='', mes1='作业已发布给学生', num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_113:
    name = '发布作业13_TC_HOMEWORK_113'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='哈', mes1='作业已发布给学生', num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_114:
    name = '发布作业14_TC_HOMEWORK_114'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec=generate_mixed_string(), mes1='作业已发布给学生', num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_115:
    name = '发布作业15_TC_HOMEWORK_115'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='@#$%^&*()!', mes1='作业已发布给学生', num=1)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_116:
    name = '发布作业16_TC_HOMEWORK_116'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10, taskdec='哈哈'*14+'作业', mes1='作业已发布给学生', num=1, time=40)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()


class TC_HOMEWORK_117:
    name = '发布作业17_TC_HOMEWORK_117'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '发布作业')
        teacher_ui.publish_process(taskname='哈'*10000, taskdec='哈哈'*14+'作业', mes1='作业已发布给学生', num=1, time=40)

    def teardown(self):
        # 撤销 已发布作业
        teacher_ui.revoke_homework('哈'*10)
        teacher_ui.wd.quit()

