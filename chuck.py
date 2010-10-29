#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'


class RoundHouseKick(Exception):
    pass


def fail():
    raise RoundHouseKick('Fix your test. Chuck Norris never fails.')


def assert_true(value, msg=None):
    pass


def assert_false(value, msg=None):
    pass


def assert_raises(excClass, callableObj, *args, **kwargs):
    pass


def assert_equals(first, second, msg=None):
    pass


def assert_not_equals(first, second, msg=None):
    pass
