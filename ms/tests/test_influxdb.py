#! /usr/bin/env python
# -*- coding: utf-8 -*-

import ms.service.deal as deal
import ms.entity.record as record
from influxdb import InfluxDBClient

client = InfluxDBClient('120.79.70.87', 8086, 'iwriter', 'iwriter')
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


def _data2json(body):
    """
    将日志参数转换为接口参数json对象
    point = {
            "measurement": "",
            "tags": {},
            "fields": {}
    }
    """
    def _p(db):
        return {
            "measurement": db["db"] if "db" in db else "",
            "tags": db["tag"] if "tag" in db else {},
            "fields": db["field"] if "field" in db else {},
            "time": db["time"] if "time" in db else ""
        }
    return [_p(b) for b in body]


ol = '{"timeindex":437438427,"host":"127.0.0.1","username":"-","method":"POST","path":"/write","uri":"/write?consistency=all&db=ceshi&precision=ns&rp=","form":"map[consistency:[all] db:[ceshi] precision:[ns] rp:[]]","body":" cpu,host=serverA,region=us-west2 value=0.64 1434055562000000201;","proto":"HTTP/1.1","status":"204","size":"0","referer":"-","agent":"InfluxDBShell/unknown","reqId":"af40b385-4db8-11e8-8010-000000000000"}'
r = record.bulid(ol)
form = r.form
client.switch_database(form["db"])
print("*********************************")
if "rp" in form:
    print(r.get_rp() if "rp" in form else None)
print("*********************************")
client.write_points(_data2json(r.body),
                    time_precision=r.get_time_precision() if "precision" in form else None,
                    database=form["db"] if "db" in form else None,
                    retention_policy=r.get_rp() if "rp" in form else None)
# query = "SELECT * FROM cpu WHERE time > 1434055562000000100"
# client.switch_database('ceshi')
# result = client.query(query)
# print(result)


# deal.process("")
