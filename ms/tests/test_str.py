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

