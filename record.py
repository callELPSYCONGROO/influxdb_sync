#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Record(object):

    def __init__(self, *args, **kwargs):
        self.__timestamp = kwargs["timestamp"]
        self.__host = kwargs["host"]
        self.__method = kwargs["method"]
        self.__uri = kwargs["uri"]
        self.__params = kwargs["params"]
        self.__proto = kwargs["proto"]
        self.__status = kwargs["status"]
        self.__size = kwargs["size"]
        self.__referer = kwargs["referer"]
        self.__agent = kwargs["agent"]
        self.__requestid = kwargs["requestid"]
