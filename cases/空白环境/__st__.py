from lib.api.SClass import sclass
from lib.api.Student import student
from lib.api.Teacher import teacher


def suite_setup():
    # 删除所有班级、学生、老师
    student.del_allstudents()
    teacher.del_allteachers()
    sclass.del_allclasses()

