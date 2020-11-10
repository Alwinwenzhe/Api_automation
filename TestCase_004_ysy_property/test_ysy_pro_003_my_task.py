import allure, pytest, os, sys
from Common import new_tool_a
from Common import ExcelHandler

@allure.feature('一生约物业app')
@allure.severity('blocker')
@allure.story('首页--任务列表')
class TestYsyPro002MyTask(object):

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step('公区报修列表')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_009_get_Repair_List_1'))
    def test_ysy_pro_009_get_Repair_List_1(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')

    @allure.step('专区报修列表')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_010_get_Repair_List'))
    def test_ysy_pro_010_get_Repair_List(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')

    @allure.step('七牛服务')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_011_qiniu_token'))
    def test_ysy_pro_011_qiniu_token(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'get')

    @allure.step('我的应用--报事报修--公区报修')
    @pytest.mark.parametrize('case', excel.get_excel_data('ysy_pro_012_public_AreaRepair_publish'))
    def test_ysy_pro_012_public_AreaRepair_publish(self, case):
        """
            用例描述：物业app密码登录
        """
        self.new.test_case_method(case, 'post')