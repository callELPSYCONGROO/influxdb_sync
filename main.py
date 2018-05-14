#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ms.service import deal
from ms.util.tail import Tail
from ms import config


if __name__ == "__main__":
    t = Tail(config.INFLUXDB_MASTER_LOG)
    t.register_callback(deal.process)
    t.follow()
