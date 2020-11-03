import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约物业app')
@allure.severity('blocker')
@allure.story('首页')
class TestYsyPro002Home(object):

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step('抢单状态更改')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_001_receive_setting'))
    def test_ysy_pro_001_receive_setting(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')

    @allure.step('抢单状态获取')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_002_receive_setting_info'))
    def test_ysy_pro_002_receive_setting_info(self,case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('体温检测')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_003_epidemic_Info'))
    def test_ysy_pro_003_epidemic_Info(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.story('签到记录')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_003_sign_find_employees_sign'))
    def test_ysy_pro_003_sign_find_employees_sign(self, case):
        """
            用例描述:根据员工Id获取当天最近一次签到记录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('顶部banner宣传')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_004_adImg_list_biotopeId'))
    def test_ysy_pro_004_adImg_list_biotopeId(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('顶部banner宣传')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_005_get_Property_Info'))
    def test_ysy_pro_005_get_Property_Info(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('我的任务')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_006_repair_find_Index_Order_Num'))
    def test_ysy_pro_006_repair_find_Index_Order_Num(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('访客登记')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_008_Health_Check_visitAdd'))
    def test_ysy_pro_008_Health_Check_visitAdd(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')