from time import sleep

from cfg.cfg import gradeToId, g_school, subjectToId, g_ui_url_teacher
from lib.api.Teacher import teacher
from lib.api.Student import student
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *
from lib.api.SClass import getFirstClass


class TC_LOGINLOGOUT_004:
    name = '老师登录4_TC_LOGINLOGOUT_004'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        mes = teacher_ui.forget_pwd(username='zhangming')
        wd = teacher_ui.wd
        wd.close()
        INFO(f'mes:{mes}')
        CHECK_POINT('获取验证码状态', mes != '用户名不存在或未绑定手机号')


class TC_LOGINLOGOUT_011:
    name = '老师登录11_TC_LOGINLOGOUT_011'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '修改密码')
        mes = teacher_ui.set_pwd('888888', 'xxxxxxx')  # 设置新密码为 xxxxxxx
        CHECK_POINT('弹框提示信息是否正确', mes == '用户密码修改成功，点击确定，重新登录')
        STEP(3, '重新登录')
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        tname = teacher_ui.get_right_name()
        teacher_ui.wd.quit()
        INFO(f'老师姓名：{tname}')
        CHECK_POINT('检查是否登录成功，获取老师姓名', tname == '张明')

    def teardown(self):
        # 将用户密码修改为默认值
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming', password='xxxxxxx')
        teacher_ui.set_pwd('xxxxxxx', '888888')
        teacher_ui.wd.quit()


class TC_LOGINLOGOUT_012:
    name = '老师登录12_TC_LOGINLOGOUT_012'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        wd = teacher_ui.wd
        STEP(1, '重新登录web系统')
        wd.get(g_ui_url_teacher)
        tname = None
        try:
            tname = teacher_ui.get_right_name()
        except Exception as e:
            INFO(f'获取用户名失败，异常信息：{e}')
        finally:
            wd.quit()
            CHECK_POINT('检查再次登录是否可以直接跳转主页', tname == '张明')


class TC_LOGINLOGOUT_013:
    name = '老师登录13_TC_LOGINLOGOUT_013'

    def teststeps(self):
        STEP(1, '使用学生账号登录老师web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='qinsang')
        wd = teacher_ui.wd
        sleep(0.2)
        mes = wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        INFO(f'mes:{mes}')
        wd.quit()
        CHECK_POINT('提示框消息是否正确', mes == '登录失败 : 用户或者密码错误')


class TC_LOGINLOGOUT_101:
    name = '老师登出1_TC_LOGINLOGOUT_101'

    def teststeps(self):
        STEP(1, '登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '退出')
        teacher_ui.logout()
        STEP(3, '再次登录')
        teacher_ui.login(username='zhangming')
        tname = teacher_ui.get_right_name()
        teacher_ui.wd.quit()
        INFO(f'老师姓名：{tname}')
        CHECK_POINT('检查是否登录成功，获取老师姓名', tname == '张明')
