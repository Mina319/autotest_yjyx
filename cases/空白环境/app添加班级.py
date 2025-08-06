from lib.webui import *
from lib.ui.AppUI import app


class TC_APP_6101:
    name = '添加班级1_TC_APP_6101'

    def teststeps(self):
        STEP(1, '获取')
        app.get_driver()
        app.vcode_login()
        STEP(2, '添加班级')
        mes1, self.sid1, code = app.add_sclass('实验一班', "七年级", 60)
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        CHECK_POINT('提示信息是否正确:', mes1 == '添加成功')

    def teardown(self):
        # 删除创建的班级
        app.del_sclass_by_sid(self.sid1)
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        app.driver.quit()


