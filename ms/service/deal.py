#! /usr/bin/env python
# -*- coding: utf-8 -*-


import time
import re
import ms.entity.record as record
import ms.util.constant as constant
import ms.util.fileio as fileio
from influxdb import InfluxDBClient


def process(oneline):
    print("开始处理日志-----------------》")
    """处理日志记录"""
    try:
        print("构建日志对象。。。")
        r = record.bulid(oneline)
        print("构建日志对象完成。。。")
    except Exception, e:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        timeindex_ = re.search("(?<=\"timeindex\":)\\w+.\\w+(?=,)", oneline).group()
        result = "SUCCESS" if e is None else "FAIL"
        msg = repr(e) if e is None else ""
        fileio.write_log("%s %s %s %s" % (now, timeindex_, result, msg))
        return None

    print("检查日志状态。。。。。")
    if not r.success():
        return None
    print("日志成功。。。。。")
    try:
        if record.WRITE == r.sql_type():
            print("执行写入。。。")
            write_deal(r)
        elif record.QUERY == r.sql_type():
            print("执行查询。。。")
            query_deal(r)
    except Exception, e:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result = "SUCCESS" if e is None else "FAIL"
        msg = repr(e) if e is None else ""
        fileio.write_log("%s %s %s %s" % (now, r.timeindex, result, msg))
        return None
    print("-----------------------》处理日志完成")


def query_deal(r):
    """处理query日志"""
    form = r.form
    # 不是CREATE、DROP和DELETE的语句就跳过
    if constant.CREATE not in form["q"].upper() \
            or constant.DROP not in form["q"].upper() \
            or constant.DELETE not in form["q"].upper():
        return None
    client = _get_slave_client()
    client.switch_database(form["db"])
    client.query(form["q"],
                 epoch=form["epoch"] if "epoch" in form else None,
                 database=form["db"] if "db" in form else None,
                 chunked=bool(form["chunked"]) if "chunked" in form else False)
    print("查询完成。。。")
    fileio.write_index(str(r.timeindex))


def write_deal(r):
    """处理write日志"""
    client = _get_slave_client()
    form = r.form
    client.switch_database(form["db"])
    client.write_points(_data2json(r.body),
                        time_precision=form["precision"] if "precision" in form else None,
                        database=form["db"] if "db" in form else None,
                        retention_policy=form["rp"] if "rp" in form else None)
    print("写入完成。。。")
    fileio.write_index(str(r.timeindex))


def _get_slave_client():
    """获取从库链接客户端"""
    return InfluxDBClient(constant.INFLUXDB_SLAVE_HOST,
                          constant.INFLUXDB_SLAVE_PORT,
                          constant.INFLUXDB_SLAVE_USER,
                          constant.INFLUXDB_SLAVE_PASSWORD)


def _data2json(body):
    """
    将日志参数转换为接口参数json对象
    point = {
            "measurement": "",
            "tags": {},
            "fields": {}
    }
    """
    def _p(db):
        return {
            "measurement": db["db"] if "db" in db else "",
            "tags": db["tag"] if "tag" in db else {},
            "fields": db["field"] if "field" in db else {},
            "time": db["time"] if "time" in db else ""
        }
    return [_p(b) for b in body]


def log(e=None):
    """
    暂未使用
    记录日志装饰器
    @:param e: 异常对象
    @:type e Exception
    """
    def _log(func):
        def wapper(*args, **kwargs):
            f = func(*args, **kwargs)
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            timeindex_ = kwargs["r"]["timeindex"]
            result = "SUCCESS" if e is None else "FAIL"
            msg = repr(e) if e is None else ""
            fileio.write_log("%s %s %s %s" % (now, timeindex_, result, msg))
            return f
        return wapper
    return _log


def index(i):
    """
    暂未使用
    索引装饰器，记录索引
    :param i: 索引值
    :type i: int
    """
    def _index(func):
        def wapper(*args, **kwargs):
            f = func(*args, **kwargs)
            fileio.write_index(i)
            return f
        return wapper
    return _index
