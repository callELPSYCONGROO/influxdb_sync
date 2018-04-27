#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ms.service import deal
from ms.util.tail import Tail
import ms.util.properties as properties


if __name__ == "__main__":
    t = Tail(properties.get_default_config("influxdb.master.log"))
    t.register_callback(deal.process)
    t.follow()
