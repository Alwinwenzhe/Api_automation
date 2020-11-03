# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler

@allure.feature('一生约--物业板块')  # @allure.feature 用于定义被测试的功能，被测产品的需求点
@allure.severity('blocker')  # allure.story  用于定义被测功能的用例等级，blocker--测试主流程 blocker级别；
@allure.story('物业首页')
class TestYsy003BiotopeServe(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @allure.step("首页广播")
    @pytest.mark.parametrize('case', excel.get_excel_data('biotope_serve_001_notice_newest'))
    def test_biotope_serve_002_notice_newest(self, case):
        """
            用例描述：首页刷新--广播
        """
        self.new.test_case_method(case, 'get')

    @allure.step("物业管家电话")
    @pytest.mark.parametrize('case', excel.get_excel_data('biotope_serve_003_phone_biotopeId'))
    def test_biotope_serve_003_phone_biotopeId(self, case):
        """
            用例描述：物业管家--电话
        """
        self.new.test_case_method(case, 'get')

    @allure.step("首页banner")
    @pytest.mark.parametrize('case', excel.get_excel_data('biotope_serve_004_list_bannerCode'))
    def test_biotope_serve_004_list_bannerCode(self, case):
        """
            用例描述：首页banner
        """
        self.new.test_case_method(case, 'get')


