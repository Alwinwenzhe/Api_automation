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
    YSY_TESTER = "tester"
    YSY_TEST_ENVIRONMENT = "environment"
    YSY_TEST_HOST = "ysy_host"
    YSY_TEST_DB_HOST = "sql_dbhost"
    YSY_TEST_DB_PORT = "sql_dbport"
    YSY_TEST_DB_NAME = "sql_dbname"
    YSY_TEST_DB_USER = "sql_user"
    YSY_TEST_DB_PWD = "sql_pwd"

    # [release] 下列数据中对应的值是没有的
    YSY_REALSER = "releaser"
    YSY_REALSE_ENVIRONMENT = "release_environment"
    YSY_REALSE_HOST = "release_host"
    YSY_REALSE_DB_HOST = "release_sql_dbhost"
    YSY_REALSE_DB_PORT = "release_sql_dbport"
    YSY_REALSE_DB_NAME = "release_sql_dbname"
    YSY_REALSE_DB_USER = "release_sql_user"
    YSY_REALSE_DB_PWD = "release_sql_pwd"

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
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

        # 分别获取三个配置模块中的内容
        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TEST_ENVIRONMENT)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TEST_HOST)
        self.db_host_ysy_debug = self.get_conf(Config.TITLE_DEBUG,Config.YSY_TEST_DB_HOST)
        self.db_port_ysy_debug = self.get_conf(Config.TITLE_DEBUG,Config.YSY_TEST_DB_PORT)
        self.db_name_ysy_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TEST_DB_NAME)
        self.db_user_ysy_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TEST_DB_USER)
        self.db_pwd_ysy_debug = self.get_conf(Config.TITLE_DEBUG, Config.YSY_TEST_DB_PWD)

        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSER)
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_ENVIRONMENT)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_HOST)
        self.db_host_ysy_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_DB_HOST)
        self.db_port_ysy_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_DB_PORT)
        self.db_name_ysy_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_DB_NAME)
        self.db_user_ysy_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_DB_USER)
        self.db_pwd_ysy_release = self.get_conf(Config.TITLE_RELEASE, Config.YSY_REALSE_DB_PWD)

        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

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
