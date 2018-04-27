#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ms.util.tail import Tail


def call_back_func(line):
    print(line)


t = Tail('./config/config.properties')
t.register_callback(call_back_func)
t.follow()
