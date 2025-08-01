from time import sleep
from lib.ui.TeacherUI import teacher_ui
from lib.webui import *


class TC_HOMEWORK_001:
    name = '创建作业1_TC_HOMEWORK_001'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='')
        teacher_ui.wd.quit()


class TC_HOMEWORK_002:
    name = '创建作业2_TC_HOMEWORK_002'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname=None)
        teacher_ui.wd.quit()


class TC_HOMEWORK_003:
    name = '创建作业3_TC_HOMEWORK_003'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='z', mes='作业名称长度应为2~100个字符')

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('z')
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_004:
    name = '创建作业4_TC_HOMEWORK_004'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='zz', mes='新建作业成功')

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('zz')
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_005:
    name = '创建作业5_TC_HOMEWORK_005'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功')

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_006:
    name = '创建作业6_TC_HOMEWORK_006'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*100, mes='新建作业成功')

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*100)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_007:
    name = '创建作业7_TC_HOMEWORK_007'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        try:
            teacher_ui.publish_homework(taskname='哈'*101, mes='新建作作业名称长度应为2~100个字符')
        finally:
            teacher_ui.wd.quit()


class TC_HOMEWORK_008:
    name = '创建作业8_TC_HOMEWORK_008'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈sd δΔsqt / ** ^%&$#@!~:"?>< ', mes='新建作业成功')

    def teardown(self):
        # 删除创建的作业
        try:
            teacher_ui.opt_homework('已创建作业')
            res = teacher_ui.del_homework_by_taskname('哈sd δΔsqt / ** ^%&$#@!~:"?>< ')
            print(f'是否删除作业{res}')
        finally:
            teacher_ui.wd.quit()


class TC_HOMEWORK_009:
    name = '创建作业9_TC_HOMEWORK_009'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework1(taskname='作业1', mes='请添加题目到作业')
        teacher_ui.wd.quit()


class TC_HOMEWORK_010:
    name = '创建作业10_TC_HOMEWORK_010'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功')
        STEP(3, '查看已发布作业')
        teacher_ui.opt_homework('已发布作业')
        num = teacher_ui.get_num_of_published_homework()
        CHECK_POINT('检验已发布作业是否不存在', num == 0)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_011:
    name = '创建作业11_TC_HOMEWORK_011'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*50, mes='选题数量大于100', num=101)
        teacher_ui.wd.quit()


class TC_HOMEWORK_012:
    name = '创建作业12_TC_HOMEWORK_012'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=1)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_013:
    name = '创建作业13_TC_HOMEWORK_013'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=50)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_014:
    name = '创建作业14_TC_HOMEWORK_014'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '七年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_015:
    name = '创建作业15_TC_HOMEWORK_015'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '七年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_016:
    name = '创建作业16_TC_HOMEWORK_016'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '八年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_017:
    name = '创建作业17_TC_HOMEWORK_017'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '八年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_018:
    name = '创建作业18_TC_HOMEWORK_018'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '九年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_019:
    name = '创建作业19_TC_HOMEWORK_019'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '浙教版', '九年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_020:
    name = '创建作业20_TC_HOMEWORK_020'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '七年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_021:
    name = '创建作业21_TC_HOMEWORK_021'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '七年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_022:
    name = '创建作业22_TC_HOMEWORK_022'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '八年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_023:
    name = '创建作业23_TC_HOMEWORK_023'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '八年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_024:
    name = '创建作业24_TC_HOMEWORK_024'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '九年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_025:
    name = '创建作业25_TC_HOMEWORK_025'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '选择题', '人教版', '九年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_026:
    name = '创建作业26_TC_HOMEWORK_026'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '七年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_027:
    name = '创建作业27_TC_HOMEWORK_027'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '七年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_028:
    name = '创建作业28_TC_HOMEWORK_028'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '八年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_029:
    name = '创建作业29_TC_HOMEWORK_029'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '八年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_030:
    name = '创建作业30_TC_HOMEWORK_030'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '九年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_031:
    name = '创建作业31_TC_HOMEWORK_031'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '浙教版', '九年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_032:
    name = '创建作业32_TC_HOMEWORK_032'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '七年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_033:
    name = '创建作业33_TC_HOMEWORK_033'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '七年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_034:
    name = '创建作业34_TC_HOMEWORK_034'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '八年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=1, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_035:
    name = '创建作业35_TC_HOMEWORK_035'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '八年级', '下册', None, None]
        try:
            teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=1, filter=f)
        finally:
            teacher_ui.wd.quit()

    def teardown(self):
        # 删除创建的作业
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_036:
    name = '创建作业36_TC_HOMEWORK_036'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '九年级', '上册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_037:
    name = '创建作业37_TC_HOMEWORK_037'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按章节', '填空题', '人教版', '九年级', '下册', None, None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_038:
    name = '创建作业38_TC_HOMEWORK_038'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '选择题', None, None, None, '简单', None]
        teacher_ui.publish_homework(taskname='哈'*50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈'*50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_039:
    name = '创建作业39_TC_HOMEWORK_039'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '选择题', None, None, None, '中等', None]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_040:
    name = '创建作业40_TC_HOMEWORK_040'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '选择题', None, None, None, '较难', None]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_041:
    name = '创建作业41_TC_HOMEWORK_041'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '填空题', None, None, None, '简单', None]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_042:
    name = '创建作业42_TC_HOMEWORK_042'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '填空题', None, None, None, '中等', None]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_043:
    name = '创建作业43_TC_HOMEWORK_043'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '填空题', None, None, None, '较难', None]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_044:
    name = '创建作业44_TC_HOMEWORK_044'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=10)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()


class TC_HOMEWORK_045:
    name = '创建作业45_TC_HOMEWORK_045'

    def teststeps(self):
        STEP(1, '老师登录web系统')
        teacher_ui.open_browser()
        teacher_ui.login(username='zhangming')
        STEP(2, '创建作业')
        f = ['按知识点', '选择题', None, None, None, '较难', 1]
        teacher_ui.publish_homework(taskname='哈' * 50, mes='新建作业成功', num=2, filter=f)

    def teardown(self):
        # 删除创建的作业
        teacher_ui.opt_homework('已创建作业')
        res = teacher_ui.del_homework_by_taskname('哈' * 50)
        print(f'是否删除作业{res}')
        teacher_ui.wd.quit()



