#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""日志对象"""


import re
import json


QUERY = "query"
WRITE = "write"


def _parse_form(form):
    """
    form字符串转换为dict对象。
     # kwargs["form"]格式：   map[precision:[ns] rp:[sdd] consistency:[all] db:[ceshi]]
    """
    d = {}
    split = form[4:-2].split("] ")
    for kv in split:
        k = re.search("\\w+", kv).group()
        v = re.search("(?<=\\[)[\\s\\S]*", kv, flags=re.IGNORECASE).group()
        d[k] = v
    return d


def _parse_body(body):
    """
    body传入格式为：" cpu,host=serverF,region=us-west4 value=0.64 1434055562000000101"。
    :param body: 日志中插入记录的参数
    :return: 返回格式为：
            [{
            'time': '1434055562000000101',
            'field': {
                    'value': '0.64'
                    },
            'tag': {
                    'region': 'us-west4',
                    'host': 'serverF'
                    },
            'db': 'cpu'
            },
            ...
            ]
    """
    bl = []
    for ib in body.split(";"):
        pb = {}
        for index, value in enumerate(ib.split()):
            if index == 0:
                pb["tag"] = _split_tag(value)["tag"]
                pb["db"] = _split_tag(value)["db"]
            elif index == 1:
                pb["field"] = _split_field(value)
            elif index == 2:
                pb["time"] = int(value)
        if len(pb) > 0:
            bl.append(pb)
    return bl


def _split_tag(s):
    d = {}
    for m in (kv for kv in s.split(",")):
        m_split = m.split("=")
        if len(m_split) > 1:
            if "tag" not in d:
                d["tag"] = {}
            d["tag"][m_split[0]] = m_split[1]
        else:
            d["db"] = m_split[0]
    return d


def _split_field(s):
    d = {}
    for m in (kv for kv in s.split(",")):
        m_split = m.split("=")
        d[m_split[0]] = m_split[1]
    return d


class Record(object):

    def __init__(self, **kwargs):
        self.timeindex = kwargs["timeindex"] if "timeindex" in kwargs else None
        self.host = kwargs["host"] if "host" in kwargs else None
        self.username = kwargs["username"] if "username" in kwargs else None
        self.method = kwargs["method"] if "method" in kwargs else None
        self.uri = kwargs["uri"] if "uri" in kwargs else None
        self.form = _parse_form(kwargs["form"]) if "form" in kwargs else None
        self.path = kwargs["path"] if "path" in kwargs else None
        self.proto = kwargs["proto"] if "proto" in kwargs else None
        self.body = _parse_body(kwargs["body"]) if "body" in kwargs else None
        self.status = kwargs["status"] if "status" in kwargs else None
        self.size = kwargs["size"] if "size" in kwargs else None
        self.referer = kwargs["referer"] if "referer" in kwargs else None
        self.agent = kwargs["agent"] if "agent" in kwargs else None
        self.requestid = kwargs["reqId"] if "reqId" in kwargs else None

    def success(self):
        """判断此请求是否成功"""
        return self.status != "200" or self.status != "204"

    def sql_type(self):
        """判断日志SQL操作类型"""
        if QUERY in self.path:
            return QUERY
        elif WRITE in self.path:
            return WRITE
        else:
            return None

    def get_time_precision(self):
        return "n" if self.form["precision"] == "ns" else None

    def get_rp(self):
        return self.form["rp"] if self.form["rp"] else None


def bulid(json_str):
    r = Record()
    r.__dict__ = json.loads(json_str)
    r.body = _parse_body(r.body)
    r.form = _parse_form(r.form)
    return r
