#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ms.util.tasker import Tasker
import time


def f():
    print(time.time())


def t():
    tasker = Tasker(2, f)
    tasker.start()


if __name__ == "__main__":
    t()
