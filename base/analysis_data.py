import sys
import yaml
import os


class AnalysisData:

    def __init__(self, filename):
        path = os.path.abspath('..') + "\\data\\"
        self.filepath = path + filename + ".yaml"

    # 一种场景多要实现多用例时，数据源加载
    def analysis_data(self):

        with open(self.filepath, 'r', encoding='utf-8') as  f:
            data = yaml.load(f)

            value = data.values()
            list_value = []

            data_lsit = []
            for i in value:
                list_value.append(i)
            for j in list_value:
                list_data = []
                for k in j:
                    list_data.append(j.get(k))

                data_lsit.append(list_data)

            return data_lsit

    # 打印日志，需要加载获取数据
    def analysis_base_data(self):

        with open(self.filepath, 'r', encoding='UTF-8') as f:
            data = yaml.load(f)
            dict_data = data.values()
            list_data = []
            for i in dict_data:
                list_data.append(i)

            return list_data
