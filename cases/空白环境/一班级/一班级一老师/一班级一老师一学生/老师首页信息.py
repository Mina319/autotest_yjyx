from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Teacher import teacher
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_003:
    name = '老师首页信息3_TC_HOME_003'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        sleep(0.5)
        # 刷新当前页面
        teacher_ui.wd.refresh()
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        menus = teacher_ui.get_menus()
        CHECK_POINT('检查首页信息', name1 == '张明' and subject1 == '初中数学' and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school and
                    menus == ['主页', '微课', '作业', '题目', '班级情况'])


class TC_HOME_004:
    name = '老师首页信息4_TC_HOME_004'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(1, '修改姓名')
        newrealname = '明明'
        mes = teacher_ui.set_realname(newrealname)
        CHECK_POINT('用户修改信息是否成功', mes == '用户信息修改成功')
        STEP(2, '查看首页姓名')
        # 点击 主页
        teacher_ui.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        name2 = teacher_ui.get_right_name()
        CHECK_POINT('检查修改后的姓名是否正确', newrealname == name1 and newrealname == name2)
        teacher_ui.logout()
        STEP(2, '重新登录检查姓名')
        teacher_ui.login(username='zhangming')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        name2 = teacher_ui.get_right_name()
        teacher_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', newrealname == name1 and newrealname == name2)

    def teardown(self):
        # 将老师姓名修改回来
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        teacher_ui.set_realname('张明')
        teacher_ui.wd.quit()


class TC_HOME_005:
    name = '老师首页信息5_TC_HOME_005'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '修改密码')
        mes = teacher_ui.set_pwd(orignpwd='888888', newpwd='xxxxxxx')
        CHECK_POINT('用户修改密码是否成功', mes == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录，查看首页姓名')
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        # 点击 主页
        teacher_ui.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        name2 = teacher_ui.get_right_name()
        CHECK_POINT('检查修改后的姓名是否正确', '张明' == name1 and '张明' == name2)
        teacher_ui.logout()
        STEP(4, '重新登录检查姓名')
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        name2 = teacher_ui.get_right_name()
        teacher_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', '张明' == name1 and '张明' == name2)

    def teardown(self):
        # 将密码修改回来
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        teacher_ui.set_pwd('xxxxxxx', '888888')
        teacher_ui.wd.quit()


class TC_HOME_006:
    name = '老师首页信息6_TC_HOME_006'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '修改姓名和密码')
        mes1 = teacher_ui.set_realname('明明')
        CHECK_POINT('用户修改密码是否成功', mes1 == '用户信息修改成功')
        mes2 = teacher_ui.set_pwd(orignpwd='888888', newpwd='xxxxxxx')
        CHECK_POINT('用户修改密码是否成功', mes2 == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录，查看首页姓名')
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        # 点击 主页
        school1, name1, subject1, goldcoin, microlessons, homework = teacher_ui.get_home_infos()
        name2 = teacher_ui.get_right_name()
        teacher_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', '明明' == name1 and '明明' == name2)

    def teardown(self):
        # 将姓名、密码修改回来
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        teacher_ui.set_realname('张明')
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        teacher_ui.set_pwd('xxxxxxx', '888888')
        teacher_ui.wd.quit()


class TC_HOME_007:
    # 暂时无法测试，所有图像都未显示
    name = '老师首页信息7_TC_HOME_007'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '修改头像')
        mes1 = teacher_ui.set_icon()
        sleep(0.4)
        teacher_ui.wd.quit()
        CHECK_POINT('用户修改头像是否成功', mes1 == '用户信息修改成功')

    def teardown(self):
        # 将头像修改回来
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        teacher_ui.set_icon()
        teacher_ui.wd.quit()


class TC_HOME_008:
    name = '老师首页信息8_TC_HOME_008'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '提交空的意见')
        mes1 = teacher_ui.submit_view()
        sleep(0.4)
        teacher_ui.wd.quit()
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '请选择分类')


class TC_HOME_009:
    name = '老师首页信息9_TC_HOME_009'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '选择意见种类：操作不方便')
        mes1 = teacher_ui.submit_view(0)
        sleep(0.4)
        teacher_ui.wd.quit()
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '请填写详细说明')


class TC_HOME_010:
    name = '老师首页信息10_TC_HOME_010'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '选择意见种类：系统错误')
        mes1 = teacher_ui.submit_view(1, '系统错误', '1111111111')
        sleep(0.4)
        teacher_ui.wd.quit()
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '提交成功，感谢您的意见，我们将尽快处理')


class TC_HOME_011:
    name = '老师首页信息11_TC_HOME_011'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')

        try:
            STEP(2, '选择意见种类：不能登录，提交意见')
            mes1 = teacher_ui.submit_view(2, '不能登录', '1111111111')
            CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '提交成功，感谢您的意见，我们将尽快处理')
            STEP(3, '检查意见提交后是否清空')
            view = teacher_ui.wd.find_element(By.CSS_SELECTOR, '.col-md-12 textarea').text
            phone = teacher_ui.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div[3]/div/input').text
            CHECK_POINT('检查意见是否清除', view == '')
            CHECK_POINT('检查意见是否清除', phone == '')
        finally:
            teacher_ui.wd.quit()



