#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, id, name, display_name):
        self.id = id
        self.name = name
        self.display_name = display_name

    def getResult(self):
        return [self.id, self.name, self.display_name]
