#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dataset
from config import config

db = dataset.connect('mysql://' + config.production.address + 'root@127.0.0.1/information_schema')

table = db['user']
results = table.find(CHARACTER_SET_NAME='utf8', order_by='-ID', _limit=3)
for r in results:
    print(r)
