from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Teacher import teacher
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_002:
    name = '老师首页信息2_TC_HOME_002'

    def teststeps(self):
        STEP(1, '使用老师A账号登录，查看首页信息')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        menus = teacher_ui.get_menus()
        CHECK_POINT('检查首页信息', name1 == '张明' and subject1 == '初中数学' and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school and
                    menus == ['主页', '微课', '作业', '题目', '班级情况'])
        teacher_ui.logout()
        STEP(2, '使用老师B账号登录，查看首页信息')
        teacher_ui.open_browser()
        teacher_ui.login(username='tangsen')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        menus = teacher_ui.get_menus()
        CHECK_POINT('检查首页信息', name1 == '唐僧' and subject1 == '初中科学' and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school and
                    menus == ['主页', '微课', '作业', '题目', '班级情况'])

