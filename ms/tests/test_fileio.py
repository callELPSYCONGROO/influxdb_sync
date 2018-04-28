#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ms.util.fileio import FileIO
import ms.util.fileio as fileio

f = FileIO("../../record/index.ms")
print(f.read())
# f.write(123)
f.write(str(123))
print(f.read())

# print(fileio.read_index())
# print(fileio.write_index(1232))
