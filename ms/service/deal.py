#! /usr/bin/env python
# -*- coding: utf-8 -*-


import time
import re
import ms.entity.record as record
import ms.util.constant as constant
import ms.util.fileio as fileio
from influxdb import InfluxDBClient


def process(oneline):
    fileio.print_msg("开始处理日志-----------------》")
    """处理日志记录"""
    try:
        fileio.print_msg("构建日志对象。。。")
        r = record.bulid(oneline)
        fileio.print_msg("构建日志对象完成。。。")
    except Exception, e:
        fileio.print_msg("发生异常：", e.message)
        timeindex_ = re.search("(?<=\"timeindex\":)\\w+.\\w+(?=,)", oneline).group()
        now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        result = "SUCCESS" if e is None else "FAIL"
        msg = e.message
        fileio.write_log("%s %s %s %s" % (now, timeindex_, result, msg))
        fileio.print_msg("---------------------------》日志处理异常")
        return None

    fileio.print_msg("检查日志状态。。。。。")
    if not r.success():
        return None
    fileio.print_msg("日志成功。。。。。")
    try:
        if record.WRITE == r.sql_type():
            fileio.print_msg("执行写入。。。")
            write_deal(r)
        elif record.QUERY == r.sql_type():
            fileio.print_msg("执行查询。。。")
            query_deal(r)
    except Exception, e:
        fileio.print_msg("发生异常：", e.message)
        now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        result = "SUCCESS" if e is None else "FAIL"
        msg = e.message
        fileio.write_log("%s %s %s %s" % (now, r.timeindex, result, msg))
        fileio.print_msg("---------------------------》日志处理异常")
        return None
    fileio.print_msg("-----------------------》处理日志完成")


def query_deal(r):
    """处理query日志"""
    form = r.form
    # 不是CREATE、DROP和DELETE的语句就跳过
    if ((constant.CREATE in form["q"].upper()) or (constant.DROP in form["q"].upper()) or (constant.DELETE in form["q"].upper())) is False:
        return None
    client = _get_slave_client()
    client.switch_database(form["db"])
    client.query(form["q"],
                 epoch=form["epoch"] if "epoch" in form else None,
                 database=form["db"] if "db" in form else None,
                 chunked=bool(form["chunked"]) if "chunked" in form else False)
    fileio.print_msg("查询完成。。。")
    fileio.write_index(str(r.timeindex))


def write_deal(r):
    """处理write日志"""
    client = _get_slave_client()
    form = r.form
    client.switch_database(form["db"])
    client.write_points(_data2json(r.body),
                        time_precision=r.get_time_precision() if "precision" in form else None,
                        database=form["db"] if "db" in form else None,
                        retention_policy=form["rp"] if "rp" in form else None)
    fileio.print_msg("写入完成。。。")
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
