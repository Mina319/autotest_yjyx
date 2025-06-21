

class MySignalHandler:
    TEST_RET_COL_NO = 5  # 测试结果在用例excel文件中的列数
    path = r'D:\tools\projects\autotest_yjyx\log\测试用例.xlsm'

    def __init__(self):
        self.caseNum2Row = {}  # 用例编号->行数 表
        self.getCaseNum2RowInExcel()

        # 执行 pip install pypiwin32 确保安装了 win32com 所在的库
        import win32com.client
        self.excel = win32com.client.Dispatch("Excel.Application")
        self.excel.Visible = True
        self.workbook = self.excel.Workbooks.Open(self.path)

    def getCaseNum2RowInExcel(self):
        """
        得到Excel 中用例 编号对应的行数，方便填写测试结果
        """
        import xlrd
        book = xlrd.open_workbook(self.path)

        for sheet in book.sheets():
            sheet_name = sheet.name
            if sheet_name == 'stat':
                continue
            # 用例编号所在列
            caseNumbers = sheet.col_values(colx=3)

            for row, cn in enumerate(caseNumbers):
                if 'tc' in cn:
                    self.caseNum2Row[cn] = (sheet_name, row + 1)  # 保存sheet名和行号

        print(self.caseNum2Row)

    def case_result(self, case):
        """
        case_result 是 每个用例执行结束 ，会调用的函数

        @param case: 用例类 实例
        """

        # 找到对应的测试用例在excel中的行数
        print(case.name)
        caseNo = case.name.split('-')[-1]
        print(caseNo)
        sheet_name, row_num = self.caseNum2Row[caseNo]
        self.sheet = self.workbook.Sheets(sheet_name)
        self.sheet.Activate()
        cell = self.sheet.Cells(row_num, self.TEST_RET_COL_NO)

        self.excel.WindowState = -4137
        self.excel.Visible = True
        try:
            if self.excel.ActiveWindow:
                window = self.excel.ActiveWindow
                window.ScrollRow = row_num - 2
        except Exception as e:
            print(f"设置ScrollRow失败: {e}")

        if case.execRet == 'pass':
            cell.Value = 'pass'
            cell.Font.Color = 0xBF00  # 绿色
        else:
            cell.Font.Color = 0xFF  # 红色
            if case.execRet == 'fail':
                cell.Value = 'fail'
            elif case.execRet == 'abort':
                cell.Value = 'abort'

    def test_end(self, runner):
        """
        test_end 是 整个测试执行完 ，会调用的函数

        @param runner :  hytest runner 对象
               runner.case_list:  列表，里面包含了所有用例类实例
        """
        for case in runner.case_list:
            print(f'{case.name} --- {case.execRet}')


# 注册这个类的实例 为一个 hytest 信号处理对象
from hytest import signal

signal.register(MySignalHandler())

