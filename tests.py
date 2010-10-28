#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_assert_true_asserts_true_for_true():
    from chuck import assert_true
    assert assert_true(True)

def test_assert_true_asserts_true_for_false():
    from chuck import assert_true
    assert assert_true(False)

def test_assert_false_asserts_true_for_false():
    from chuck import assert_false
    assert assert_false(False)

def test_assert_false_asserts_true_for_true():
    from chuck import assert_false
    assert assert_false(True)

def test_assert_raise_asserts_true_for_empty_callable():
    from chuck import assert_raises
    def f():
        pass
    assert assert_raises(Exception, f)

def test_assert_raise_asserts_true_for_callable_that_raises_exception():
    from chuck import assert_raises
    def f():
        raise Exception
    assert assert_raises(Exception, f)

def test_fail_raises_import_error():
    try:
        from chuck import fail
    except ImportError:
        return
    raise AssertionError, 'Chuck-norris never fails'

def test_assert_equals_asserts_true_for_equals():
    from chuck import assert_equals
    assert assert_equals('chuck', 'chuck')

def test_assert_equals_asserts_true_for_not_equals():
    from chuck import assert_equals
    assert assert_equals('chuck', 'CHUCK')

def test_assert_not_equals_asserts_true_for_not_equals():
    from chuck import assert_not_equals
    assert assert_not_equals('chuck', 'CHUCK')

def test_assert_not_equals_asserts_true_for_equals():
    from chuck import assert_not_equals
    assert assert_not_equals('chuck', 'chuck')

