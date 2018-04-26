#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""文件读写"""


import codecs


class FileIO(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self, mode="rb", decode="utf-8"):
        with codecs.open(self.file_path, mode) as f:
            return f.read().decode(decode)

    def write(self, content, mode="w"):
        with codecs.open(self.file_path, mode) as f:
            f.write(content)
