import yaml


class AnalysisData:

    def __init__(self, filename):

        self.filepath = "./data/" + filename + ".yaml"

    def analysis_data(self):

        with open(self.filepath, 'r') as  f:
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

    def analysis_base_data(self):

        with open(self.filepath, 'r',encoding='UTF-8') as f:
            data = yaml.load(f)
            dict_data  = data.values()
            list_data = []
            for i in dict_data:
                list_data.append(i)


            return list_data