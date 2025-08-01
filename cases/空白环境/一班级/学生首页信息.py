from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_101:
    name = '学生首页信息1_TC_HOME_101'

    def teststeps(self):
        STEP(1, '创建学生')
        username, realname, grade, classid, phonenumber = 'qinsang', '秦桑', '高一', \
                                                          getFirstClass()["id"], '1894567233'
        gradeid = gradeToId[grade]
        r = student.add_student(username, realname, gradeid, classid, phonenumber)
        self.sid = r.json()["id"]
        CHECK_POINT('是否创建学生成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        student_ui.open_browser()
        student_ui.login(username=username)
        INFO('检查 学校、姓名、已发布微课、已发布作业 的信息是否正确')
        wd = student_ui.wd
        # 获取主页信息
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('检查信息是否正确', name1 == realname and microlessons == 0
                    and homework == 0 and school1 == g_school)

        STEP(3, '查看顶部菜单')
        menus = student_ui.get_menus()
        wd.quit()
        CHECK_POINT('顶部菜单是否一致', menus == ['主页', '亿教课堂', '我的任务', '错题库', '统计'])

    def teardown(self):
        # 删掉学生
        student.del_student(self.sid)
