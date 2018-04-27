#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""日志对象"""


import re


QUERY = "query"
WRITE = "write"


def parse_form(form):
    """
    form字符串转换为dict对象。
     # kwargs["form"]格式：   map[precision:[ns] rp:[sdd] consistency:[all] db:[ceshi]]
    """
    split = form[4:-1].split()
    d = {}
    for kv in split:
        k = re.search("\\w+", kv).group()
        print(k)
        v = re.search("(?<=\\[)\\w*(?=\\])", kv).group()
        print(v)
        d[k] = v
    return d


def parse_body(body):
    """
    body传入格式为：" cpu,host=serverF,region=us-west4 value=0.64 1434055562000000101"。
    :param body: 日志中插入记录的参数
    :return: 返回格式为：
    {
        "time": 1434055562000000101,
        "dbtag": {
                    "db": ceshi,
                    "kv": {"host": "serverF", "region": "us-west4"}
                },
        "field": {
                    "kv": {value: 0.64}
                }
    }
    """
    pb = {}
    for index, value in enumerate(body.split()):
        if index == 0:
            pb["dbtag"] = split_str(value)
        elif index == 1:
            pb["field"] = split_str(value)
        elif index == 2:
            pb["time"] = value
    return pb


def split_str(s):
    d = {}
    for m in (kv for kv in s.split(",")):
        m_split = m.split("=")
        if len(m_split) > 1:
            if "kv" not in d:
                d["kv"] = {}
            d["kv"][m_split[0]] = m_split[1]
        else:
            d["db"] = m_split[0]
    return d


class Record(object):

    def __init__(self, **kwargs):
        self.__timeindex = kwargs["timeindex"]
        self.__host = kwargs["host"]
        self.__username = kwargs["username"]
        self.__method = kwargs["method"]
        self.__uri = kwargs["uri"]
        self.__form = parse_form(kwargs["form"])
        self.__path = kwargs["path"]
        self.__params = kwargs["params"]
        self.__proto = kwargs["proto"]
        self.__body = parse_body(kwargs["body"])
        self.__status = kwargs["status"]
        self.__size = kwargs["size"]
        self.__referer = kwargs["referer"]
        self.__agent = kwargs["agent"]
        self.__requestid = kwargs["reqId"]

    def success(self):
        """判断此请求是否成功"""
        if self.__username != "master2slave":
            return False
        if self.__status != "200" or self.__status != "204":
            return False
        return True

    def sql_type(self):
        """判断日志SQL操作类型"""
        if QUERY in self.__path:
            return QUERY
        elif WRITE in self.__path:
            return WRITE
        else:
            return None
