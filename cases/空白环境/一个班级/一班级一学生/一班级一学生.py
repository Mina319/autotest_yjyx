from hytest import CHECK_POINT, STEP
from lib.api.Teacher import *
from lib.api.Student import *
from cfg.cfg import *
from lib.api.SClass import *
from lib.ui.TeacherUI import *


# web功能

class Case_tc005002:
    name = '老师登录2-API-tc005002'

    def teststeps(self):
        STEP(1, '创建老师')
        subject = '初中数学'
        username, realname, subjectid, classlist, phonenumber, email, idcardnumber = \
            'liubenben', '刘本本', subjectToId[subject], [{"id": getFirstClass()["id"]}], '13466613456', \
            'liubenben@163.com', '3209251988090987955'
        r = teacher.add_teacher(username=username, realname=realname, subjectid=subjectid,
                            classlist=classlist, phonenumber=phonenumber, email=email,
                            idcardnumber=idcardnumber)
        self.tid = r.json()["id"]
        CHECK_POINT('是否创建老师成功', r.json()["retcode"] == 0)

        STEP(2, '登录web系统')
        t_ui.open_browser()
        t_ui.login(username=username)
        INFO('检查 学校、姓名、学科、金币、已发布微课、已发布作业 的信息是否正确')
        wd = GSTORE['wd']
        sleep(2)
        infos_ele = wd.find_elements(By.XPATH, '//table//td[2]/a')
        infos = [e.text for e in infos_ele]
        school1, name1, subject1, goldcoin = infos
        goldcoin = 0 if goldcoin == '' else int(goldcoin)
        infos_ele1 = wd.find_elements(By.XPATH, '//*[@class="col-md-12"]//a/h2/strong')
        infos1 = [int(e.text) for e in infos_ele1]
        microlessons, homework = infos1
        sleep(1)
        SELENIUM_LOG_SCREEN(wd, width='70%')

        CHECK_POINT('检查信息是否正确', name1 == realname and subject1 == subject and goldcoin == 0
                    and microlessons == 0 and homework == 0 and school1 == g_school)

        STEP(3, '点击班级学生')
        # 点击班级情况
        wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]').click()
        # 点击班级学生
        wd.find_element(By.XPATH, '//*[@class="main-menu"]//li[4]//li/span').click()
        sleep(1)
        # 点击 年级
        wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[1]/a').click()
        sleep(2)

        stuName = getFirstStudent()["realname"]
        # 学生人数
        stuNum = wd.find_element(By.CSS_SELECTOR, '.panel-heading span')
        name = wd.find_element(By.CSS_SELECTOR, '.panel-body > table tbody td:nth-child(2) > span')

        SELENIUM_LOG_SCREEN(wd, width='70%')
        CHECK_POINT('学生列表是否为空', int(stuNum.text) == 1 and
                    stuName == name.text)

    def teardown(self):
        # 删掉老师
        teacher.del_teacher(self.tid)
