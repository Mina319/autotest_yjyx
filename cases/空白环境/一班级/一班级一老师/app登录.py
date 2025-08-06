from lib.api.SClass import sclass, getFirstClass
from lib.webui import *
from lib.ui.AppUI import app
from appium.webdriver.common.appiumby import AppiumBy


class TC_APP_6003:
    name = 'vcode登录3_TC_APP_6003'

    def teststeps(self):
        STEP(1, '使用正确的vcode登录')
        app.get_driver()
        app.vcode_login()
        sleep(1)
        STEP(2, '查看存在的班级信息是否正确')
        newgrade, newname, sid, stunum, studentlimit = app.get_one_sclass_infos()
        # {'name': '实验二班', 'grade__name': '八年级', 'invitecode': '202563130374', 'studentlimit': 50,
        # 'studentnumber': 0, 'id': 20256, 'teacherlist': []}
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        app.driver.quit()
        name, grade_name, _, studentlimit1, stunum1, sid1, _ = getFirstClass().values()
        CHECK_POINT('检查班级信息是否正确:', newgrade == grade_name and name == newname and sid1 == sid and
                    stunum == stunum1 and studentlimit1 == studentlimit)
