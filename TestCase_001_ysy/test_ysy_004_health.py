import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler

@allure.feature('健康')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
@allure.severity('critical')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
class TestYsy004Health(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.story('添加成員步數')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('health_001_addMenberStep'))
    def test_invitation_001_addMenberStep(self,case):
        """
            用例描述：添加成员步数，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'post')
