from lib.api.SClass import getFirstClass, sclass
from lib.webui import *
from lib.ui.AppUI import app


class TC_APP_6201:
    name = '添加老师1_TC_APP_6201'

    def teststeps(self):
        STEP(1, '获取')
        app.get_driver()
        app.vcode_login()
        STEP(2, '添加老师')
        sclassid = getFirstClass()['id']
        mes1, self.tid = app.add_teacher('唐僧', 'tangsen', '初中体育', [sclassid],
                                         '12734567676', 'tangsen@163.com', '328076001209085665')
        CHECK_POINT('提示信息是否正确:', mes1 == '添加成功')

    def teardown(self):
        # 删除创建的老师
        app.click_menu_opt('老师')
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        app.del_teacher_by_tid(self.tid)
        INFO('删除创建的老师')
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        app.driver.quit()

