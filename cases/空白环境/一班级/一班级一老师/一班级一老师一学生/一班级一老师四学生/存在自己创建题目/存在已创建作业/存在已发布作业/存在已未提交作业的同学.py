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
    taskid = teacher_ui.publish_process(taskname='哈哈1', taskdec='作业' + '哈' * 8,
                                        mes1='作业已发布给学生', checkall=True)
    teacher_ui.publish_process(taskname='哈哈2', taskdec='作业' + '哈' * 8,
                               mes1='作业已发布给学生', checkall=True)
    teacher_ui.publish_process(taskname='哈哈3', taskdec='作业' + '哈' * 8,
                               mes1='作业已发布给学生', checkall=True)
    teacher_ui.wd.quit()

    # 学生1 做作业
    student_ui.open_browser()
    student_ui.login(username='qinsang')
    acc, b, e, complete_time, time, mes = student_ui.do_homework(taskid=taskid)
    res['秦桑'] = complete_time, f'正确率 {int(acc*100)} % : 对 {b} 题， 错 {e} 题'


    # 学生2 做作业
    student_ui.login(username='wukong')
    acc, b, e, complete_time, time, mes = student_ui.do_homework(taskid=taskid)
    res['悟空'] = complete_time, f'正确率 {int(acc*100)} % : 对 {b} 题， 错 {e} 题'
    student_ui.wd.quit()


class TC_HOMEWORK_201:
    name = '老师查看结果1_TC_HOMEWORK_201'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1')
        STEP(2, '检查和实际完成情况是否一致')
        for name in res1.keys():
            if name in res:
                # 完成作业的同学
                ctime1, acc1 = res1[name]
                ctime, acc = res[name]
                INFO(f'acc1:{acc1},acc:{acc}')
                CHECK_POINT(f'{name}同学的正确率是否一致', acc1 == acc)
        teacher_ui.wd.quit()


class TC_HOMEWORK_202:
    name = '老师查看结果2_TC_HOMEWORK_202'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1')
        STEP(2, '检查和实际完成情况是否一致')
        for name in res1.keys():
            if name not in res:
                # 未完成作业的同学
                ctime1, acc1 = res1[name]
                CHECK_POINT(f'{name}同学的正确率是否一致', ctime1 == '尚未提交')
        teacher_ui.wd.quit()


class TC_HOMEWORK_203:
    name = '老师查看结果3_TC_HOMEWORK_203'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1', completed=True)
        STEP(2, '检查已完成同学 实际完成情况是否一致')
        for name in res1.keys():
            ctime1, acc1 = res1[name]
            ctime, acc = res[name]
            INFO(f'acc1:{acc1},acc:{acc}')
            CHECK_POINT(f'{name}同学的正确率是否一致', acc1 == acc)
        teacher_ui.wd.quit()


class TC_HOMEWORK_204:
    name = '老师查看结果4_TC_HOMEWORK_204'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1', notcompleted=True)
        STEP(2, '检查未完成同学 实际完成情况是否一致')
        for name in res1.keys():
            ctime1, acc1 = res1[name]
            CHECK_POINT(f'{name}同学状态', ctime1 == '尚未提交')
        teacher_ui.wd.quit()


class TC_HOMEWORK_205:
    name = '老师查看结果5_TC_HOMEWORK_205'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1', refresh=True)
        STEP(2, '检查未完成同学 实际完成情况是否一致')
        CHECK_POINT(f'检查同学人数：', len(res1) == 4)
        for name in res1.keys():
            ctime1, acc1 = res1[name]
            if name in res:
                # 完成作业的同学
                ctime, acc = res[name]
                INFO(f'acc1:{acc1},acc:{acc}')
                CHECK_POINT(f'{name}同学的正确率是否一致', acc1 == acc)
            else:
                CHECK_POINT(f'{name}同学暂未提交', ctime1 == '尚未提交')
        teacher_ui.wd.quit()


class TC_HOMEWORK_206:
    name = '老师查看结果6_TC_HOMEWORK_206'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1', completed=True, refresh=True)
        STEP(2, '检查完成同学 实际完成情况是否一致')
        CHECK_POINT(f'检查同学人数：', len(res1) == 2)
        for name in res1.keys():
            ctime1, acc1 = res1[name]
            ctime, acc = res[name]
            # 完成作业的同学
            INFO(f'acc1:{acc1},acc:{acc}')
            CHECK_POINT(f'{name}同学的正确率是否一致', acc1 == acc)
        teacher_ui.wd.quit()


class TC_HOMEWORK_207:
    name = '老师查看结果7_TC_HOMEWORK_207'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        res1 = teacher_ui.view_result(taskname='哈哈1', notcompleted=True, refresh=True)
        STEP(2, '检查未完成同学 实际完成情况是否一致')
        INFO(f'未完成同学个数：{len(res1)}')
        CHECK_POINT(f'检查同学人数：', len(res1) == 2)
        for name in res1.keys():
            ctime1, acc1 = res1[name]
            CHECK_POINT(f'{name}同学暂未提交', ctime1 == '尚未提交' and (name not in res))
        teacher_ui.wd.quit()


class TC_HOMEWORK_355:
    name = '老师修改描述5_TC_HOMEWORK_355'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：点进去修改，实际并未修改')
        teacher_ui.edit_taskdec(taskname='哈哈1')
        teacher_ui.wd.quit()


class TC_HOMEWORK_356:
    name = '老师修改描述6_TC_HOMEWORK_356'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', dec='哈哈1作业')
        teacher_ui.wd.quit()


class TC_HOMEWORK_357:
    name = '老师修改描述7_TC_HOMEWORK_357'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', time1=60)
        teacher_ui.wd.quit()


class TC_HOMEWORK_358:
    name = '老师修改描述8_TC_HOMEWORK_358'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        teacher_ui.edit_taskdec(taskname='哈哈1', dec='哈哈1作业', time1=60)
        teacher_ui.wd.quit()


class TC_HOMEWORK_402:
    name = '老师撤销作业2_TC_HOMEWORK_402'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'修改任务描述：仅修改描述')
        msg = teacher_ui.revoke_homework(taskname='哈哈1')
        CHECK_POINT('检查是否撤销', msg == '错误 : 该任务已经有学生做了，不能再撤销')
        teacher_ui.wd.quit()


class TC_HOMEWORK_551:
    name = '删除作业1_TC_HOMEWORK_551'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, f'删除作业')
        teacher_ui.opt_homework('已创建作业')
        msg = teacher_ui.del_homework_by_taskname1(taskname='哈哈1')
        CHECK_POINT('检查是否没有删除成功', msg == '删除失败:该试卷/作业已经发布在任务中，不能删除！！')
        teacher_ui.wd.quit()


