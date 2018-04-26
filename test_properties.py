#! /usr/bin/env python
# -*- coding: utf-8 -*-

from properties import Properties

p = Properties('./config/config.properties')
properties = p.get_properties()

print(p.get('task.wait.time'))
