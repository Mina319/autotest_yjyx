from time import sleep
from cfg.cfg import gradeToId, g_school
from lib.api.Student import student
from lib.ui.StudnetUI import student_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_0xxx:

    ddt_cases = [
        {
            'name': '学生登录-0205',
            'para': ['', '88888888', '请输入用户名']
        },
        {
            'name': '学生登录-0206',
            'para': ['qinsang', '', '请输入密码']
        },
        {
            'name': '学生登录-0207',
            'para': ['', '', '请输入密码']
        },
        {
            'name': '学生登录-0208',
            'para': ['qinsan', '888888', '登录失败 : 用户或者密码错误']
        },
        {
            'name': '学生登录-0209',
            'para': ['qinsang', '88888', '登录失败 : 用户或者密码错误']
        },
        {
            'name': '学生登录-0210',
            'para': ['qinsan', '8888888', '登录失败 : 用户或者密码错误']
        }
    ]

    def teststeps(self):
        # 取出参数
        username, password, info = self.para
        STEP(1, '学生登录')
        student_ui.open_browser()
        wd = student_ui.wd
        student_ui.login(username=username, password=password)
        sleep(0.2)
        mes = wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        INFO(f'mes:{mes}')
        wd.close()
        CHECK_POINT('提示框消息是否正确', mes == info)


class TC_LOGINLOGOUT_204:
    name = '学生登录4_TC_LOGINLOGOUT_204'

    def teststeps(self):
        STEP(1, '访问web系统，点击忘记密码')
        student_ui.open_browser()
        mes = student_ui.forget_pwd(username='qinsang')
        student_ui.wd.close()
        INFO(f'mes:{mes}')
        CHECK_POINT('获取验证码状态', mes != '用户名不存在或未绑定手机号')


class TC_LOGINLOGOUT_211:
    name = '学生登录11_TC_LOGINLOGOUT_211'

    def teststeps(self):
        STEP(1, '登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '修改密码')
        mes = student_ui.set_pwd(orignpwd='888888', newpwd='xxxxxxx')
        CHECK_POINT('获取验证码状态', mes == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录')
        student_ui.login(username='qinsang', password='xxxxxxx')
        sname = student_ui.get_right_name()
        student_ui.wd.close()
        INFO(f'学生姓名：{sname}')
        CHECK_POINT('是否重新登录，查看用户姓名', sname == '秦桑')

    def teardown(self):
        # 将用户密码修改为默认值
        student_ui.open_browser()
        student_ui.login(username='qinsang', password='xxxxxxx')
        student_ui.set_pwd('xxxxxxx', '888888')
        student_ui.wd.close()


class TC_LOGINLOGOUT_301:
    name = '学生登出1_TC_LOGINLOGOUT_301'

    def teststeps(self):
        STEP(1, '登录web系统')
        student_ui.open_browser()
        student_ui.login(username='qinsang')
        STEP(2, '退出')
        student_ui.logout()
        STEP(3, '再次登录')
        student_ui.login(username='qinsang')
        sname = student_ui.get_right_name()
        student_ui.wd.close()
        INFO(f'学生姓名：{sname}')
        CHECK_POINT('检查是否登录成功，获取学生姓名', sname == '秦桑')
