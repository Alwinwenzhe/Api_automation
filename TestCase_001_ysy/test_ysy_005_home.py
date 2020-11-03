import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler


@allure.feature('一生约--首頁')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
@allure.severity('critical')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；

class TestYsy005Home(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.story('今日推荐')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('home_001_today_Recommend'))
    def test_home_001_today_Recommed(self,case):
        """
            用例描述：首页--今日推荐
        """
        self.new.test_case_method(case, 'get')


    @pytest.mark.parametrize('case', excel.get_excel_data('home_002_topic'))
    def test_home_002_topic(self, case):
        """
            用例描述：首页--话题专栏
        """
        self.new.test_case_method(case,'get')

    @pytest.mark.parametrize('case', excel.get_excel_data('home_003_login_Score'))
    def test_home_003_login_Score(self, case):
        """
            用例描述：首页--每日登陆获取积分
        """
        self.new.test_case_method(case,'get')

    @pytest.mark.parametrize('case', excel.get_excel_data('home_004_update_Locate_City'))
    def test_home_004_update_Locate_City(self, case):
        """
            用例描述：首页--更新所属城市
        """
        self.new.test_case_method(case,'post')

    @pytest.mark.parametrize('case', excel.get_excel_data('home_005_hot_product'))
    def test_home_005_hot_product(self, case):
        """
            用例描述：首页--热门商品
        """
        self.new.test_case_method(case, 'get')

    @pytest.mark.parametrize('case', excel.get_excel_data('home_006_get_Weather_Info'))
    def test_home_006_get_Weather_Info(self, case):
        """
            用例描述：首页--获取天气信息
        """
        self.new.test_case_method(case, 'get')




