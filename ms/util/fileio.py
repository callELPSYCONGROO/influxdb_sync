#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""文件读写"""


import codecs
from ms.util import constant


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
    """读取索引"""
    return FileIO(constant.INDEX_PATH).read()


def write_index(index):
    """覆盖索引"""
    return FileIO(constant.INDEX_PATH).write(index)


def write_log(log):
    """向日志文件中写日志"""
    return FileIO(constant.MS_LOG_PATH).write(log, mode="a+")
