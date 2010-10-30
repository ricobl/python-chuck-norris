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

def test_assert_equals_assert_true_for_equal():
    from chuck import assert_equal
    assert assert_equal('chuck', 'chuck')

def test_assert_equal_asserts_true_for_not_equal():
    from chuck import assert_equal
    assert assert_equal('chuck', 'CHUCK')

def test_assert_not_equals_asserts_true_for_not_equals():
    from chuck import assert_not_equals
    assert assert_not_equals('chuck', 'CHUCK')

def test_assert_not_equals_asserts_true_for_equals():
    from chuck import assert_not_equals
    assert assert_not_equals('chuck', 'chuck')

def test_assert_not_equals_asserts_true_for_not_equals():
    from chuck import assert_not_equal
    assert assert_not_equal('chuck', 'CHUCK')

def test_assert_not_equals_asserts_true_for_equals():
    from chuck import assert_not_equal
    assert assert_not_equal('chuck', 'chuck')

def test_assert_almost_equal_asserts_true_within_2_places():
    from chuck import assert_almost_equal
    assert assert_almost_equal(2.3333333333333, 2.33333334, places=2)

def test_assert_almost_equal_asserts_true_within_10_places():
    from chuck import assert_almost_equal
    assert assert_almost_equal(2.3333333333333, 2.33333334, places=10)

def test_assert_not_almost_equal_asserts_true_within_10_places():
    from chuck import assert_not_almost_equal
    assert assert_not_almost_equal(2.3333333333333, 2.33333334, places=10)

def test_assert_not_almost_equal_asserts_true_within_2_places():
    from chuck import assert_not_almost_equal
    assert assert_not_almost_equal(2.3333333333333, 2.33333334, places=2)

def test_assert_almost_equals_asserts_true_within_2_places():
    from chuck import assert_almost_equals
    assert assert_almost_equals(2.3333333333333, 2.33333334, places=2)

def test_assert_almost_equals_asserts_true_within_10_places():
    from chuck import assert_almost_equals
    assert assert_almost_equals(2.3333333333333, 2.33333334, places=10)

def test_assert_not_almost_equals_asserts_true_within_10_places():
    from chuck import assert_not_almost_equals
    assert assert_not_almost_equals(2.3333333333333, 2.33333334, places=10)

def test_assert_not_almost_equals_asserts_true_within_2_places():
    from chuck import assert_not_almost_equals
    assert assert_not_almost_equals(2.3333333333333, 2.33333334, places=2)



