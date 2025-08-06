import os
from hytest import INFO
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
from cfg.cfg import desired_caps, app_server_url, gradeToId, subjectToId
from lib.webui import get_element_with_retry, get_text_with_retry


class AppUI:

    def get_driver(self):
        INFO('连接Appium Server')
        # 连接Appium Server，初始化自动化环境
        self.driver = webdriver.Remote(app_server_url,
                                  options=UiAutomator2Options().load_capabilities(desired_caps))
        # 设置缺省等待时间
        self.driver.implicitly_wait(10)
        INFO(f"Session ID: {self.driver.session_id}")

    def vcode_login(self, ip='http://192.168.1.49', vcode='00000004074389951477'):
        # 登录
        eles = get_element_with_retry(self.driver, AppiumBy.CLASS_NAME, 'android.widget.EditText', True)
        # print(f'len(eles):{len(eles)}')
        eles[0].send_keys(ip)
        eles[1].send_keys(vcode)
        # 点击登录
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="登录"]').click()
        sleep(1)

    def click_menu_opt(self, opt):
        # 点击底部菜单： 班级、老师、设置
        if opt == '班级':
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'tabnav-classes').click()
        elif opt == '老师':
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'tabnav-teachers').click()
        elif opt == '设置':
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'tabnav-settings').click()
        sleep(0.5)

    def get_one_sclass_infos(self):
        """获取班级信息，当前在“班级”页 """
        # 返回  年级、班级名称、班级id、学生人数、人数上限
        eles = get_text_with_retry(self.driver, AppiumBy.XPATH, '//android.widget.ScrollView//android.view.ViewGroup/android.widget.TextView[2]')
        eles1 = get_text_with_retry(self.driver, AppiumBy.XPATH, '//android.widget.ScrollView//android.view.ViewGroup/android.widget.TextView[3]')
        INFO(f'eles:{eles}')
        INFO(f'eles1:{eles1}')
        newgrade, newname = [i.strip() for i in eles.split(':')]
        sid, stunum, studentlimit = [int(i.split('：')[1].strip()) for i in eles1.split()]
        INFO(f'newgrade, newname, sid, stunum, studentlimit: {newgrade, newname, sid, stunum, studentlimit}')
        return newgrade, newname, sid, stunum, studentlimit

    def add_sclass(self, sclass_name, class1, studentlimit):
        """创建班级"""

        # 点击 加号 创建
        btn1 = get_element_with_retry(self.driver, AppiumBy.ACCESSIBILITY_ID, 'IconAddClass')
        btn1.click()
        sleep(1)
        eles = get_element_with_retry(self.driver, AppiumBy.CLASS_NAME, 'android.widget.EditText', True)
        # 班级名称
        eles[0].send_keys(sclass_name)
        # 年级id
        eles[1].send_keys(gradeToId[class1])
        # 学生人数最大限制
        eles[2].send_keys(studentlimit)
        sleep(0.5)
        # 点击添加
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="添加"]').click()
        sleep(0.5)
        mes = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.TextView[@resource-id="android:id/message"]').text
        mes1, sid, scinvitecode = mes.split('\n')
        sid1 = int(sid.split('：')[1])
        code = int(scinvitecode.split('：')[1])
        INFO(f'{mes1}，班级id：{sid1}，班级邀请码：{code}')
        # 点击 OK
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]').click()
        sleep(0.5)
        return mes1, sid1, code

    def del_all(self, opt):
        """删除所有班级
            opt: 班级、老师
        """
        self.click_menu_opt(opt)
        del_btns = get_element_with_retry(self.driver, AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.TextView[4]', True)
        for btn in del_btns:
            btn.click()
            sleep(0.5)
            # 点击 确定
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]').click()
            sleep(0.5)

    def del_sclass_by_sid(self, sid):
        id_infos = get_text_with_retry(self.driver, AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.TextView[3]', True)[1:]
        sids = [int(t.split()[0].split('：')[1]) for t in id_infos]
        INFO(f'sids: {sids}')
        del_btns = get_element_with_retry(self.driver, AppiumBy.XPATH,
                                          '//android.view.ViewGroup/android.widget.TextView[4]', True)
        for i, id1 in enumerate(sids):
            if id1 == sid:
                del_btns[i].click()
                sleep(0.5)
                # 点击 确定
                self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.Button[@resource-id="android:id/button1"]').click()
                sleep(0.5)
                break

    def add_teacher(self, realname, username, sub, classids, phone, email, idnum):
        """
        添加老师
        :param realname: 真实姓名
        :param username: 登录名
        :param sub: 学科， 比如 初中数学
        :param classids: 列表，授课的班级id号 [12398, 12346]
        :param phone: 手机
        :param email: 邮箱
        :param idnum: 身份证
        :return:
        """
        self.click_menu_opt('老师')
        # 将班级号变为字符串
        class_ids = '，'.join(map(str, classids))
        # 点击 加号添加
        addbtn = get_element_with_retry(self.driver, AppiumBy.ACCESSIBILITY_ID, 'IconAddTeacher')
        addbtn.click()
        sleep(1)
        eles = get_element_with_retry(self.driver, AppiumBy.CLASS_NAME, 'android.widget.EditText', True)
        eles[0].send_keys(realname)
        eles[1].send_keys(username)
        eles[2].send_keys(subjectToId[sub])
        eles[3].send_keys(class_ids)
        eles[4].send_keys(phone)
        eles[5].send_keys(email)
        eles[6].send_keys(idnum)
        # 点击 添加
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className("android.view.ViewGroup").instance(9)').click()
        sleep(1)
        mes = get_text_with_retry(self.driver, AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/message"]')
        mes1, tid1 = mes.split('\n')
        INFO(f'{mes1}, 老师id：{tid1}')
        tid = int(tid1.split('：')[1])
        # 点击OK
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]').click()
        sleep(0.5)
        # 点击返回
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="返回"]').click()
        sleep(0.5)
        return mes1, tid

    def del_teacher_by_tid(self, tid):
        """根据 sid 删除老师， 老师页面"""
        id_infos = get_text_with_retry(self.driver, AppiumBy.XPATH, '//android.view.ViewGroup/android.widget.TextView[3]', True)[1:]
        tids = [int(t.split()[0].split('：')[1]) for t in id_infos]
        INFO(f'老师ids: {tids}')
        del_btns = get_element_with_retry(self.driver, AppiumBy.XPATH,
                                          '//android.view.ViewGroup/android.widget.TextView[4]', True)
        for i, id1 in enumerate(tids):
            if id1 == tid:
                del_btns[i].click()
                sleep(0.5)
                # 点击 确定
                self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.Button[@resource-id="android:id/button1"]').click()
                sleep(0.5)
                break




app = AppUI()
