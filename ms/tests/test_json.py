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

oneline = '{"timeindex": 1610, "host": "127.0.0.1", "username": "-", "method": "POST", "path": "/query", "uri": "/query?chunked=true&db=ceshi&epoch=ns&q=select+%2A+from+cpu", "form" :"map[db:[ceshi] epoch:[ns] q:[select * from cpu] chunked:[true]]", "body": "","proto": "HTTP/1.1", "status": "200", "size": "539", "referer": "-", "agent": "InfluxDBShell/unknown", "reqId": "e20f35ab-4aa6-11e8-8008-000000000000"}'
# json_obj = json.loads(oneline)
# r = record.Record(json_obj)
# print(r)


class Tpp(object):

    def __init__(self):
        self.a = "/query?chunked=true&db=ceshi&epoch=ns&q=select+%2A+from+cpu"
        self.b = "127.0.0.1"
        self.c = "map[db:[ceshi] epoch:[ns] q:[select * from cpu] chunked:[true]]"


jjj = '{"timeindex":345921735,"host":"127.0.0.1","username":"ireader","method":"POST","path":"/query","uri":"/query?chunked=true&db=ceshi&epoch=ns&q=DROP+DATABASE+asd","form":"map[chunked:[true] db:[ceshi] epoch:[ns] q:[DROP DATABASE asd]]","body":"","proto":"HTTP/1.1","status":"403","size":"127","referer":"-","agent":"InfluxDBShell/unknown","reqId":"2d6c9ba2-4f3e-11e8-8011-000000000000"}'
# jjj = '{"timeindex":114475284,"host":"127.0.0.1","username":"-","method":"POST","path":"/write","uri":"/write?consistency=all&db=ceshi&precision=ns&rp=","form":"map[consistency:[all] db:[ceshi] precision:[ns] rp:[]]","body":" cpu,host=serverA,region=us-west value=0.64,value2=0.86 1434055562000000200;","proto":"HTTP/1.1","status":"204","size":"0","referer":"-","agent":"InfluxDBShell/unknown","reqId":"89384d42-4ac0-11e8-800b-000000000000"}'
# jjj = '{"timeindex":416067558,"host":"127.0.0.1","username":"-","method":"GET","path":"/ping","uri":"/ping","form":"map[]","body":"","proto":"HTTP/1.1","status":"204","size":"0","referer":"-","agent":"InfluxDBShell/unknown","reqId":"a922cdcb-4f39-11e8-8001-000000000000"}'
# jjj = '{"timeindex":458946112,"host":"127.0.0.1","username":"-","method":"POST","path":"/query","uri":"/query?db=&epoch=ns&q=SHOW+DATABASES","form":"map[db:[] epoch:[ns] q:[SHOW DATABASES]]","body":"","proto":"HTTP/1.1","status":"200","size":"139","referer":"-","agent":"InfluxDBShell/unknown","reqId":"cb912125-4ab6-11e8-8003-000000000000"}'
# jjj = '{"timeindex":57197063,"host":"127.0.0.1","username":"-","method":"POST","path":"/query","uri":"/query?chunked=true&db=ceshi&epoch=ns&q=SHOW+MEASUREMENTS","form":"map[chunked:[true] db:[ceshi] epoch:[ns] q:[SHOW MEASUREMENTS]]","body":" cpu,host=serverA,region=us-west value=0.64,value2=0.86 1434055562000000200;","proto":"HTTP/1.1","status":"200","size":"57","referer":"-","agent":"InfluxDBShell/unknown","reqId":"217c4351-4ac6-11e8-800c-000000000000"}'
# print(Tpp().__dict__)
# print(json.dumps(Tpp().__dict__))
# print(json.loads(json.dumps(Tpp().__dict__)))
print("*********************")
r = record.bulid(jjj)
print(r.body)
print(r.form)
print(not r.success())

# asd = 'q:[SHOW MEASUREMENTS]'
# print(re.search("(?<=\\[)[\\s\\S]*(?=\\])", asd, flags=re.IGNORECASE).group())

form = {'q': 'DROP DATABASE lkl', 'epoch': 'ns', 'chunked': 'true', 'db': 'ceshi'}
# print(((constant.CREATE in form["q"].upper()) or (constant.DROP in form["q"].upper()) or (constant.DELETE in form["q"].upper())) is False)
