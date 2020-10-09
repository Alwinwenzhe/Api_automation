# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午10:14
# @Author  : WangJuan
# @File    : Assert.py


"""
封装Assert方法

"""
from Common import Log
from Common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)         # 将body序列化为JSON格式的str
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_common(self,res_code,res_body,res_expect,res_time):
        '''
        通用常用三个维度验证
        :param res_code: 接口响应代码
        :param res_body: 接口响应内容
        :param res_expect: 接口响应期望值
        :param res_time: 接口响应时间
        :return:
        '''
        assert self.assert_code(res_code, 200)
        assert self.assert_in_text(res_body, res_expect)
        assert self.assert_time(res_time, 1500)

    def assert_php(self,res_code,res_time):
        '''
        判断响应状态及响应时间
        :return:
        '''
        assert self.assert_code(res_code, 200)
        assert self.assert_time(res_time, 1500)


