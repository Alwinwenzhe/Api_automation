# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @Author  : WangJuan
# @File    : Config.py

from configparser import ConfigParser
from Common import Log
import os, re

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 脚本路径
TEST_CASE_PATH = BASE_PATH + r'\Conf\接口示例.xlsx'

class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"

    # values:
    # [debug]
    # 一生约测试环境信息
    YSY_USER = "tester"
    YSY_ENVIRONMENT = "environment"
    YSY_HOST = "ysy_host"
    # 一生约测试环境数据库信息
    YSY_DB_HOST = "ysy_sql_dbhost"
    YSY_DB_PORT = "ysy_sql_dbport"
    YSY_DB_NAME = "ysy_sql_dbname"
    YSY_DB_USER = "ysy_sql_user"
    YSY_DB_PWD = "ysy_sql_pwd"
    # 雨花斋测试环境信息
    YHZ_HOST = "yhz_host"
    YHZ_DB_NAME = "yhz_db_name"
    YHZ_DB_USER = "yhz_sql_user"
    YHZ_DB_PWD = "yhz_sql_pwd"
    YHZ_USER = 'tyhz_user'

    # 商城测试环境
    O2O_HOST = "ysyo2o_host"
    O2O_DB_NAME = 'ysyo2o_db_name'

    # [release] 下列数据中对应的值是没有的
    # 一生约正式环境信息
    YSY_USER = "ysy_user"
    YSY_USERID = "releaser_userId"
    YSY_ACCESSTOKEN = "releaser_accessToken"
    YSY_ENVIRONMENT = "environment"
    YSY_HOST = "ysy_host"
    # 一生约正式环境数据库信息
    YSY_DB_HOST = "ysy_sql_dbhost"
    YSY_DB_PORT = "ysy_sql_dbport"
    YSY_DB_NAME = "ysy_sql_dbname"
    YSY_DB_USER = "ysy_sql_user"
    YSY_DB_PWD = "ysy_sql_pwd"
    # 一生约物业正式环境信息
    YSY_PRO_USER = "ysy_pro_user"
    YSY_PRO_HOST = "ysy_pro_host"
    # 商城正式环境
    O2O_HOST = "ysyo2o_host"
    O2O_DB_NAME = 'ysyo2o_db_name'
    # 雨花斋正式环境
    YHZ_USER = 'yhz_user'

    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        # print(self.conf_path)
        self.xml_report_path = Config.path_dir+'/allure-results'
        self.html_report_path = Config.path_dir+'/allure-report'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

        # 一生约测试环境信息
        self.tysy_user = self.get_conf(Config.TITLE_DEBUG, Config.YSY_USER)
        self.tysy_environment = self.get_conf(Config.TITLE_DEBUG, Config.YSY_ENVIRONMENT)
        self.tysy_host = self.get_conf(Config.TITLE_DEBUG, Config.YSY_HOST)
        # 一生约正式环境信息
        self.ysy_user = self.get_conf(Config.TITLE_RELEASE, Config.YSY_USER)
        self.ysy_userId = self.get_conf(Config.TITLE_RELEASE, Config.YSY_USERID)
        self.ysy_accesstoken = self.get_conf(Config.TITLE_RELEASE, Config.YSY_ACCESSTOKEN)
        self.ysy_environment = self.get_conf(Config.TITLE_RELEASE, Config.YSY_ENVIRONMENT)
        self.ysy_host = self.get_conf(Config.TITLE_RELEASE, Config.YSY_HOST)

        # 一生约测试环境数据库
        self.tysy_db_host = self.get_conf(Config.TITLE_DEBUG,Config.YSY_DB_HOST)
        self.tysy_db_port = self.get_conf(Config.TITLE_DEBUG,Config.YSY_DB_PORT)
        self.tysy_db_name = self.get_conf(Config.TITLE_DEBUG, Config.YSY_DB_NAME)
        self.tysy_db_user = self.get_conf(Config.TITLE_DEBUG, Config.YSY_DB_USER)
        self.tysy_db_pwd = self.get_conf(Config.TITLE_DEBUG, Config.YSY_DB_PWD)
        # 一生约正式环境数据库
        self.ysy_db_host = self.get_conf(Config.TITLE_RELEASE, Config.YSY_DB_HOST)
        self.ysy_db_port = self.get_conf(Config.TITLE_RELEASE, Config.YSY_DB_PORT)
        self.ysy_db_name = self.get_conf(Config.TITLE_RELEASE, Config.YSY_DB_NAME)
        self.ysy_db_user = self.get_conf(Config.TITLE_RELEASE, Config.YSY_DB_USER)
        self.ysy_db_pwd = self.get_conf(Config.TITLE_RELEASE, Config.YSY_DB_PWD)

        # 雨花斋测试库信息，user和pwd和一生约测试一致
        self.tyhz_user = self.get_conf(Config.TITLE_DEBUG, Config.YHZ_USER)
        self.tyhz_host = self.get_conf(Config.TITLE_DEBUG, Config.YHZ_HOST)
        self.tyhz_db_name = self.get_conf(Config.TITLE_DEBUG,Config.YHZ_DB_NAME)
        # 雨花斋正式库信息
        self.yhz_user = self.get_conf(Config.TITLE_RELEASE,Config.YHZ_USER)
        self.yhz_host = self.get_conf(Config.TITLE_RELEASE, Config.YHZ_HOST)
        self.yhz_db_name = self.get_conf(Config.TITLE_RELEASE, Config.YHZ_DB_NAME)

        # 一生约测试环境物业app
        self.tysy_pro_host = self.get_conf(Config.TITLE_DEBUG, Config.YSY_PRO_HOST)
        # 一生约正式环境物业app
        self.ysy_pro_user = self.get_conf(Config.TITLE_RELEASE,Config.YSY_PRO_USER)
        self.ysy_pro_host = self.get_conf(Config.TITLE_RELEASE,Config.YSY_PRO_HOST)

        # 小猪测试数据库
        self.tysyo2o_host = self.get_conf(Config.TITLE_DEBUG, Config.O2O_HOST)
        self.tdb_name_o2o = self.get_conf(Config.TITLE_DEBUG,Config.O2O_DB_NAME)
        # 小猪正式数据库
        self.ysyo2o_host = self.get_conf(Config.TITLE_RELEASE, Config.O2O_HOST)
        self.db_name_o2o = self.get_conf(Config.TITLE_RELEASE, Config.O2O_DB_NAME)

        # self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        # self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        # self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        # self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        # self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改：w+ 可读可写-覆盖写；如无文件则创建
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == "__main__":
    con = Config()
    print(TEST_CASE_PATH)
    print(con.tester_debug)
    te = con.db_pwd_ysy_debug
    print(te)
