#! /usr/bin/env python
#  -*- coding: utf-8 -*-
"""常量"""
# 配置文件路径，现在暂时不使用
CONFIG_PATH = "./config/config.properties"
# 索引文件路径
INDEX_PATH = "./record/index.ms"
# 主从复制系统日志文件路径
MS_LOG_PATH = "./logs/ms.log"

# 主机日志文件路径
INFLUXDB_MASTER_LOG = "/usr/software/logs/http.log"
# 从机HOST
INFLUXDB_SLAVE_HOST = "118.24.160.252"
# 从机PORT
INFLUXDB_SLAVE_PORT = "8086"
# 从机用户名
INFLUXDB_SLAVE_USER = "ims"
# 从机密码
INFLUXDB_SLAVE_PASSWORD = "ims"

# SQL 关键字
CREATE = "CREATE"
DROP = "DROP"
DELETE = "DELETE"
