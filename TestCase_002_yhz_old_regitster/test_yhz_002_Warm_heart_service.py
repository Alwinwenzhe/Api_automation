import allure, pytest, sys
sys.path.append("D:\Job\python\Script\Api_automation")  #增加系统寻包路径
from Common import Consts
from Common import new_tool_a
from Common import ExcelHandler
from Common import req_reload
from Common import Assert

@allure.feature('老人登记_暖心服务')
@allure.severity('blocker')
class TestYhz002WarmHearService:

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()
    reqe = req_reload.ReqReload()
    test = Assert.Assertions()

    @allure.story('敬老送餐--获取老人餐食要求及禁忌')
    @pytest.mark.parametrize('case', excel.get_excel_data('yhz_001_get_people_mark_list'))
    def test_yhz_001_get_people_mark_list(self, case):
        """
            用例描述：敬老送餐--获取老人餐食要求及禁忌
        """
        self.new.test_case_method(case, 'get')

    @allure.story('送餐记录')
    @pytest.mark.parametrize('case', excel.get_excel_data('yhz_002_get_send_food_record_list'))
    def test_yhz_002_get_send_food_record_list(self, case):
        """
            用例描述：送餐记录
        """
        self.new.test_case_method(case, 'get')