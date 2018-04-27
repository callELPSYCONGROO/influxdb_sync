#! /usr/bin/env python
# -*- coding: utf-8 -*-


import ms.entity.record as record


f = "map[precision:[ns] rp:[sdd] consistency:[all] db:[ceshi]]"
b = " cpu,host=serverF,region=us-west4 value=0.64 1434055562000000101"
record.parse_body(b)
# record.parse_form(f)

p = {}
p["a"] = 1
p["b"] = {}
p["b"]["b1"] = 11
# print(p)
