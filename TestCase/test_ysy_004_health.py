import allure, pytest
from Common import Consts
from Common import new_tool_a
from Common import ExcelHandler
from Common import req_reload
from Common import Assert

@allure.feature('Invitation')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
class TestYsy004Health:
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()
    reqe = req_reload.ReqReload()
    test = Assert.Assertions()


    @allure.severity('critical')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
    @allure.story('health')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('health_001_addMenberStep'))
    def test_invitation_01_bind_house(self,case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        expect,api_url, headers,params, global_var= self.new.param_get_deal(case)
        response = self.reqe.req('post',api_url, params, headers, global_var)              # 响应有问题，需要查看日志
        if global_var:
            self.new.response_write_to_json(global_var,response['text'])
        self.test.assert_common(response['code'],response['body'],expect,response['time_consuming'])
        Consts.RESULT_LIST.append('True')
        print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'],case['case_description'], case['case_expect']))
