#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ms.service import deal
from ms.util.tail import Tail
import ms.util.constant as constant


if __name__ == "__main__":
    t = Tail(constant.INFLUXDB_MASTER_LOG)
    t.register_callback(deal.process)
    t.follow()
