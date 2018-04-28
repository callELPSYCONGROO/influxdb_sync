#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ms.service.deal as deal
from influxdb import InfluxDBClient

# client = InfluxDBClient('118.24.160.252', 8086, 'iwriter', 'iwriter')
json_body = [
    {
        "measurement": "cpu",
        "tags": {
            "host": "serverA",
            "region": "us-west1"
        },
        "fields": {
            "Float_value": 0.64,
            "Int_value": 3,
            "String_value": "Text",
            "Bool_value": True
        }
    }
]
# client.switch_database('ceshi')
# client.write_points(json_body)
# query = "SELECT * FROM cpu WHERE time > 1434055562000000100"
# client.switch_database('ceshi')
# result = client.query(query)
# print(result)


deal.process("")
