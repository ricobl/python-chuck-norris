#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equals
from mox import Mox

import chuck

# Trick chuck to skip asserts on functions
# that starts with "verify" instead of "test"
chuck._prefix = 'verify'

filename = 'fake_module.py'


def test_module_cache():
    chuck._load_module(filename)
    yield cache_loads_file
    yield cache_finds_lines_with_asserts


def cache_loads_file():
    assert filename in chuck._cache


def cache_finds_lines_with_asserts():
    lines = chuck._load_module(filename)
    assert_equals(lines[0], 4)


def test_assert_skipping():
    def verify_assert():
        assert False, 'Should not fail'
        return
    verify_assert()

