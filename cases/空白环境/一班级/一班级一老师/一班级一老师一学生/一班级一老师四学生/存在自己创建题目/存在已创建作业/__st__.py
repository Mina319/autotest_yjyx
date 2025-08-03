from hytest import STEP

from lib.ui.TeacherUI import teacher_ui


def suite_setup():
    # 存在 已创建作业
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    STEP(2, '创建作业')
    for i in range(3):
        teacher_ui.publish_homework(taskname=f'哈哈{i+1}', mes='新建作业成功', num=10)

    teacher_ui.publish_homework(taskname='哈' * 10, mes='新建作业成功', num=10)

    teacher_ui.wd.quit()


def suite_teardown():
    # 删除 已创建作业
    teacher_ui.open_browser()
    teacher_ui.login(username='zhangming')
    teacher_ui.opt_homework('已创建作业')
    for i in range(3):
        res = teacher_ui.del_homework_by_taskname(f'哈哈{i+1}')
        print(f'是否删除作业{res}')
    res = teacher_ui.del_homework_by_taskname('哈' * 10)
    print(f'是否删除作业{res}')
    teacher_ui.wd.quit()
