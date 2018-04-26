#! /usr/bin/env python
# -*- coding: utf-8 -*-


from fileio import FileIO

f = FileIO("./record/index.ms")
print(f.read())
f.write("a解放看")
print(f.read())
