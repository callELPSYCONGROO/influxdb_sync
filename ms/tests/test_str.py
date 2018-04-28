#! /usr/bin/env python
# -*- coding: utf-8 -*-


import re

s1 = "/query"
s2 = "/write"

if "query" in s1:
    print("s1 is query")
if "write" in s2:
    print("s2 is write")

q = "map[precision:[ns] rp:[] consistency:[all] db:[ceshi]]"
p = "map[]"


def parse_form(s):
    """
    form字符串转换为dict对象。
     # kwargs["form"]格式：   map[precision:[ns] rp:[sdd] consistency:[all] db:[ceshi]]
    """
    split = s[4:-1].split()
    d = {}
    for kv in split:
        k = re.search("\\w+", kv).group()
        print(k)
        v = re.search("(?<=\\[)\\w*(?=\\])", kv).group()
        print(v)
        d[k] = v
    return d


# parse_form(q)
print("*************")
# parse_form(p)
# print(parse_form(p))
# print(re.search("\\w+", " precision:[ns] ").group())
# print(re.search("(?<=\\[)\\w+(?=\\])", " precision:[ns] ").group())

ss = '{"timeindex":1635.213,"host":"127.0.0.1","username":"-",method:"POST","path":"/query","uri":"/query?chunked=true&db=ceshi&epoch=ns&q=SELECT+%2A+FROM+cpu","form":"map[epoch:[ns] q:[SELECT * FROM cpu] chunked:[true] db:[ceshi]]","body":"","proto":"HTTP/1.1","status":"200","size":"539","referer":"-","agent":"InfluxDBShell/unknown","reqId":"81c862fd-4a86-11e8-8003-000000000000"}'
# print(re.search("(?<=\"timeindex\":)\\w+.\\w+(?=,)", ss).group())

t = '{"timeindex":704297975,"host":"127.0.0.1","username":"-","method":"POST","path":"/write","uri":"/write?consistency=all&db=ceshi&precision=ns&rp=","form":"map[consistency:[all] db:[ceshi] precision:[ns] rp:[]]","body":" cpu,host=serverA,region=us-west value=0.64,value2=0.86 1434055562000000200'
print(re.search("(?<=\"timeindex\":)\\w+.\\w+(?=,)", t).group())
