import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约--我的')
@allure.severity('blocker')
class TestYsy007Myself(object):
    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.story('我的信息')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('myself_001_user_info'))
    def test_myself_001_user_info(self, case):
        """
            用例描述：获取验证码
        """
        self.new.test_case_method(case, 'get')