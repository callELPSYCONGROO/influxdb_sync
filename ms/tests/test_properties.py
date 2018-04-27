#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ms.util.properties import Properties
import ms.util.properties as properties

p = Properties('../../config/config.properties')
print(properties.get_default_config("task.wait.time"))

print(p.get('ms.db.status.log.path'))
