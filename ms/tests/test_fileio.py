#! /usr/bin/env python
# -*- coding: utf-8 -*-


from ms.util.fileio import FileIO
import ms.util.fileio as fileio

f = FileIO("../../record/index.ms")
print(f.read())
f.write("a解放看")
print(f.read())

print(fileio.read_index())