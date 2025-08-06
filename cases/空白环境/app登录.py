from lib.webui import *
from lib.ui.AppUI import app
from appium.webdriver.common.appiumby import AppiumBy


class TC_APP_6001:
    name = 'vcode登录1_TC_APP_6001'

    def teststeps(self):
        STEP(1, '使用无效的vcode登录')
        app.get_driver()
        app.vcode_login(vcode='243546576879809')
        # 提示框信息
        mes = app.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/message"]').text
        SELENIUM_LOG_SCREEN(app.driver, '30%')
        app.driver.quit()
        CHECK_POINT('提示信息是否正确:', mes == '登录失败 : vcode format error:1')


class TC_APP_6002:
    name = 'vcode登录2_TC_APP_6002'

    def teststeps(self):
        STEP(1, '使用正确的vcode登录')
        app.get_driver()
        app.vcode_login()
        mes = None
        try:
            mes = get_text_with_retry(app.driver, AppiumBy.XPATH, '//android.widget.TextView[@content-desc="no-class-warning"]')
            INFO(f'mes: {mes}')
            SELENIUM_LOG_SCREEN(app.driver, '30%')
        except Exception as e:
            print(e)
        finally:
            app.driver.quit()
        if mes:
            CHECK_POINT('提示信息是否正确:', mes == '该学校还没有班级，点击刷新')
        else:
            CHECK_POINT('不通过: 未成功登录', False)
