# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest, sys
sys.path.append("D:\Job\python\Script\Api_automation")  #增加系统寻包路径
from Common import Consts
from Common import new_tool_a
from Common import ExcelHandler
from Common import req_reload
from Common import Assert

@allure.feature('雨花_老人登记_登录')
@allure.severity('blocker')
class TestYhz001Login:
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

    @allure.story('获取验证码')
    @pytest.mark.parametrize('case', excel.get_excel_data('yhz_001_register_verify'))
    def test_yhz_001_register_verify(self, case):
        """
            用例描述：获取验证码
        """
        self.new.test_case_method(case, 'post')

    @allure.story('登录')
    @pytest.mark.parametrize('case', excel.get_excel_data('yhz_002_log_in'))
    def test_login_002_log_in(self, case):
        """
            用例描述：验证码登录
        """
        self.new.test_case_method(case, 'post')

    @allure.story('用户信息')
    @pytest.mark.parametrize('case', excel.get_excel_data('yhz_003_user_info'))
    def test_login_003_user_info(self, case):
        """
            用例描述：验证码登录
        """
        self.new.test_case_method(case, 'get')
