import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约物业app')
@allure.severity('blocker')
@allure.story('登录')
class TestYsyPro001Login(object):

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step('登录')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_001_user_login'))
    def test_ysy_pro_001_user_login(self,case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')

    @allure.step('我的')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_002_myself'))
    def test_ysy_pro_002_myself(self, case):
        """
            用例描述:我的--我的个人资料
        """
        self.new.test_case_method(case, 'get')

    @allure.step('忘记密码')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_002_myself'))
    def test_ysy_pro_002_myself(self, case):
        """
            用例描述:我的--我的个人资料
        """
        self.new.test_case_method(case, 'get')