# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest, os, sys
from Common import Consts
from Common import new_tool_a
from Common import ExcelHandler
from Common import req_reload
from Common import Assert

@allure.feature('ysy_Login')
@allure.severity('blocker')
@allure.story('Log in')
class TestO2O001Myself:
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()

    @pytest.mark.parametrize('case', excel.get_excel_data('myself_001_get_my_three_info'))
    def test_myself_001_get_my_three_info(self, case):
        """
            用例描述：首页--每日登陆获取积分
        """
        self.new.test_case_method(case, 'get')

    @pytest.mark.parametrize('case', excel.get_excel_data('myself_002_member_list'))
    def test_myself_002_member_list(self, case):
        """
            用例描述：首页--每日登陆获取积分
        """
        self.new.test_case_method(case, 'get')

