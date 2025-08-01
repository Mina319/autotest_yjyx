from time import sleep

from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_203:
    name = '学生登录3_TC_LOGINLOGOUT_203'

    def teststeps(self):
        STEP(1, '创建学生')
        username, realname, grade, classid, phonenumber = 'yiliankan', '易连恺', '高一', \
                                                          getFirstClass()["id"], '1894567214'
        gradeid = gradeToId[grade]
        r = student.add_student(username, realname, gradeid, classid, phonenumber)
        self.sid = r.json()["id"]
        CHECK_POINT('是否创建学生成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        student_ui.open_browser()
        student_ui.login(username=username)
        STEP(3, '检查 学校、姓名、已发布微课、已发布作业 的信息是否正确')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        SELENIUM_LOG_SCREEN(student_ui.wd, width='70%')
        CHECK_POINT('检查信息是否正确', name1 == realname and microlessons == 0
                    and homework == 0 and school1 == g_school)
        STEP(4, '查看错题库')
        info = student_ui.click_wrong_answer_database()
        SELENIUM_LOG_SCREEN(student_ui.wd, width='70%')
        CHECK_POINT('检查错题库', info == '您尚未有错题入库哦')
        student_ui.wd.quit()

    def teardown(self):
        # 删掉同学
        student.del_student(self.sid)


class TC_LOGINLOGOUT_213:
    name = '学生登录13_TC_LOGINLOGOUT_213'

    def teststeps(self):
        STEP(1, '使用老师账号登录老师web系统')
        student_ui.open_browser()
        student_ui.login(username='zhangming')
        wd = student_ui.wd
        sleep(0.2)
        mes = wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        INFO(f'mes:{mes}')
        wd.quit()
        CHECK_POINT('提示框消息是否正确', mes == '登录失败 : 请使用学生账户登录')
