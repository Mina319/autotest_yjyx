from datetime import datetime, timedelta
from time import sleep

from lib.ui.StudnetUI import student_ui
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *

# 任务编号
taskid = None
# 作业完成结果： username: (acc, complete_time)
res = {}


def suite_setup():
    # 存在 已发布作业
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    global taskid
    # 将任务全部发给所有 学生
    for i in range(3):
        taskid = teacher_ui.publish_process(taskname=f'哈哈{i+1}', taskdec=f'作业{i+1}'+'哈'*8,
                                        mes1='作业已发布给学生', checkall=True)
    teacher_ui.wd.quit()


class TC_HOMEWORK_251:
    name = '老师查询作业1_TC_HOMEWORK_251'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.query_homework(revokenum=1)
        STEP(2, '检查主页发布作业数量')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos(home=True)
        CHECK_POINT('检查已发布作业数量', homework == res1)

    def teardown(self):
        # 把撤销的作业重新发布
        # 将任务全部发给所有 学生
        teacher_ui.publish_process(taskname=f'哈哈3', taskdec=f'作业3' + '哈' * 8,
                                                mes1='作业已发布给学生', checkall=True)
        teacher_ui.wd.quit()


class TC_HOMEWORK_252:
    name = '老师查询作业2_TC_HOMEWORK_252'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.query_homework(revokenum=2)
        STEP(2, '检查主页发布作业数量')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos(home=True)
        CHECK_POINT('检查已发布作业数量', homework == res1)

    def teardown(self):
        # 把撤销的作业重新发布
        # 将任务全部发给所有 学生
        for i in range(1, 3):
            teacher_ui.publish_process(taskname=f'哈哈{i + 1}', taskdec=f'作业{i + 1}' + '哈' * 8,
                                                mes1='作业已发布给学生', checkall=True)
        teacher_ui.wd.quit()


class TC_HOMEWORK_253:
    name = '老师查询作业3_TC_HOMEWORK_253'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.query_homework(revokenum=3)
        STEP(2, '检查主页发布作业数量')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos(home=True)
        CHECK_POINT('检查已发布作业数量', homework == res1)

    def teardown(self):
        for i in range(3):
            teacher_ui.publish_process(taskname=f'哈哈{i+1}', taskdec=f'作业{i+1}'+'哈'*8,
                                            mes1='作业已发布给学生', checkall=True)
        teacher_ui.wd.quit()


class TC_HOMEWORK_254:
    name = '老师查询作业4_TC_HOMEWORK_254'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        time1 = datetime.today().strftime('%Y-%m-%d')
        res1 = teacher_ui.query_homework1(starttime=time1)
        teacher_ui.wd.quit()
        CHECK_POINT('检查已发布作业数量', res1 == 3)


class TC_HOMEWORK_255:
    name = '老师查询作业5_TC_HOMEWORK_255'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        time1 = datetime.today().strftime('%Y-%m-%d')
        res1 = teacher_ui.query_homework1(endtime=time1)
        teacher_ui.wd.quit()
        CHECK_POINT('检查已发布作业数量', res1 == 3)


class TC_HOMEWORK_256:
    name = '老师查询作业6_TC_HOMEWORK_256'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        time1 = datetime.today().strftime('%Y-%m-%d')
        # 获取明天的日期
        time2 = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        res1 = teacher_ui.query_homework1(starttime=time1, endtime=time2)
        teacher_ui.wd.quit()
        CHECK_POINT('检查已发布作业数量', res1 == 3)


class TC_HOMEWORK_301:
    name = '老师修改作业1_TC_HOMEWORK_301'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第2题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=2, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功', res)


class TC_HOMEWORK_302:
    name = '老师修改作业2_TC_HOMEWORK_302'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第3题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=3, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功', res)


class TC_HOMEWORK_303:
    name = '老师修改作业3_TC_HOMEWORK_303'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第4题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=4, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功', res)


class TC_HOMEWORK_304:
    name = '老师修改作业4_TC_HOMEWORK_304'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第5题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=5, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功', res)


class TC_HOMEWORK_305:
    name = '老师修改作业5_TC_HOMEWORK_305'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第6题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=6, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功', res)


class TC_HOMEWORK_306:
    name = '老师修改作业6_TC_HOMEWORK_306'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第2题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=2, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)


class TC_HOMEWORK_307:
    name = '老师修改作业7_TC_HOMEWORK_307'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第3题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=3, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)



class TC_HOMEWORK_308:
    name = '老师修改作业8_TC_HOMEWORK_308'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第4题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=4, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)


class TC_HOMEWORK_309:
    name = '老师修改作业9_TC_HOMEWORK_309'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第5题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=5, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)


class TC_HOMEWORK_310:
    name = '老师修改作业10_TC_HOMEWORK_310'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第6题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=6, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)


class TC_HOMEWORK_311:
    name = '老师修改作业11_TC_HOMEWORK_311'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第1题上移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=1, move='up')
        teacher_ui.wd.quit()
        CHECK_POINT('检验上移是否成功:', res)



class TC_HOMEWORK_312:
    name = '老师修改作业13_TC_HOMEWORK_312'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'将任务名为“哈哈1”的第10题下移')
        res = teacher_ui.edit_homework(taskname='哈哈1', idx=10, move='down')
        teacher_ui.wd.quit()
        CHECK_POINT('检验下移是否成功', res)


class TC_HOMEWORK_351:
    name = '老师修改描述1_TC_HOMEWORK_351'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：点进去修改，实际并未修改')
        teacher_ui.edit_taskdec(taskname='哈哈1')
        teacher_ui.wd.quit()


class TC_HOMEWORK_352:
    name = '老师修改描述2_TC_HOMEWORK_352'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', dec='哈哈1作业')
        teacher_ui.wd.quit()


class TC_HOMEWORK_353:
    name = '老师修改描述3_TC_HOMEWORK_353'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', time1=60)
        teacher_ui.wd.quit()


class TC_HOMEWORK_354:
    name = '老师修改描述4_TC_HOMEWORK_354'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', dec='哈哈1作业', time1=60)
        teacher_ui.wd.quit()


class TC_HOMEWORK_401:
    name = '老师撤销作业1_TC_HOMEWORK_401'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        len1 = teacher_ui.revoke_homework(taskname='哈哈2')
        teacher_ui.wd.quit()
        CHECK_POINT('检查是否撤销', len1 == 2)


class TC_HOMEWORK_403:
    name = '老师撤销作业3_TC_HOMEWORK_403'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        len1 = None
        for i in range(3):
            len1 = teacher_ui.revoke_homework(taskname=f'哈哈{i+1}')
        teacher_ui.wd.quit()
        CHECK_POINT('检查是否撤销', len1 == 0)


class TC_HOMEWORK_552:
    name = '删除作业2_TC_HOMEWORK_552'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'删除作业')
        teacher_ui.opt_homework('已创建作业')
        msg = teacher_ui.del_homework_by_taskname(taskname='哈哈1')
        teacher_ui.wd.quit()
        CHECK_POINT('检查是否没有删除成功', not msg)

