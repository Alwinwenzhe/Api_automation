# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:56
# @Author  : WangJuan
# @File    : tools.py

"""
读取yaml测试数据
"""

import yaml
import os
import os.path


def parse():
    '''
    读取目标目录中所有文件，更新进pages，并返回
    :return:
    '''
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param'
    pages = {}
    # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下；
    # path_ya是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path,'r',encoding="UTF-8") as f:
                page = yaml.safe_load(f)        # 解析流中的第一个YAML文档并生成相应的Python对象
                pages.update(page)
        return pages


class GetPages:
    @staticmethod       #python staticmethod 返回函数的静态方法。
    def get_page_list():
        _page_list = {}     # 单下划线表示表面上私有 ，但是其实这样的实例变量外部是可以访问的；该方法不强制要求传递参数；变量前的双下划线表示真正的私有,实际上的私有,只有内部可以访问，外部不能访问
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
    print(lists)
