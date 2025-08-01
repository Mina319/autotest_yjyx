import datetime

import selenium
from selenium import webdriver
from hytest import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from lib.webui import get_element_with_retry, get_text_with_retry


class TeacherUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # 添加无头模式配置
        # options.add_argument('--headless')  # 启用无头模式
        # options.add_argument('--disable-gpu')  # 禁用 GPU 加速 (在某些系统上有帮助)
        # options.add_argument('--no-sandbox')  # 某些系统可能需要此选项

        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)

    def login(self, username, password='888888'):
        # 登录
        self.wd.get(g_ui_url_teacher)
        self.wd.find_element(By.ID, 'username').send_keys(username)
        self.wd.find_element(By.ID, 'password').send_keys(password)
        # 点击登录
        self.wd.find_element(By.ID, 'submit').click()

    def logout(self):
        # 登出
        # 点击 右上角 用户名
        sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 退出
        self.wd.find_element(By.CSS_SELECTOR, '.fa-key').click()

    def get_right_name(self):
        # 获取主页  右上角 用户名
        tname = self.wd.find_element(By.CSS_SELECTOR, 'li.dropdown .ng-binding').text
        return tname

    def get_home_infos(self, home=None):
        # 返回页面 捕获的 学校、姓名、学科、金币、已发布微课、已发布作业数量信息
        # 主页页面
        # 等待 school 信息加载
        if home:
            # 点击主页
            get_element_with_retry(self.wd, By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        sleep(2)
        infos_ele = self.wd.find_elements(By.XPATH, '//table//td[2]/a')
        infos = [e.text for e in infos_ele]
        school1, name1, subject1, goldcoin = infos
        goldcoin = 0 if goldcoin == '' else int(goldcoin)
        sleep(1)
        infos_ele1 = self.wd.find_elements(By.XPATH, '//*[@class="col-md-12"]//a/h2/strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        return school1, name1, subject1, goldcoin, microlessons, homework

    def get_menus(self):
        # 获取主页 菜单
        menus = []
        home = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').text
        eles = self.wd.find_elements(By.CSS_SELECTOR, '.main-menu li > a')
        menus.append(home)
        menus += [e.text for e in eles]
        return menus

    def has_students(self):
        # 查看该老师的学生数量，返回{班级名称：学生人数}， 学生总人数
        # 主页页面
        # 点击班级情况
        sleep(0.4)
        res = {}
        self.wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]').click()
        # 点击班级学生
        self.wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]//li/span').click()
        sleep(0.2)

        # 点击 所有班级
        eles = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[1]/a')
        for e in eles:
            e.click()

        stuClass = self.wd.find_elements(By.XPATH, "//*[contains(@class, 'fa-home')]/..")
        sClassname = [i.text.strip() for i in stuClass]
        nums = self.wd.find_elements(By.CSS_SELECTOR, '.panel-heading .ng-scope')
        sum1 = 0
        for i, sname in enumerate(sClassname):
            num = int(nums[i].text)
            sum1 += num
            res[sname] = num
        return res, sum1

    def forget_pwd(self, username):
        # 点击忘记密码
        self.wd.get(g_ui_url_teacher)
        sleep(1)
        mainWindow = self.wd.current_window_handle
        self.wd.find_element(By.XPATH, '//*[@id="reg-for"]/ul/li/a').click()
        sleep(0.5)
        # 切换页面
        # 所有窗口的句柄
        allHandles = self.wd.window_handles
        # 进入新窗口
        self.wd.switch_to.window(allHandles[-1])
        self.wd.find_element(By.XPATH, '//dd/input').send_keys(username)
        # 点击 获取手机验证码
        self.wd.find_element(By.CSS_SELECTOR, '.subtijiao input').click()
        # 获取信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.ng-binding').text
        # 关闭当前（忘记密码）窗口
        self.wd.close()
        # 切换回主窗口
        self.wd.switch_to.window(mainWindow)
        return mes

    def click_right(self):
        # 点击个人信息
        # 点击 右上角头像
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 个人信息
        self.wd.find_element(By.CSS_SELECTOR, '.fa-user').click()

    def set_pwd(self, orignpwd, newpwd):
        # 账号登录状态  设置新密码newpwd

        self.click_right()

        # 点击 登录密码修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[3]').click()

        # 获取三个输入框
        inputs = self.wd.find_elements(By.CSS_SELECTOR, 'table.table_password tr input')
        # 输入当前密码
        inputs[0].send_keys(orignpwd)
        # 输入修改密码
        inputs[1].send_keys(newpwd)
        # 确认当前密码
        inputs[2].send_keys(newpwd)
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, 'table.table_password button').click()

        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        return mes

    def set_realname(self, new):
        # 账号登录状态  设置新用户名

        self.click_right()
        # 点击 基本信息修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[2]').click()

        # 获取 输入框
        inputs = self.wd.find_elements(By.XPATH, '//tbody/tr/td[2]/div/input')
        # 输入 新姓名
        inputs[0].clear()
        inputs[0].send_keys(new)

        # 点击确定
        self.wd.find_element(By.XPATH, '//tbody/tr[3]/td/div/button').click()
        sleep(0.3)
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()

        return mes

    def set_icon(self):
        # 设置头像
        self.click_right()
        # 点击 基本信息修改
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div[2]/ul/li[2]').click()
        # 点击 选择图片
        self.wd.find_element(By.XPATH, '//figure/a[1]').click()
        # 点击选择的图片
        self.wd.find_elements(By.CSS_SELECTOR, '.pop-ico img')[0].click()
        # 点击确定
        self.wd.find_element(By.XPATH, '//table/tbody/tr[3]/td/div/button').click()
        # 获取提示框信息
        mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        return mes

    def submit_view(self, viewtype=None, detai=None, phone=None):
        # 点击 右上角头像
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a').click()
        # 点击 意见反馈
        self.wd.find_element(By.CSS_SELECTOR, '.fa-envelope-o').click()
        if viewtype is not None:
            # 选择意见: 操作不方便 系统错误 不能登录 授课信息变更 变更学校 其他
            eles = self.wd.find_elements(By.CSS_SELECTOR, '.col-md-12 label')
            eles[viewtype].click()
        if detai is not None:
            ele = self.wd.find_element(By.CSS_SELECTOR, '.col-md-12 textarea')
            ele.clear()
            ele.send_keys(detai)
        if phone is not None:
            ele = self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div[3]/div/input')
            ele.clear()
            ele.send_keys(phone)

        # 点击 提交
        self.wd.find_element(By.CSS_SELECTOR, '.col-md-2 button').click()
        res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        return res

    def opt_homework(self, opt):
        # 点击作业
        # self.wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        btn = get_element_with_retry(self.wd, By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a')
        btn.click()
        sleep(1)
        if opt == '创建作业':
            # 创建作业
            # self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
            btn = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span')
            self.wd.execute_script("arguments[0].click();", btn)
        elif opt == '已创建作业':
            # 已创建作业
            self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[3]/li/span').click()
        elif opt == '已发布作业':
            self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[4]/li/span').click()
        sleep(1)

    def revoke_homework(self, taskname):
        # 根据 taskname 撤销未被学生做过的作业
        flag = False
        self.opt_homework(opt='已发布作业')
        taskname_eles = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody//tr//td[3]')
        tasknames = [i.text.strip for i in taskname_eles]
        num = len(tasknames)
        for i, t in enumerate(tasknames):
            if t == taskname:
                revokes = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody//tr/td[6]/a')
                revokes[i].click()  # 撤销
                # 点击确定撤销
                self.wd.find_element(By.XPATH,
                                     "//*[@class='bootstrap-dialog-footer-buttons']//button[text()='确定']").click()
                flag = True
        taskname_eles = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody//tr//td[3]')

        msg = None
        # 如果撤销不了的情况
        try:
            msg = self.wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        except Exception as e:
            print(e)

        if msg:
            return msg

        if msg is None and flag:
            return len(taskname_eles)
        # CHECK_POINT('是否撤销成功', num - 1 == len(taskname_eles))

    def get_num_of_published_homework(self):
        # 统计已发布作业都个数

        e = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody//tr')
        return len(e)

    def del_homework_by_taskname(self, taskname):

        # 当前窗口
        window1 = self.wd.current_window_handle
        t_eles = self.wd.find_elements(By.CSS_SELECTOR, '.row .div-search-result-one-text')
        num = len(t_eles)  # 已发布作业个数
        t = [i.text.strip() for i in t_eles]
        # del_eles = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]//div//label[3]')
        for i, t1 in enumerate(t):
            if t1 == taskname:
                del_eles = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]//div//label[3]')
                # del_eles[i].click()
                self.wd.execute_script("arguments[0].click();", del_eles[i])
                sleep(1)

        window2 = self.wd.current_window_handle
        self.wd.switch_to.window(window2)
        # 点击确定
        button = get_element_with_retry(self.wd, By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']//button[text()='确定']")
        # button = self.wd.find_element(By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']//button[text()='确定']")
        self.wd.execute_script("arguments[0].click();", button)
        sleep(1)
        self.wd.switch_to.window(window1)
        num1 = len(self.wd.find_elements(By.CSS_SELECTOR, '.row .div-search-result-one-text'))
        return num1 == num - 1

    def del_homework_by_taskname1(self, taskname):

        t_eles = self.wd.find_elements(By.CSS_SELECTOR, '.row .div-search-result-one-text')
        t = [i.text.strip() for i in t_eles]
        # del_eles = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]//div//label[3]')
        for i, t1 in enumerate(t):
            if t1 == taskname:
                del_eles = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]//div//label[3]')
                # del_eles[i].click()
                self.wd.execute_script("arguments[0].click();", del_eles[i])
                sleep(1)

        window2 = self.wd.current_window_handle
        self.wd.switch_to.window(window2)
        # 点击确定
        # button = self.wd.find_element(By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']//button[text()='确定']")
        button = get_element_with_retry(self.wd, By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']//button[text()='确定']")
        self.wd.execute_script("arguments[0].click();", button)
        sleep(1)
        msg = self.wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        return msg

    def publish_homework(self, taskname='作业1', mes='新建作业成功', num=3, filter=None, ispublished=False):
        # 新建作业-不发布

        # 创建作业
        self.opt_homework(opt='创建作业')
        sleep(0.2)
        if taskname is None or taskname.strip() == '':
            # 点击 确定添加
            self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
            sleep(0.5)
            mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
            CHECK_POINT('弹窗消息是否正确', mes == '请输入作业名称')
            return

        input = self.wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        input.send_keys(taskname)
        self.wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(0.5)
        # 切换窗口iframe，选择题目的小窗口
        self.wd.switch_to.frame("pick_questions_frame")
        sleep(1)
        ### 筛选条件
        dict1 = {'按章节': 0, '按知识点': 1,
                 '选择题': 0, '填空题': 1,
                 '浙教版': 0, '人教版': 1,
                 '七年级': 0, '八年级': 1, '九年级': 2, '高一': 3, '高二': 4, '高三': 5,
                 '上册': 0, '下册': 1,
                 '简单': 0, '中等': 1, '较难': 2}
        if filter is not None:
            # 按章节 按知识点
            if filter[0] is not None:
                eles = get_element_with_retry(self.wd, By.XPATH, '//*[@id="btn_group_treetype"]/label', True)
                # eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_treetype"]/label')
                idx = dict1[filter[0]]
                eles[idx].click()
                sleep(0.5)
            # 选择题 填空题
            if filter[1] is not None:
                eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_questiontypes"]/label')
                idx = dict1[filter[1]]
                eles[idx].click()
                sleep(0.5)
            # 浙教版 人教版
            if filter[2] is not None:
                eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_textbookvers"]/label')
                idx = dict1[filter[2]]
                eles[idx].click()
                sleep(0.5)
            # 年纪 七 八 九 高一 二 三
            if filter[3] is not None:
                eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_grades"]/label')
                idx = dict1[filter[3]]
                eles[idx].click()
                sleep(0.5)
            # 上册 下册
            if filter[4] is not None:
                eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_textbookvols"]/label')
                idx = dict1[filter[4]]
                eles[idx].click()
                sleep(0.5)
            # 难度：简单 中等 较难
            if filter[5] is not None:
                eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_level"]/label')
                idx = dict1[filter[5]]
                eles[idx].click()
                sleep(0.5)
            # 我创建的
            if filter[6] is not None:
                self.wd.find_element(By.XPATH, '//*[@id="onlysearchmine"]').click()
                sleep(0.5)

        ############
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        n = num // 10
        remainder = num % 10
        for i in range(n):
            # 等待“本页全部加入”按钮可点击并点击
            add_all_btn = WebDriverWait(self.wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_footer"]/div[2]'))
            )
            # add_all_btn.click()
            self.wd.execute_script("arguments[0].click();", add_all_btn)
            sleep(0.2)  # 稍微等待一下加入完成

            # 等待“下一页”按钮可点击并点击
            next_page_btn = WebDriverWait(self.wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_serach_next_page"]'))
            )

            # next_page_btn.click()
            self.wd.execute_script("arguments[0].click();", next_page_btn)
            sleep(0.2)  # 再加一点缓冲时间

        # 点击最后一页的前 remainder 个题目
        if remainder > 0:
            for j in range(remainder):
                options = get_element_with_retry(self.wd, By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)', True)
                self.wd.execute_script("arguments[0].click();", options[j])
        if num > 100:
            try:
                e = self.wd.find_element(By.XPATH, '//*[@id="alert_msg"]').text
                return e
            except:
                pass
        # 点击确定
        sleep(0.5)
        # self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        btn1 = self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]')
        self.wd.execute_script("arguments[0].click();", btn1)
        # btn = WebDriverWait(self.wd, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]'))
        # )
        # self.wd.execute_script("arguments[0].click();", btn)
        sleep(0.5)

        # 切换窗口：点击确认添加  按钮
        window1 = self.wd.current_window_handle
        self.wd.switch_to.window(window1)
        sleep(0.5)
        # 确认添加
        self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(0.5)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = self.wd.current_window_handle
        self.wd.switch_to.window(window2)
        sleep(1)
        mes11 = self.wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-message h3').text
        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        if ispublished:
            # 点击发布
            self.wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()
            self.mainWindow = window1
        else:
            self.wd.find_element(By.XPATH, '//button[text()="暂不发布"]').click()
            self.wd.switch_to.window(window1)
        CHECK_POINT('是否新建作业成功', mes == mes11)

    def publish_process(self, taskname, taskdec, mes1, time=30, num=0, checkall=False):
        self.opt_homework('已创建作业')
        window2 = self.wd.current_window_handle
        flag = True
        homework = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[1]')
        h = [i.text for i in homework]
        for i, h1 in enumerate(h):
            if h1 == taskname:
                # 找到任务
                publish_btns = self.wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]')
                publish_btns[i].click()
                flag = False
        if flag:
            INFO(f'没用找到要发布的作业：{taskname}')
            return
        allwindows = self.wd.window_handles
        self.wd.switch_to.window(allwindows[-1])
        studnets = self.wd.find_elements(By.XPATH, '//tbody//span')

        if 0 < num < len(studnets):
            for i in range(num):
                studnets = self.wd.find_elements(By.XPATH, '//tbody//span')
                studnets[i].click()

        if checkall:
            # 点击全选
            self.wd.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[1]/a').click()

        sleep(1)
        # 点击 确定下发
        btn = get_element_with_retry(self.wd, By.CSS_SELECTOR, 'h3 > button')
        btn.click()
        # WebDriverWait(self.wd, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'h3 > button'))
        # ).click()

        if num == 0 and not checkall:
            mes = self.wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
            self.wd.switch_to.window(self.mainWindow)
            CHECK_POINT('检查弹窗信息', mes1 == mes)
            return
        time_e = self.wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[2]/input')
        time_e.clear()
        time_e.send_keys(str(time))
        sleep(1)
        dec = self.wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[2]/textarea')
        dec.clear()
        dec.send_keys(taskdec)
        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        sleep(1)
        # mes = self.wd.find_element(By.CLASS_NAME, 'bootstrap-dialog-message').text
        mes = get_text_with_retry(self.wd, By.CLASS_NAME, 'bootstrap-dialog-message')
        # 点击确定
        btn1 = get_element_with_retry(self.wd, By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']/button[text()='确定']")
        btn1.click()
        # self.wd.find_element(By.XPATH, "//*[@class='bootstrap-dialog-footer-buttons']/button[text()='确定']").click()
        sleep(1)
        self.wd.switch_to.window(window2)
        CHECK_POINT('检查弹窗信息', mes1 == mes[:8])
        taskid = ''.join([char for char in mes if char.isdigit()])
        return taskid

    def publish_homework1(self, taskname, mes):
        # 发布作业
        # 点击作业
        self.wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        btn1 = get_element_with_retry(self.wd, By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span')
        btn1.click()

        # 切换窗口：点击确认添加  按钮
        window1 = self.wd.current_window_handle

        input = self.wd.find_element(By.XPATH, '//*[@id="exam_name_text"]')
        input.send_keys(taskname)
        self.wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(1)
        # 切换窗口iframe，选择题目的小窗口
        self.wd.switch_to.frame("pick_questions_frame")
        sleep(1)
        ############
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        for i in range(3):
            options = self.wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
            options[i].click()
            sleep(1)

        # 点击 清空试题篮
        self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[3]').click()

        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(0.5)

        # 切换窗口：
        self.wd.switch_to.window(window1)
        sleep(0.5)
        # 确认添加
        self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(0.5)

        # 切换窗口：弹框“新建作业成功”，点击发布给学生
        window2 = self.wd.current_window_handle
        self.wd.switch_to.window(window2)
        sleep(1)
        mes11 = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        CHECK_POINT('是否新建作业成功', mes == mes11)

        # 点击确定
        self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()
        self.wd.switch_to.window(window1)

    def create_questions(self, type=None, difflevel=None, knowleadege=None, textbook=None, content=None, video=None,
                         answer=None, desc=None, opt=3):
        # 创建题目
        # type： 0 选择题， 1 填空题
        # difflevel：0 简单， 1 中等， 2 难
        # knowleadege：选择knowleadege个知识点
        # textbook：[[0, 0, 0]]
        # 0浙教版 1人教版
        # 0七年级 1八年级 2九年级 3高一 4高二 5高三
        # 0上册 1下册
        # content: 题目内容
        # video： 视频
        # answer：[答案个数, [具体答案]]
        # desc: 解释说明
        # opt 1继续添加题目 2重新编辑 3 确定，

        # 点击 题目
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
        sleep(1)
        # 点击 创建题目
        btn = self.wd.find_element(By.CSS_SELECTOR, '.fa-plus-square-o')
        self.wd.execute_script("arguments[0].click();", btn)

        sleep(1)
        if type is not None:
            sleep(0.4)
            # eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_questiontypes"]/label')
            eles = get_element_with_retry(self.wd, By.XPATH, '//*[@id="btn_group_questiontypes"]/label', True)
            # eles[type].click()
            self.wd.execute_script("arguments[0].click();", eles[type])
            sleep(1)

        if difflevel is not None:
            sleep(0.4)
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_level"]/label')
            # eles[difflevel].click()
            self.wd.execute_script("arguments[0].click();", eles[difflevel])

        if knowleadege is not None:
            # 点击 选择
            sleep(0.4)
            self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]').click()
            # 点击 初中数学左边的三角
            self.wd.find_element(By.XPATH, '//*[@id="ZSD_1_0"]/i').click()

            # 点击 所有章
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[1].click()
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[2].click()

            div_elements = self.wd.find_elements(By.CSS_SELECTOR, 'a i.jstree-checkbox:nth-child(1)')[4:]
            for i in range(knowleadege):
                div_elements[i].click()

            # 点击 确定
            self.wd.find_element(By.XPATH, '//*[@id="btn_selectTree_ok"]').click()

        if textbook is not None:
            if textbook == 14:
                # 编号14用例
                # 点击 增加
                self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
                eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
                eles[0].click()  # 选择 浙教版
                nianji = self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_grades_1 label')
                # 强制点击 七年级和八年级
                self.wd.execute_script("arguments[0].click();", nianji[0])
                self.wd.execute_script("arguments[0].click();", nianji[1])

            else:
                for m, e in enumerate(textbook):
                    INFO(f'textbook:{textbook}')
                    i, j, k = e
                    # 点击 增加
                    element = self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a')
                    self.wd.execute_script("arguments[0].click();", element)
                    eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
                    eles[i].click()  # 选择 浙教版 或 人教版
                    # self.wd.execute_script("arguments[0].click();", eles[i])
                    sleep(1)
                    nianji = self.wd.find_elements(By.XPATH,
                                                   f'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[{m + 1}]/table/tbody/tr[1]/td[3]/div//label')
                    # 强制点击
                    self.wd.execute_script("arguments[0].click();", nianji[j])
                    cehao = self.wd.find_elements(By.XPATH,
                                                  f'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[{m + 1}]/table/tbody/tr[2]/td[3]/div//label')
                    self.wd.execute_script("arguments[0].click();", cehao[k])  # 选择 册号

        if content is not None:
            # 获取输入框
            # 切换到iframe
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_element(By.CSS_SELECTOR, 'iframe.ke-edit-iframe')
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[0].send_keys(content)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        if video is not None:
            # 点击 选择视频文件
            for i in video:
                self.wd.find_element(By.XPATH, '//*[@id="pick_video_files"]').send_keys(rf'{i}')

        if answer is not None:
            input = self.wd.find_element(By.XPATH, '//*[@id="Question_AnswerNum_text"]')
            input.clear()
            input.send_keys(answer[0])
            sleep(0.5)
            if answer[1][0] is not None and 1 <= answer[0] <= 10:
                if type == 0:
                    # 选择题  点击正确答案
                    eles = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/label')
                    if answer[1][0] is not None and len(eles) != 0:
                        # eles[answer[1][0]].click()
                        for i in answer[1]:
                            self.wd.execute_script("arguments[0].click();", eles[i])
                elif type == 1:
                    # 填空题 输入正确答案
                    ele = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/input')
                    for i, e in enumerate(ele):
                        e.send_keys(answer[1][i])
            if answer[0] is not None and (answer[0] > 10 or answer[0] < 1) and type:
                # 获取弹框信息
                res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
                return res

        if desc is not None:
            # 获取输入框
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_elements(By.CLASS_NAME, 'ke-edit-iframe')[1]
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[1].send_keys(desc)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        try:
            # 点击 确定添加
            self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        except Exception as e:
            print(e)
        sleep(1)
        try:
            res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message h3').text
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text

        # 点击 确定
        try:
            self.wd.find_element(By.CSS_SELECTOR, f'.bootstrap-dialog-footer-buttons button:nth-child({opt})').click()
        except selenium.common.exceptions.NoSuchElementException as e:
            print(e)
            self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button').click()

        return res

    def check_textbook(self, type, difflevel, textbook):
        # 创建题目时检查教材版本
        # textbook：[0, 0 ] 0 浙教版 1人教版

        # 点击 题目
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
        # 点击 创建题目
        self.wd.find_element(By.CSS_SELECTOR, '.fa-plus-square-o').click()

        if type is not None:
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_questiontypes"]/label')
            eles[type].click()

        if difflevel is not None:
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_level"]/label')
            eles[difflevel].click()

        for i in textbook:
            # 点击 增加
            self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
            # 点击添加教材
            eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
            eles[i].click()  # 选择 浙教版 或 人教版

        sleep(0.2)

    def edit_question1(self, type=0, difflevel=None, knowleadege=None, textbook=None, content=None, video=None,
                       answer=None, desc=None):
        # 重新编辑
        sleep(1)
        if difflevel is not None:
            eles = self.wd.find_elements(By.XPATH, '//*[@id="btn_group_level"]/label')
            if difflevel < len(eles):
                target = eles[difflevel]
                self.wd.execute_script("arguments[0].click();", target)

        if knowleadege is not None:
            # 点击 选择
            self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]').click()
            # 点击 初中数学左边的三角
            self.wd.find_element(By.XPATH, '//*[@id="ZSD_1_0"]/i').click()

            # 点击 所有章
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[1].click()
            self.wd.find_elements(By.CSS_SELECTOR, 'i.jstree-ocl')[2].click()

            div_elements = self.wd.find_elements(By.CSS_SELECTOR, 'a i.jstree-checkbox:nth-child(1)')[4:]
            for i in range(knowleadege):
                div_elements[i].click()

            # 点击 确定
            self.wd.find_element(By.XPATH, '//*[@id="btn_selectTree_ok"]').click()

        if textbook is not None:
            if textbook == 14:
                # 编号14用例
                # 点击 增加
                self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
                eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
                eles[0].click()  # 选择 浙教版
                nianji = self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_grades_1 label')
                # 强制点击 七年级和八年级
                self.wd.execute_script("arguments[0].click();", nianji[0])
                self.wd.execute_script("arguments[0].click();", nianji[1])

            else:
                for m, e in enumerate(textbook):
                    i, j, k = e
                    # 点击 增加
                    self.wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
                    eles = self.wd.find_elements(By.XPATH, '//*[@id="dropdown_textbookversions"]/li')
                    eles[i].click()  # 选择 浙教版 或 人教版
                    nianji = self.wd.find_elements(By.XPATH,
                                                   f'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[{m + 1}]/table/tbody/tr[1]/td[3]/div//label')
                    # 强制点击
                    self.wd.execute_script("arguments[0].click();", nianji[j])
                    cehao = self.wd.find_elements(By.XPATH,
                                                  f'/html/body/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[{m + 1}]/table/tbody/tr[2]/td[3]/div//label')
                    self.wd.execute_script("arguments[0].click();", cehao[k])  # 选择 册号

        if content is not None:
            # 获取输入框
            # 切换到iframe
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_element(By.CSS_SELECTOR, 'iframe.ke-edit-iframe')
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[0].clear()
            input[0].send_keys(content)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        if video is not None:
            # 点击 选择视频文件
            for i in video:
                self.wd.find_element(By.XPATH, '//*[@id="pick_video_files"]').send_keys(rf'{i}')

        if answer is not None:
            input = self.wd.find_element(By.XPATH, '//*[@id="Question_AnswerNum_text"]')
            input.clear()
            input.send_keys(answer[0])
            if answer[1][0] is not None and 1 <= answer[0] <= 10:
                if type == 0:
                    # 选择题  点击正确答案
                    eles = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/label')
                    if answer[1][0] is not None and len(eles) != 0:
                        # eles[answer[1][0]].click()
                        for i in answer[1]:
                            self.wd.execute_script("arguments[0].click();", eles[i])
                elif type == 1:
                    # 填空题 输入正确答案
                    ele = self.wd.find_elements(By.XPATH, '//*[@id="question_answers"]/input')
                    for i, e in enumerate(ele):
                        e.send_keys(answer[1][i])

        if desc is not None:
            # 获取输入框
            mainWindow = self.wd.current_window_handle
            iframe = self.wd.find_elements(By.CLASS_NAME, 'ke-edit-iframe')[1]
            self.wd.switch_to.frame(iframe)
            input = self.wd.find_elements(By.CSS_SELECTOR, 'body.ke-content')
            input[0].send_keys(desc)
            sleep(0.3)
            self.wd.switch_to.window(mainWindow)

        # 点击确定修改
        self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(0.1)
        res = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message h3').text.strip()
        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@class="bootstrap-dialog-footer-buttons"]//button[3]').click()

        return res

    def del_textbook(self, idx):
        # 需要删除教材的索引 ele=[0,1]

        # 创建作业时  删除教材
        # 找到你想悬浮的元素
        eles = self.wd.find_elements(By.XPATH, '//ul[@role="tablist"]//li')
        num = len(eles)
        for i in idx:
            ele = eles[i]
            # 创建ActionChains对象
            actions = ActionChains(self.wd)
            # 移动鼠标到指定的元素上
            actions.move_to_element(ele).perform()
            ele.find_element(By.TAG_NAME, 'span').click()  # 点击删除x
            # 点击确实
            self.wd.find_element(By.XPATH, '//div[@class="bootstrap-dialog-footer-buttons"]//button[2]').click()

        eles = self.wd.find_elements(By.XPATH, '//ul[@role="tablist"]//li')

        return num, len(eles)

    def mul_questions(self, type, opt, content=None):
        # 删除 type为提醒，0选择1填空，题目内容为content的 题目
        # opt 1 查看
        # opt 2 编辑
        # opt 3 删除
        # opt 4 直接获取内容个数
        sleep(1)
        # 点击题目-搜索题目，
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
        sleep(0.4)
        target = self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/ul/a[2]/li/i')
        self.wd.execute_script("arguments[0].click();", target)
        # 点击 按知识点
        sleep(1)
        target = self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]')
        self.wd.execute_script("arguments[0].click();", target)
        sleep(0.4)
        # 点击 题目类型
        self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_questiontypes label')[type].click()
        sleep(0.4)
        # 点击 我创建的
        self.wd.find_element(By.XPATH, '//*[@id="onlysearchmine"]').click()
        sleep(1)
        # 查找
        ele = get_element_with_retry(self.wd, By.CSS_SELECTOR, 'div.div-search-result-one-text', True)
        # ele = self.wd.find_elements(By.CSS_SELECTOR, 'div.div-search-result-one-text')
        num = len(ele)

        if opt == 4:
            return num

        sleep(0.4)
        mainWindow = self.wd.current_window_handle
        wait = WebDriverWait(self.wd, 10)
        # 获取所有题目卡片
        for attempt in range(2):  # 重试1次
            try:
                cons = get_element_with_retry(self.wd, By.CSS_SELECTOR, 'div.div-search-result-one-text', True)
                cons = [c.text.strip() for c in cons]
                eles = self.wd.find_elements(By.CSS_SELECTOR, f'#serach_result_table label:nth-child({opt})')
                for i, c in enumerate(cons):
                    if c == content:
                        sleep(0.3)  # 避免过快操作
                        eles = self.wd.find_elements(By.CSS_SELECTOR, f'#serach_result_table label:nth-child({opt})')
                        self.wd.execute_script("arguments[0].click();", eles[i])
                        print('点击所需内容按键')
                        sleep(1)
                        break  # ✅ 只退出当前 for-i 循环，不 return
                else:
                    continue  # 没找到匹配项，进入下一轮 attempt
                break  # ✅ 找到了并点击了，退出 retry 循环
            except StaleElementReferenceException:
                print("元素失效，重试中...")
                sleep(0.5)  # 等待页面稳定

        if opt == 3:
            # 删除，点击确定
            # self.wd.find_element(By.CSS_SELECTOR, 'div.bootstrap-dialog-footer-buttons button.btn-primary').click()
            # self.wd.find_element(By.XPATH, '//*[@class="bootstrap-dialog-footer"]//button[2]').click()
            try:
                btn = get_element_with_retry(self.wd, By.XPATH, '//*[@class="bootstrap-dialog-footer"]//button[2]')
                btn.click()
            except Exception as e:
                print(e)
            sleep(1)
            ele = self.wd.find_elements(By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)')
            return len(ele) == num - 1

        elif opt == 1:
            # 查看
            # 切换窗口
            # 所有窗口的句柄
            allHandles = self.wd.window_handles
            self.wd.switch_to.window(allHandles[-1])
            sleep(0.5)
            res = []  # type,diff,content,ans,video,textbook
            res.append(self.wd.find_element(By.ID, 'label_questiontype').text.strip())
            res.append(self.wd.find_element(By.ID, 'label_questionlevel').text.strip())
            res.append(self.wd.find_element(By.ID, 'Question_content_text').text.strip())
            ans = None
            if type == 1:
                eles = self.wd.find_elements(By.XPATH, '//table//td[2]//div//span')
                ans = [i.text.strip() for i in eles]
            elif type == 0:
                ele = self.wd.find_element(By.XPATH, '//*[@id="question_answers"]').text.strip()
                ans = ele.split()
            res.append(ans)
            # 视频
            video = self.wd.find_elements(By.XPATH, '//*[@id="tbody_question_body"]/tr[3]/td[2]')
            res.append(video)
            # 知识点 textbook
            textbook = []
            lis = self.wd.find_elements(By.CSS_SELECTOR, 'div.panel-body > ul.nav-tabs > li')
            for li in lis[:-1]:
                li.click()  # 点击
                sleep(0.4)
                group = self.wd.find_elements(By.XPATH,
                                              '//*[@id="sgt_tab_content"]//*[@class="tab-pane active"]//td[2]//div')
                group = [i.text.strip() for i in group]
                textbook.append(group)
            res.append(textbook)
            INFO(f'e:{res}')
            self.wd.close()
            sleep(0.1)
            self.wd.switch_to.window(mainWindow)
            return res

        elif opt == 2:
            # 编辑
            pass

    def del_all_questions(self, flag=False, type=0):
        # 删除所有题目

        if flag:
            # 点击题目-搜索题目，
            self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]').click()
            sleep(0.5)
            self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/ul/a[2]/li/i').click()
            # 点击 按知识点
            sleep(1)
            self.wd.find_element(By.XPATH, '//*[@id="btn_choose_knowledgetree"]').click()
            sleep(0.5)
            # 点击 题目类型
            self.wd.find_elements(By.CSS_SELECTOR, '#btn_group_questiontypes label')[type].click()
            sleep(0.5)
            # 点击 我创建的
            self.wd.find_element(By.XPATH, '//*[@id="onlysearchmine"]').click()
            sleep(0.5)

        # 查询题目页面
        while True:
            # 查询题目页面

            eles = get_element_with_retry(self.wd, By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)', True)
            # eles = self.wd.find_elements(By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)')
            if not eles:  # 如果没有元素了，退出循环
                break
            try:
                eles = get_element_with_retry(self.wd, By.CSS_SELECTOR, '#serach_result_table label:nth-child(3)', True)
                eles[0].click()  # 点击删除（删除第一个元素）
                sleep(0.5)
                # 点击确定
                self.wd.find_element(By.XPATH, '//*[@class="bootstrap-dialog-footer"]//button[2]').click()
                sleep(1)
            except Exception as e:
                INFO(e)

    def get_result_acc(self):
        # 查看学生完成作业情况
        # 点击 “已发布作业”
        self.wd.find_element(By.CSS_SELECTOR, 'span.badge-blue').click()
        # 点击 完成情况
        self.wd.find_element(By.CSS_SELECTOR, 'table.table td:nth-child(5)').click()
        sleep(0.5)
        # 获取信息
        mes_teacher = self.wd.find_element(By.CSS_SELECTOR, 'table td:nth-child(3) > p').text
        acc1 = float(mes_teacher.split('%')[0][3:]) / 100
        self.wd.close()
        return acc1

    def view_result(self, taskname, completed=None, notcompleted=None, refresh=None):
        # 老师查看结果
        res = {}
        # 点击已发布作业

        # self.wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]').click()
        opt = get_element_with_retry(self.wd, By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]')
        opt.click()
        sleep(1)

        taskname_eles = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr/td[3]')
        for i, t_ele in enumerate(taskname_eles):
            if t_ele.text.strip() == taskname:
                # 找到taskname，点击 完成情况
                wcqks = self.wd.find_elements(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr/td[5]')
                wcqks[i].click()
                sleep(0.2)

        # 筛选已完成
        if completed is not None:
            # 点击 全部
            self.wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[1]/div[1]/div/span/button[1]').click()
            sleep(1)
            # 点击已完成
            self.wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[1]/div[1]/div/span/ul/li[2]/a').click()
            sleep(1)

        # 筛选未完成
        if notcompleted is not None:
            # 点击 全部
            self.wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[1]/div[1]/div/span/button[1]').click()
            sleep(1)
            # 点击已完成
            self.wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[1]/div[1]/div/span/ul/li[3]/a').click()
            sleep(1)

        if refresh is not None:
            # 点击 刷新按钮
            self.wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[1]/div/button[2]').click()
            sleep(1)

        names = self.wd.find_elements(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[2]/table/tbody/tr/td[1]')
        for i in range(len(names)):
            names = self.wd.find_elements(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[2]/table/tbody/tr/td[1]')
            sub_time = self.wd.find_elements(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[2]/table/tbody/tr/td[2]')
            acc = self.wd.find_elements(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[2]/table/tbody/tr/td[3]')
            sleep(0.5)
            res[names[i].text.strip()] = sub_time[i].text.strip(), acc[i].text.strip()

        return res

    def query_homework(self, revokenum):
        # 查询作业
        # 点击已发布作业
        sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]').click()
        sleep(1)

        num = len(self.wd.find_elements(By.XPATH, '//tbody//td[6]/a'))

        i = 0
        while True:
            if i == revokenum:
                break
            revoke_btns = get_element_with_retry(self.wd, By.XPATH, '//tbody//td[6]/a', True)
            revoke_btns[0].click()
            sleep(1)
            i += 1
            # 点击 确定
            self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button:nth-child(2)').click()
            sleep(1)
        CHECK_POINT('检查撤销后，当前页面显示是否一致',
                    num - revokenum == len(self.wd.find_elements(By.XPATH, '//tbody//td[6]/a')))
        return num - revokenum

    def query_homework1(self, starttime=None, endtime=None):
        # 查询作业
        # 点击已发布作业
        self.wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]').click()
        sleep(0.2)

        if starttime is not None:
            start_input = self.wd.find_element(By.XPATH, '//*[@id="createTimeAfter"]')
            start_input.send_keys(starttime)

        if endtime is not None:
            end_input = self.wd.find_element(By.XPATH, '//*[@id="createTimeBefore"]')
            end_input.send_keys(endtime)
        sleep(0.2)

        # 点击搜索
        self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[2]/button').click()
        time_items = len(self.wd.find_elements(By.XPATH, '//tbody//td[2]'))
        sleep(0.2)
        return time_items

    def edit_homework(self, taskname, idx, move=None):
        # 编辑作业
        # move up 上移  down  下移
        # 第i个题目，i从1开始,所以用i-1

        # 点击已发布作业
        self.opt_homework('已发布作业')

        names = self.wd.find_elements(By.XPATH, '//tbody//td[3]')
        names = [n.text.strip() for n in names]

        for i, name in enumerate(names):
            if name == taskname:
                # 找到taskname，点击编辑按钮
                edit_btns = self.wd.find_elements(By.XPATH, '//tbody//td[3]//i')
                edit_btns[i].click()
        sleep(1)

        contents = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]//div/div[2]/p[1]')
        contents = [c.text.strip() for c in contents]

        res = None
        if move == 'up':
            moveup_btns = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]//div[3]/div/label[3]')
            moveup_btns[idx - 1].click()
            sleep(1)
            contents1 = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]//div/div[2]/p[1]')
            contents1 = [c.text.strip() for c in contents1]
            i = idx - 1
            j = len(contents1) - 1 if idx == 1 else idx - 2
            res = contents[i] == contents1[j]

        if move == 'down':
            movedown_btns = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]//div[3]/div/label[4]')
            movedown_btns[idx - 1].click()
            sleep(1)
            contents1 = self.wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]//div/div[2]/p[1]')
            contents1 = [c.text.strip() for c in contents1]
            i = idx - 1
            j = 0 if idx == len(contents1) else idx
            res = contents[i] == contents1[j]

        # 点击 确定修改
        self.wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(1)
        # 点击 暂不发布
        self.wd.find_element(By.XPATH, '//button[text()="暂不发布"]').click()
        sleep(1)
        return res

    def edit_taskdec(self, taskname, dec=None, time1=None):
        # 编辑任务描述

        # 点击已发布作业
        self.opt_homework('已发布作业')

        names = self.wd.find_elements(By.XPATH, '//tbody//td[3]')
        names = [n.text.strip() for n in names]

        for i, name in enumerate(names):
            if name == taskname:
                # 找到任务描述，点击编辑按钮
                edit_btns = self.wd.find_elements(By.XPATH, '//tbody//td[4]//i')
                edit_btns[i].click()
        sleep(0.3)

        if dec is not None:
            dec_element = self.wd.find_element(By.XPATH, '//*[@id="modal-task_modify"]/div[2]/div/div[2]/textarea')
            dec_element.clear()
            dec_element.send_keys(dec)

        if time1 is not None:
            time1_element = self.wd.find_element(By.XPATH, '//*[@id="modal-task_modify"]/div[2]/div/div[2]/input')
            time1_element.clear()
            time1_element.send_keys(time1)

        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="modal-task_modify"]/div[2]/div/div[3]/button[2]').click()

        if dec is None and time1 is None:
            mes = self.wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
            CHECK_POINT('提示消息', mes == '您没有修改任务信息')
            # 点击确定
            self.wd.find_element(By.XPATH,
                                 '//*[@class="bootstrap-dialog-footer-buttons"]//button[text()="确定"]').click()

        sleep(0.3)
        # 重新获取dec和时间
        cons = self.wd.find_element(By.XPATH, '//tbody//td[4]').text
        dec1 = cons.split('(')[0]
        time2 = cons.split('(')[1].split('分')[0]
        if dec is not None:
            CHECK_POINT('修改后的任务描述是否正确', dec1 == dec)
        if time1 is not None:
            CHECK_POINT('修改后的完成时间是否正确', str(time1) == time2)

    def query_created_homework(self):
        # 查询已创建作业个数

        self.opt_homework('已创建作业')
        eles = self.wd.find_elements(By.CSS_SELECTOR, 'div.div-search-result-one-text')
        return len(eles)

    def query_created_homework1(self, searchitem=None):
        # 查询已创建作业个数

        self.opt_homework('已创建作业')

        if searchitem is not None:
            searchinput = self.wd.find_element(By.XPATH, '//*[@id="srch-term"]')
            searchinput.clear()
            searchinput.send_keys(searchitem)
            # 点击搜索
            self.wd.find_element(By.XPATH, '//*[@id="btn_search_exams"]').click()
            sleep(0.3)

        eles = self.wd.find_elements(By.CSS_SELECTOR, 'div.div-search-result-one-text')
        return len(eles)


teacher_ui = TeacherUI()
