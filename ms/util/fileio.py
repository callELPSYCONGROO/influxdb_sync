#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""文件读写"""


import codecs
from ms import config


class FileIO(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self, mode="rb", decode="utf-8"):
        with codecs.open(self.file_path, mode) as f:
            return f.read().decode(decode)

    def write(self, content, mode="w"):
        with codecs.open(self.file_path, mode) as f:
            f.write(content)


def read_index():
    """暂未使用，读取索引"""
    return FileIO(config.INDEX_PATH).read()


def write_index(index):
    """暂未使用，覆盖索引"""
    return FileIO(config.INDEX_PATH).write(index)


def write_log(log):
    """向日志文件中写日志"""
    return FileIO(config.MS_LOG_PATH).write(log + " \n", mode="a+")


def print_msg(msg):
    if config.MODEL == "test":
        print(msg)
