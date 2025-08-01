from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Teacher import teacher
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_001:
    name = '老师首页信息1_TC_HOME_001'

    def teststeps(self):
        STEP(1, '创建老师')
        subject = '初中数学'
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
            'zhangming', '张明', subjectToId[subject], [{"id": getFirstClass()['id']}], '13451813456', \
            'zhangming@163.com', '3209251983090987799'
        r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                            classlist=classlist, phonenumber=phonenumber, email=email,
                            idcardnumber=idcardnumber)
        self.tid = r.json()["id"]
        CHECK_POINT('是否创建老师成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username=username)
        INFO('检查 学校、姓名、学科、金币、已发布微课、已发布作业 的信息是否正确')
        wd = teacher_ui.wd
        # 获取主页信息
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('检查信息是否正确', name1 == realname and subject1 == subject and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school)

        STEP(3, '查看顶部菜单')
        menus = teacher_ui.get_menus()
        wd.quit()
        CHECK_POINT('顶部菜单是否一致', menus == ['主页', '微课', '作业', '题目', '班级情况'])

    def teardown(self):
        # 删掉老师
        teacher.del_teacher(self.tid)
