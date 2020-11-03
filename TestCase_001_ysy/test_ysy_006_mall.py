import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约--商城')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
@allure.severity('critical')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
class TestYsy006Mall(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.story('商城首页')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('mall_001_mall_index'))
    def test_mall_001_mall_index(self,case):
        """
            用例描述：首页--访问状态
        """
        self.new.test_case_method(case, 'get')
