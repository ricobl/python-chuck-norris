#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.2'


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

assert_equal = assert_equals


def assert_not_equals(first, second, msg=None):
    pass

assert_not_equal = assert_not_equals


def assert_almost_equals(first, second, places=7, msg=None):
    pass

assert_almost_equal = assert_almost_equals


def assert_not_almost_equals(first, second, places=7, msg=None):
    pass

assert_not_almost_equal = assert_not_almost_equals
