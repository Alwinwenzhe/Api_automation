# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:42
# @Author  : WangJuan
# @File    : run.py

"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""

import pytest, sys, os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from Common import Log
from Common import Shell
from Conf import Config


if __name__ == '__main__':


    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    args = ['-v','-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    cmd1 = 'allure generate %s -o %s  --clean' % (xml_report_path, html_report_path)
    # cmd2 = r'xcopy %s %s /e /Y /I' % (xml_report_path,html_report_path)   # trend使用

    try:
        shell.invoke(cmd1)
        # shell.invoke(cmd2)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise           # raise引发一个异常，比如，当一个条件不满足用户意愿时引发一个异常

    #使用jenkins的郵件發送，暫時不使用代碼發送報告，所以屏蔽以下代碼
    # try:
    #     mail = Email.SendMail()
    #     mail.sendMail()
    # except Exception as e:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise



