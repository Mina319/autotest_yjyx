from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_102:
    name = '学生首页信息2_TC_HOME_102'

    def teststeps(self):
        STEP(1, '使用学生A账号登录，查看首页信息')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        menus = student_ui.get_menus()
        CHECK_POINT('检查首页信息', name1 == '秦桑' and microlessons == 0
                    and homework == 0 and school1 == g_school and
                    menus == ['主页', '亿教课堂', '我的任务', '错题库', '统计'])
        student_ui.logout()
        STEP(2, '使用学生B账号登录，查看首页信息')
        student_ui.open_browser()
        student_ui.login(username='hongyu')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        menus = student_ui.get_menus()
        CHECK_POINT('检查首页信息', name1 == '红玉' and microlessons == 0
                    and homework == 0 and school1 == g_school and
                    menus == ['主页', '亿教课堂', '我的任务', '错题库', '统计'])
        student_ui.wd.quit()