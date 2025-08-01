from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_HOME_103:
    name = '学生首页信息3_TC_HOME_103'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        sleep(0.5)
        # 刷新当前页面
        student_ui.wd.refresh()
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        menus = student_ui.get_menus()
        sleep(0.4)
        student_ui.wd.quit()
        CHECK_POINT('检查首页信息', name1 == '秦桑' and microlessons == 0
                    and homework == 0 and school1 == g_school and
                    menus == ['主页', '亿教课堂', '我的任务', '错题库', '统计'])


class TC_HOME_104:
    name = '学生首页信息4_TC_HOME_104'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '修改姓名')
        newrealname = '桑桑'
        mes = student_ui.set_realname(newrealname)
        CHECK_POINT('用户修改信息是否成功', mes == '用户信息修改成功')
        STEP(3, '查看首页姓名')
        student_ui.login(username='qinsang')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        name2 = student_ui.get_right_name()
        CHECK_POINT('检查修改后的姓名是否正确', newrealname == name1 and newrealname == name2)
        student_ui.logout()
        STEP(4, '重新登录检查姓名')
        student_ui.login(username='qinsang')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        name2 = student_ui.get_right_name()
        student_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', newrealname == name1 and newrealname == name2)

    def teardown(self):
        # 将学生姓名修改回来
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        student_ui.set_realname('秦桑')
        student_ui.wd.quit()


class TC_HOME_105:
    name = '学生首页信息5_TC_HOME_105'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '修改密码')
        mes = student_ui.set_pwd(orignpwd='888888', newpwd='xxxxxxx')
        CHECK_POINT('用户修改密码是否成功', mes == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录，查看首页姓名')
        student_ui.login(username='qinsang', password='xxxxxxx')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        name2 = student_ui.get_right_name()
        CHECK_POINT('检查修改后的姓名是否正确', '秦桑' == name1 and '秦桑' == name2)
        STEP(4, '重新登录检查姓名')
        student_ui.login(username='qinsang', password='xxxxxxx')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        name2 = student_ui.get_right_name()
        student_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', '秦桑' == name1 and '秦桑' == name2)

    def teardown(self):
        # 将密码修改回来
        student_ui.open_browser()
        student_ui.login(username='qinsang', password='xxxxxxx')
        student_ui.set_pwd('xxxxxxx', '888888')
        student_ui.wd.quit()


class TC_HOME_106:
    name = '学生首页信息6_TC_HOME_106'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '修改姓名和密码')
        mes1 = student_ui.set_realname('桑桑')
        CHECK_POINT('用户修改密码是否成功', mes1 == '用户信息修改成功')
        mes2 = student_ui.set_pwd(orignpwd='888888', newpwd='xxxxxxx')
        CHECK_POINT('用户修改密码是否成功', mes2 == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录，查看首页姓名')
        student_ui.login(username='qinsang', password='xxxxxxx')
        name1, school1, microlessons, homework = student_ui.get_home_infos()
        name2 = student_ui.get_right_name()
        student_ui.wd.quit()
        CHECK_POINT('检查修改后的姓名是否正确', '桑桑' == name1 and '桑桑' == name2)

    def teardown(self):
        # 将姓名、密码修改回来
        student_ui.open_browser()
        student_ui.login(username='qinsang', password='xxxxxxx')
        student_ui.set_realname('秦桑')
        student_ui.login(username='qinsang', password='xxxxxxx')
        student_ui.set_pwd('xxxxxxx', '888888')
        student_ui.wd.quit()


class TC_HOME_107:
    # 暂时无法测试，所有图像都未显示
    name = '学生首页信息7_TC_HOME_107'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '修改头像')
        mes1 = student_ui.set_icon()
        sleep(0.4)
        student_ui.wd.quit()
        CHECK_POINT('用户修改头像是否成功', mes1 == '用户信息修改成功')

    def teardown(self):
        # 将头像修改回来
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        student_ui.set_icon()
        student_ui.wd.quit()


class TC_HOME_108:
    name = '学生首页信息8_TC_HOME_108'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '提交空的意见')
        mes1 = student_ui.submit_view()
        INFO(f'mes: {mes1}')
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '请选择分类')
        student_ui.wd.quit()

class TC_HOME_109:
    name = '学生首页信息9_TC_HOME_109'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '选择意见种类：操作不方便')
        mes1 = student_ui.submit_view(0)
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '请填写详细说明')
        student_ui.wd.quit()

class TC_HOME_110:
    name = '学生首页信息10_TC_HOME_110'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '选择意见种类：系统错误')
        mes1 = student_ui.submit_view(1, '系统错误', '1111111111')
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '提交成功，感谢您的意见，我们将尽快处理')
        student_ui.wd.quit()

class TC_HOME_111:
    name = '学生首页信息11_TC_HOME_111'

    def teststeps(self):
        STEP(1, '学生登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '选择意见种类：不能登录，提交意见')
        mes1 = student_ui.submit_view(2, '不能登录', '1111111111')
        CHECK_POINT('提交意见反馈提示文本是否正确', mes1 == '提交成功，感谢您的意见，我们将尽快处理')
        STEP(3, '检查意见提交后是否清空')
        view = student_ui.wd.find_element(By.CSS_SELECTOR, '.col-md-12 textarea').text
        phone = student_ui.wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div/div[3]/div/input').text
        CHECK_POINT('检查意见是否清除', view == '')
        CHECK_POINT('检查意见是否清除', phone == '')
        student_ui.wd.quit()


