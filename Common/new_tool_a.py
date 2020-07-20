import json, re
from Common import Log
from Common import operate_json
from Conf import Config
from Common import operate_sql_al
from Common import ExcelHandler
from Common import req_reload
from Common import Assert

class New_Tool_A(object):

    log = Log.MyLog()
    oper_j = operate_json.OperateJson()
    conf = Config.Config()
    excel = ExcelHandler.ExcelHandler()
    reqe = req_reload.ReqReload()
    test = Assert.Assertions()

    def param_get_deal(self,case):
        '''
        case参数获取并进行相关处理
        :param case:
        :return:
        '''

        envir = case['envir']
        expect = case['case_expect']
        if expect:
            expect = self.multiple_data(envir,expect)
        preset_data = case['case_preset']
        urls = case['case_url']
        global_var = case['case_global_var']
        if preset_data:
            self.multiple_data(envir, preset_data)
        req_url = self.conf.host_debug
        api_url = req_url + urls
        api_url = self.multiple_data(envir, api_url)[0]
        headers = json.loads(case['case_header'])
        params = case['case_params']
        params = self.multiple_data(envir, params)  # params格式有问题
        return expect[0], api_url, headers, params, global_var          # 只验证第一个expect值即可

    def get_path(self, key, res):
        list_comma = key.split(',')
        for i in list_comma:
            list = i.split("/")
            list_last = list[-1]
            res_value = json.loads(res, encoding='utf-8')
            try:
                for i in range(len(list)):
                    if str(list[i]).isdigit():
                        res_value = res_value[int(list[i])]
                    else:
                        res_value = res_value[list[i]]
            except Exception as e:
                self.log.error('get param fail')
                raise
            self.oper_j.write_json_value(list_last, res_value)

    def response_write_to_json(self,path,response):
        '''
        写入json文件
        :param path:
        :param response:
        :return:
        '''
        self.get_path(path, response)


    def multiple_data(self,envir,data):
        '''
        对多个数据进行拆分组装，并还原;注意这里是处理了单个数据多种情况，未对多个数据多种情况进行处理---建议将三个方法拆开，合并调用
        数据如：如多个sql，或body是多个：'{"mobile":"c::","verifyCode":"j::verifyCode"}'
        :param envir:
        :param data:
        :return:list
        '''
        temp = []
        if data.startswith('{'):                # dict
            result = self.brackets_data(data,envir)
            return result
        elif ';' in data:                       # sql后都需要跟上";"
            split_data = data.split(';')
            for i in split_data:
                if len(i) > 0:
                    result = self.single_sql_data_deal(envir, i)
                    if result:
                        temp.append(result)
            return temp
        else:                                   # 这里是实际结果，不需要任何处理的
            temp.append(self.while_split_data(envir, data))
            return temp

    # def single_data_deal(self,data, envir):
    #     '''
    #     这里是对单个数据中可能出现$$或“format”进行处理
    #     :param data:
    #     :param envir:
    #     :return:
    #     '''
    #     oper_s = operate_sql_al.OperateSqlAl(envir)
    #     result = data
    #     exit_flag = True
    #     while exit_flag:
    #         if 'format' in result:
    #             result = self.format_data(result, envir)
    #             exit_flag = False
    #             return result
    #         elif '$$' in result:
    #             split_data = result.split("$$")
    #             sql_resutl = oper_s.execute_sql(split_data[1])
    #             self.oper_j.write_json_value(split_data[0], sql_resutl)
    #             exit_flag = False

    def single_sql_data_deal(self,envir,data):
        '''
        单个sql结构拆分
        :param data:
        :param envir:
        :return:
        '''
        oper_s = operate_sql_al.OperateSqlAl(envir)
        if '$$' in data:
            # 将$$识别为即将执行sql并写入json
            symbol_data = data.split('$$')
            symbol_data[1] = self.format_data(envir,symbol_data[1])
            val = oper_s.execute_sql(symbol_data[1])
            self.oper_j.write_json_value(symbol_data[0], val)
            return None
        else:
            val = self.format_data(envir,data)
            val = oper_s.execute_sql(val)
            return val

    def brackets_data(self,data, envir):
        '''
         处理通过“{”来输入的多个数据，比如dict， 针对dict中多个内容
        :param data:
        :param envir:
        :return:
        '''
        data = json.loads(data)  # 函数是将字符串转化为json格式字典
        for key, value in data.items():
            data[key] = self.while_split_data(envir, value)
        return data

    # def quotation_data(self,data,envir):
    #     '''
    #     处理通过“；”来输入的多个数据，比如: SQL语句
    #     :param data:
    #     :return: list
    #     '''
    #     mul_data = []
    #     split_data = data.split(';')
    #     for i in split_data:
    #         mul_data.append(self.while_split_data(envir, i))
    #     return mul_data

    def format_data(self,envir,data):
        '''
        处理数据中包含formate的待处理数据
        :param data:
        :return:
        '''
        if 'format' in data:
            oper_s = operate_sql_al.OperateSqlAl(envir)
            p1 = re.compile(r"[(](.*?)[')]", re.S)  # 非贪心匹配
            split_str = data.split('format')
            var_1 = re.findall(p1, split_str[1])
            # 这里会对list中每个值进行判断
            var_1 = self.while_split_data(envir, var_1)
            resutl = split_str[0].format(*var_1)        # 重组sql
        else:
            resutl = self.while_split_data(envir, data)
        return resutl

    def while_split_data(self,envir,data):
        '''
        循环处理数据中的变量
        :param envir:
        :param data:
        :return:
        '''
        if isinstance(data, str):
            data = self.split_data(envir,data)
        elif isinstance(data, list):
            new_data = []
            for i in data:
                i = self.split_data(envir, i)
                new_data.append(i)
            return new_data
        return  data

    # def typeof(self,envir,data):
    #     '''
    #     判断元素类型，做不同类型处理
    #     :param data:
    #     :return:
    #     '''
    #     if isinstance(data, str):
    #         self.while_split_data(envir,data)
    #     elif isinstance(data, list):
    #         for i in data:
    #             self.while_split_data(envir, data)

    def split_data(self,envir,data):
        '''
        所有数据进行分解并找到对应的分解方法，将最终结果返回
        注意这里并未对多个sql进行解析，需要单独进行处理
        还是需要处理多个数据，
        :param data:
        :return:
        '''
        oper_s = operate_sql_al.OperateSqlAl(envir)
        while 'j::' in data or 'c::' in data or 's::' in data:
            if 'j::' in data:
                symbol_data = data.split('j::')     # 这里有可能是body中的某个值传入，如：'j::verifyCode'
                con_data = self.oper_j.get_json_value(symbol_data[1])
                data = symbol_data[0] + con_data
                return data
            elif 'c::' in data:
                symbol_data = data.split('c::')
                con_data = self.con_var(symbol_data[1])
                data = symbol_data[0] + con_data
                return data
            elif 's::' in data:
                symbol_data = data.split('s::')
                con_data = oper_s.sql_main(symbol_data[1])     #這裡不能調用con_var方法
                data = con_data
                return data
            else:
                return data
                break
        else:
            return data

    def con_var(self,var):
        if var == 'tester_debug':
            temp_con_var = self.conf.tester_debug
        elif var == 'environment_debug':
            temp_con_var = self.conf.environment_debug
        elif var == 'host_debug':
            temp_con_var = self.conf.host_debug
        elif var == 'tester_release':
            temp_con_var = self.conf.tester_release
        elif var == 'environment_release':
            temp_con_var = self.conf.environment_release
        elif var == 'host_release':
            temp_con_var = self.conf.host_release
        else:
            temp_con_var = var
        return temp_con_var


if __name__ == '__main__':
    ut = New_Tool_A()
    # print(ut.while_split_data('test_debug',"s::SELECT IFNULL(dv.version,'error_version') FROM data_version dv WHERE dv.code='ios'"))
    # print(ut.split_data(''))
