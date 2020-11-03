import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('小区服务')
@allure.story('物业缴费')  # allure.story  用于定义被测功能的用户场景，即子功能点
@allure.severity('blocker')
class TestYsy009BiotopeFee(object):

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step("获取业主房屋资源列表")
    @pytest.mark.parametrize('case', excel.get_excel_data('fee_001_fee_resource'))
    def test_fee_001_fee_resource(self, case):
        self.new.test_case_method(case, 'get')

    @allure.step("待缴费列表")
    @pytest.mark.parametrize('case', excel.get_excel_data('fee_002_fee_stayFee'))
    def test_fee_002_fee_stayFee(self, case):
        self.new.test_case_method(case, 'get')

    @allure.step("历史缴费")
    @pytest.mark.parametrize('case', excel.get_excel_data('fee_003_fee_history'))
    def test_fee_003_fee_history(self, case):
        self.new.test_case_method(case, 'get')

    @allure.step("立即缴费")
    @pytest.mark.parametrize('case', excel.get_excel_data('fee_004_immediately_Fee'))
    def test_fee_004_immediately_Fee(self, case):
        self.new.test_case_method(case, 'post')

    @allure.story('物业预缴')
    @allure.step("预存缴费")
    @pytest.mark.parametrize('case', excel.get_excel_data('fee_005_get_prepay_resource_info'))
    def test_fee_004_immediately_Fee(self, case):
        self.new.test_case_method(case, 'get')