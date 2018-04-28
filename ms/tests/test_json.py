#! /usr/bin/env python
# -*- coding: utf-8 -*-


import ms.entity.record as record


f = "map[precision:[ns] rp:[sdd] consistency:[all] db:[ceshi]]"
b = " cpu,host=serverF,region=us-west4 value=0.64 1434055562000000101"
# record.parse_form(f)

p = {}
p["a"] = 1
p["b"] = {}
p["b"]["b1"] = 11
# print(p)

oneline = '{"timeindex": 1610, "host": "127.0.0.1", "username": "-", method: "POST", "path": "/query", "uri": "/query?chunked=true&db=ceshi&epoch=ns&q=select+%2A+from+cpu", "form" :"map[db:[ceshi] epoch:[ns] q:[select * from cpu] chunked:[true]]", "body": "","proto": "HTTP/1.1", "status": "200", "size": "539", "referer": "-", "agent": "InfluxDBShell/unknown", "reqId": "e20f35ab-4aa6-11e8-8008-000000000000"}'
# json_obj = json.loads(oneline)
# r = record.Record(json_obj)
# print(r)


class Tpp(object):

    def __init__(self):
        self.a = "/query?chunked=true&db=ceshi&epoch=ns&q=select+%2A+from+cpu"
        self.b = "127.0.0.1"
        self.c = "map[db:[ceshi] epoch:[ns] q:[select * from cpu] chunked:[true]]"


# jjj = '{"a": "/query?chunked=true&db=ceshi&epoch=ns&q=select+%2A+from+cpu", "c": "map[db:[ceshi] epoch:[ns] q:[select * from cpu] chunked:[true]]", "b": "127.0.0.1"}'
jjj = '{"timeindex":57197063,"host":"127.0.0.1","username":"-","method":"POST","path":"/query","uri":"/query?chunked=true&db=ceshi&epoch=ns&q=SHOW+MEASUREMENTS","form":"map[chunked:[true] db:[ceshi] epoch:[ns] q:[SHOW MEASUREMENTS]]","body":" cpu,host=serverA,region=us-west value=0.64,value2=0.86 1434055562000000200;","proto":"HTTP/1.1","status":"200","size":"57","referer":"-","agent":"InfluxDBShell/unknown","reqId":"217c4351-4ac6-11e8-800c-000000000000"}'
# print(Tpp().__dict__)
# print(json.dumps(Tpp().__dict__))
# print(json.loads(json.dumps(Tpp().__dict__)))
# print("*********************")
r = record.bulid(jjj)
print(r.body)
