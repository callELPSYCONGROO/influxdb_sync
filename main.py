#! /usr/bin/env python
# -*- coding: utf-8 -*-

from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
from tail import Tail
from properties import Properties


__properties = Properties('config/config.properties')
"""InfluxDB数据库状态，master为初始化主机，slave为初始化从机，status为链接状态，is_master为当前主从状态"""
__db_status = {
    'master': {
        'status': True,
        'is_master': True
    },
    'slave': {
        'status': True,
        'is_master': False
    }
}


def listen_log(path):
    """
    使用tail监听日志文件
    :param path: 日志文件路径
    :type path: string
    """
    tail = Tail(__properties.get(path))
    tail.register_callback(__handling_log_record)
    tail.follow()


def __handling_log_record(log_record):
    """
    日志文件新增记录处理。
    将读取到的新日志记录解析后插入当前从机中。
    """
    print(log_record)
    if not (__db_status['master']['status'] and __db_status['slave']['status']):
        pass
    if __db_status['master']['is_master'] and not __db_status['slave']['is_master']:
        master_slave_sync(__client('master'), log_record)
    elif not __db_status['master']['is_master'] and __db_status['slave']['is_master']:
        master_slave_sync(__client('slave'), log_record)


def master_slave_sync(client, data):
    """将当前主机新增数据插入当前从机中。"""
    client.write_points(data)


def __client(client_name):
    """获得对应客户端"""
    host = __properties.get('influxdb.' + client_name + '.host')
    port = __properties.get('influxdb.' + client_name + '.port')
    user = __properties.get('influxdb.' + client_name + '.user')
    password = __properties.get('influxdb.' + client_name + '.password')
    return InfluxDBClient(host, port, user, password)


def check_influxdb_activity():
    """
    检查连接状态。
    :except InfluxDBClientError: 客户端发出的请求错误异常。
    :except Exception: 其他异常，需要切换主从。
    """
    master_client = __client('master')
    slave_client = __client('slave')
    global __db_status
    try:
        master_client_ping = master_client.ping()
        if is_blank(master_client_ping):
            __db_status['master']['status'] = False
        else:
            __db_status['master']['status'] = True
        slave_client_ping = slave_client.ping()
        if is_blank(slave_client_ping):
            __db_status['slave']['status'] = False
        else:
            __db_status['slave']['status'] = True
    except InfluxDBClientError:
        pass
    except Exception:
        if __db_status['master']['is_master'] and not __db_status['slave']['is_master']:
            __db_status['master']['is_master'] = False
            __db_status['slave']['is_master'] = True
        elif not __db_status['master']['is_master'] and __db_status['slave']['is_master']:
            __db_status['master']['is_master'] = True
            __db_status['slave']['is_master'] = False


def is_blank(text):
    """判断字符串为空"""
    if text is None:
        return True
    elif not text.strip():
        return True
    else:
        return False


if __name__ == '__main__':
    if __db_status['master']['is_master'] and not __db_status['slave']['is_master']:
        listen_log(__properties.get('influxdb.master.log'))
    elif not __db_status['master']['is_master'] and __db_status['slave']['is_master']:
        listen_log(__properties.get('influxdb.slave.log'))
