# # -*- coding: utf-8 -*-
# # @Time    : 2018/7/24 下午3:33
# # @Author  : WangJuan
# # @File    : Session.py
#
# """
# 封装获取cookie方法
#
# """
#
# import requests
# from Common import Util
# from Common import Log
# from Common import Operate_json
# from Conf import Config
#
#
# class TestLogin(object):
#
#     config = Config.Config()
#     log = Log.MyLog()
#     com = Util.Util()
#     oper_j = Operate_json.OperateJson()
#     '''
#     在case执行前获取cookies信息已被注释
#     根据实际情况修改为获取验证码，并写入文件，以待其它接口调用
#     '''
#
#     def test_login_get_verify_code(self, env):
#         """
#         获取session
#         :param env: 环境变量
#         :return:
#         """
#         headers = {
#             "Content-Type":"application/json; charset=UTF-8",
#             "enterpriseId":"1122c78ae5d140a5acbaa9e75c8b8994"
#         }
#
#         if env == "debug":
#             login_url = 'https://' + self.config.loginHost_debug
#             parm = self.config.loginInfo_debug
#
#             session_debug = requests.session()
#             response = session_debug.post(login_url, parm, headers=headers)
#             print(response.cookies)
#             # text = '{"code":0,"data":{"verifyCode":"7201","isReg":"Y"},"ts":1590047375037}'
#             key,value = self.com.get_path('data/verifyCode', response.text)
#             self.oper_j.write_json_value(key,value)
#
#         elif env == "release":
#             login_url = 'http://' + self.config.loginHost_release
#             parm = self.config.loginInfo_release
#             session_release = requests.session()
#             response = session_release.post(login_url, parm, headers=headers)
#             print(response.cookies)
#             key, value = self.com.get_path('verifyCode', response.text).items()
#             self.oper_j.write_json_value(key, value)
#
#         else:
#                 print("get cookies error")
#                 self.log.error('get cookies error, please checkout!!!')
#
# if __name__ == '__main__':
#     ss = TestLogin()
#     ss.test_login_get_verify_code('debug')