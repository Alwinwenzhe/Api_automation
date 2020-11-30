import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约--首頁--智慧门禁')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
@allure.severity('critical')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
@allure.story('智慧门禁')
class TestYsy010HomeDoor(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step("人像设备是否支持")
    @pytest.mark.parametrize('case', excel.get_excel_data('home_door_001_get_Biotope_Face'))
    def test_home_door_001_get_Biotope_Face(self, case):
        """
            用例描述：首页-智慧门禁--人像管理--人像列表
        """
        self.new.test_case_method(case, 'get')

    @allure.step("人像列表数据")
    @pytest.mark.parametrize('case', excel.get_excel_data('home_door_002_get_Face_List'))
    def test_home_door_002_get_Face_List(self,case):
        """
            用例描述：首页-智慧门禁--人像管理--人像列表
        """
        self.new.test_case_method(case, 'get')

    @allure.step("申请理由")
    @pytest.mark.parametrize('case', excel.get_excel_data('home_door_003_get_Face_Apply_Reason'))
    def test_home_door_003_get_Face_Apply_Reason(self, case):
        """
            用例描述：首页-智慧门禁--人像管理--人像列表
        """
        self.new.test_case_method(case, 'get')

    @allure.step("扫码开门")
    @pytest.mark.parametrize('case', excel.get_excel_data('home_door_004_gated_open_Code'))
    def test_home_door_004_gated_open_Code(self, case):
        """
            用例描述：首页-智慧门禁--人像管理--扫码开门
        """
        self.new.test_case_method(case, 'post')


    @allure.step("远程开门")
    @pytest.mark.parametrize('case', excel.get_excel_data('home_door_005_device_door_open'))
    def test_home_door_005_device_door_open(self, case):
        """
            用例描述：首页-智慧门禁--人像管理--远程开门
        """
        self.new.write_data_to_json()  # 初始化相关数据
        self.new.test_case_method(case, 'post')







