#
# import allure, pytest
# from Common import Consts
# from Common import new_tool_a
# from Common import ExcelHandler
# from Common import req_reload
# from Common import Assert
#
#
# class TestBase:
#     '''
#     # BLOCKER = 'blocker'　　阻塞缺陷
#     # CRITICAL = 'critical'　严重缺陷
#     # NORMAL = 'normal'　　  一般缺陷
#     # MINOR = 'minor'　　    次要缺陷
#     # TRIVIAL = 'trivial'　　轻微缺陷　
#     '''
#
#     excel = ExcelHandler.ExcelHandler()
#     new = new_tool_a.New_Tool_A()
#     reqe = req_reload.ReqReload()
#     test = Assert.Assertions()
#
#     def test_001(self):
#         ex_ti = self.excel.get_excel_data()
#         for item in ex_ti:
#             @allure.feature('Log')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
#
#
#     def demo(self,case):
#         """
#             用例描述：获取验证码，该用例数据源来自excel
#         """
#         api_method, expect,api_url, headers,params= self.new.param_get_deal(case)
#         response = self.reqe.req(api_method,api_url, params, headers)              # 响应有问题，需要查看日志
#         self.test.assert_common(response['code'],response['body'],expect,response['time_consuming'])
#         Consts.RESULT_LIST.append('True')
#         print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'],case['case_description'], case['case_expect']))