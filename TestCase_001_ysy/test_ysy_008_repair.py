import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('小区服务--报事报修')
@allure.story('报事报修')  # allure.story  用于定义被测功能的用户场景，即子功能点
@allure.severity('blocker')
class TestYsy007Myself(object):
    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step("获取报修类型")
    @pytest.mark.parametrize('case', excel.get_excel_data('repair_001_favorite_And_Types'))
    def test_repair_001_favorite_And_Types(self, case):
        """
            用例描述：获取报修类型，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'get')

    @allure.step("提交报修")
    @pytest.mark.parametrize('case', excel.get_excel_data('repair_002_repair_publish'))
    def test_repair_002_repair_publish(self, case):
        """
            用例描述：报修历史记录
        """
        self.new.test_case_method(case, 'post')

    @allure.step("报修历史记录")
    @pytest.mark.parametrize('case', excel.get_excel_data('repair_003_cur_Repair_List'))
    def test_repair_003_cur_Repair_List(self, case):
        """
            用例描述：报修历史记录
        """
        self.new.test_case_method(case, 'get')

    @allure.step("业主取消报修订单")
    @pytest.mark.parametrize('case', excel.get_excel_data('repair_004_repair_userCancel'))
    def test_repair_004_repair_userCancel(self, case):
        """
            用例描述：报修历史记录
        """
        self.new.test_case_method(case, 'post')