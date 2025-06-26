from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By
from cfg.cfg import *
from time import sleep


class TeacherUI:

    def open_browser(self):
        INFO('打开浏览器')
        options = webdriver.ChromeOptions()
        os.environ['SE_DRIVER_MIRROR_URL'] = 'https://cdn.npmmirror.com/binaries/chrome-for-testing'
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)

    def login(self, username, password='888888'):
        # 登录
        self.wd.get(g_ui_url_teacher)
        self.wd.find_element(By.ID, 'username').send_keys(username)
        self.wd.find_element(By.ID, 'password').send_keys(password)
        # 点击登录
        self.wd.find_element(By.ID, 'submit').click()

    def publish_homework(self, taskname='作业1'):
        # 发布作业
        # 点击作业
        self.wd.find_element(By.CSS_SELECTOR, 'div.main-menu li:nth-child(5) > a').click()
        # 创建作业
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
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
        ############
        options = self.wd.find_elements(By.CSS_SELECTOR, '.div-search-question-button-bar label:nth-child(2)')
        # 检查是否能够找到某个 iframe 中的元素（例如一个按钮）
        for i in range(3):
            options[i].click()
        # 点击确定
        self.wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
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
        CHECK_POINT('是否新建作业成功', '新建作业成功' == mes11)
        # 弹框点击  将作业发布给学生，不能直接定位id，id是自动生成的
        self.wd.find_element(By.XPATH, '//button[text()="发布给学生"]').click()

        # 设置主窗口
        mainWindow = self.wd.current_window_handle
        # 切换至新窗口
        # 所有窗口的句柄
        allHandles = self.wd.window_handles
        # 进入新窗口
        self.wd.switch_to.window(allHandles[-1])
        sleep(0.5)

        # 全选
        self.wd.find_element(By.CSS_SELECTOR, "a.ng-scope").click()
        # self.wd.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div[1]/a").click()
        # self.wd.find_element(By.XPATH, "//a[contains(text(), '全选')]").click()
        # 点击  确定下发
        self.wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        sleep(0.5)
        # 点击 确定
        self.wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        sleep(0.5)
        # 提示窗口 点击 确定
        self.wd.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div/button").click()
        # 切换回主窗口
        self.wd.switch_to.window(mainWindow)
        sleep(0.5)
        # 点击 发布给学生
        self.wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[4]').click()

        # 主页查看是否发布作业成功
        # 点击主页
        self.wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/a[1]/li').click()
        # 已发布作业
        self.wd.find_element(By.XPATH, '//*[@id="home_div"]/div/div/div[2]/div[1]/div[2]/a/span').click()
        taskname1 = self.wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr[1]/td[3]')
        CHECK_POINT('是否发布作业成功', taskname == taskname1.text)
        self.wd.close()

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


t_ui = TeacherUI()
