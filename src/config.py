#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config:
    def __init__(self):
        self.production = Config.Database("127.0.0.1", "3306", "family_coin", "family_coin")

    class Database:
        def __init__(self, address, port, user_name, password):
            self.address = address
            self.port = port
            self.user_name = user_name
            self.password = password


config = Config()


def production():
    return None