import xlrd
from Conf import Config
from Common import operate_json

class ExcelHandler(object):
    '''
    关于Excel表的操作
    '''
    oper_j = operate_json.OperateJson()
    con = Config.Config()

    def get_excel_data(self, case_desc):
        '''
        过滤excel中不必要的数据
        :param case_desc: 通过excel中的case_description来过滤用例
        :return:
        '''
        # 获取到book对象
        book = xlrd.open_workbook(Config.TEST_CASE_PATH)
        sheet = book.sheet_by_index(0)
        # sheet = book.sheet_by_name('接口自动化用例')
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            if case_desc in sheet.row_values(i):
                l.append(dict(zip(title, sheet.row_values(i))))
        return l


if __name__ == '__main__':
    eh = ExcelHandler()
    print(eh.get_excel_data('login_01_get_verifycode'))

