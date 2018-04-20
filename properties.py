# -*- coding: utf-8 -*-
"""
    Properties：获取.properties配置文件属性
                get_properties()获取全文
                get(key)获取key对应的值
"""


class Properties(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.__properties = {}

    def __get_dict(self, str_name, dict_name, value):

        if str_name.find('.') > 0:
            k = str_name.split('.')[0]
            dict_name.setdefault(k, {})
            return self.__get_dict(str_name[len(k) + 1:], dict_name[k], value)
        else:
            dict_name[str_name] = value
            return

    def get_properties(self):
        try:
            pro_file = open(self.file_name, 'Ur')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0]) + 1:]
                    self.__get_dict(strs[0].strip(), self.__properties, strs[1].strip())
        except Exception, e:
            raise e
        else:
            pro_file.close()
        return self.__properties

    def get(self, key):
        p = self.__properties
        split = key.split('.')
        for k in split:
            try:
                p = p[k]
            except Exception, e:
                raise e
        return p
