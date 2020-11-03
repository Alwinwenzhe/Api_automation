# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import allure, pytest
from Common import new_tool_a
from Common import ExcelHandler

@allure.feature('一生约--邀請')
@allure.severity('blocker')
class TestYsy002Invitation(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　
    '''

    excel = ExcelHandler.ExcelHandler()
    new = new_tool_a.New_Tool_A()


    # 详细测试 critical级别；修改个人信息-修改不是本人的用户信息，无权限操作 这个是针对接口的功能点详细测试 critical级别
    @allure.story('訪客邀請')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @allure.step("到訪戶號：户号列表")
    @pytest.mark.parametrize('case', excel.get_excel_data('invitation_001_bind_house'))
    def test_invitation_001_bind_house(self,case):
        """
            用例描述：访客邀请--到访户号--正常
        """
        self.new.test_case_method(case, 'get')


    @allure.story('getWaitVisitor')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('invitation_002_get_Wait_Visitor'))
    def test_invitation_002_get_Wait_Visitor(self, case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'post')


    @allure.story('getHistoryVisitor')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('invitation_003_get_History_Visitor'))
    def test_invitation_003_get_History_Visitor(self, case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'post')


    @allure.story('invite_Visitor')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('invitation_004_invite_Visitor'))
    def test_invitation_004_invite_Visitor(self, case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'post')

    @allure.story('invite_Visitor')  # allure.story  用于定义被测功能的用户场景，即子功能点
    @pytest.mark.parametrize('case', excel.get_excel_data('invitation_005_share_invitation'))
    def test_invitation_005_share_invitation(self, case):
        """
            用例描述：获取验证码，该用例数据源来自excel
        """
        self.new.test_case_method(case, 'get')