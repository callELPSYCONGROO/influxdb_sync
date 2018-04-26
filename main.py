#! /usr/bin/env python
# -*- coding: utf-8 -*-


import deal as deal
from tail import Tail
from properties import Properties


if __name__ == "__main__":
    p = Properties("./config/config.properties")
    t = Tail(p.get("influxdb.master.log"))
    t.register_callback(deal.process)
    t.follow()
