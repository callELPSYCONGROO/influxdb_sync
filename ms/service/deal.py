#! /usr/bin/env python
# -*- coding: utf-8 -*-


import json
import re
import ms.entity.record as record
import ms.util.properties as properties
from influxdb import InfluxDBClient


def process(log):
    """处理日志记录"""
    try:
        json_obj = json.loads(log)
        r = record.Record(json_obj)
    except Exception:
        return None

    if not r.success():
        return None

    if record.WRITE == r.sql_type():
        pass
    elif record.QUERY == r.sql_type():
        pass
    else:
        return None


def query_deal(r):
    """处理query日志"""
    pass


def write_deal(r):
    """处理write日志"""
    __data2json(r.get_body())
    form = r.get_form()


def __get_slave_client():
    """获取从库链接客户端"""
    return InfluxDBClient(properties.get_default_config("influxdb.slave.host"),
                          properties.get_default_config("influxdb.slave.port"),
                          properties.get_default_config("influxdb.slave.user"),
                          properties.get_default_config("influxdb.slave.password"))


def __data2json(body):
    """
    将日志参数转换为接口参数json对象
    point = {
            "measurement": "",
            "tags": {},
            "fields": {}
    }
    """
    return [{
        "measurement": body["dbtag"],
        "tags": body["tag"],
        "fields": body["field"],
        "time": body["time"]
    }]


def __write_record(db, data):
    """向数据库中写记录"""
    client = __get_slave_client()
    client.switch_database(db)
    client.write_points(data)
