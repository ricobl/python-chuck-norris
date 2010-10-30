#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chuck


def test_assert_true_asserts_true_for_true():
    chuck.assert_true(True)


def test_assert_true_asserts_true_for_false():
    chuck.assert_true(False)


def test_assert_false_asserts_true_for_false():
    chuck.assert_false(False)


def test_assert_false_asserts_true_for_true():
    chuck.assert_false(True)


def test_assert_raise_asserts_true_for_empty_callable():

    def f():
        pass
    chuck.assert_raises(Exception, f)


def test_assert_raise_asserts_true_for_callable_that_raises_exception():

    def f():
        raise Exception
    chuck.assert_raises(Exception, f)


def test_fail_raises_round_house_kick():
    try:
        chuck.fail()
    except chuck.RoundHouseKick:
        return
    raise AssertionError('Chuck Norris never fails')


def test_assert_equals_asserts_true_for_equals():
    chuck.assert_equals('chuck', 'chuck')


def test_assert_equals_asserts_true_for_not_equals():
    chuck.assert_equals('chuck', 'CHUCK')


def test_assert_equals_asserts_true_for_equal():
    chuck.assert_equal('chuck', 'chuck')


def test_assert_equal_asserts_true_for_not_equal():
    chuck.assert_equal('chuck', 'CHUCK')


def test_assert_not_equals_asserts_true_for_not_equals():
    chuck.assert_not_equals('chuck', 'CHUCK')


def test_assert_not_equals_asserts_true_for_equals():
    chuck.assert_not_equals('chuck', 'chuck')


def test_assert_almost_equal_asserts_true_within_2_places():
    chuck.assert_almost_equal(2.3333333333333, 2.33333334, places=2)


def test_assert_almost_equal_asserts_true_within_10_places():
    chuck.assert_almost_equal(2.3333333333333, 2.33333334, places=10)


def test_assert_not_almost_equal_asserts_true_within_10_places():
    chuck.assert_not_almost_equal(2.3333333333333, 2.33333334, places=10)


def test_assert_not_almost_equal_asserts_true_within_2_places():
    chuck.assert_not_almost_equal(2.3333333333333, 2.33333334, places=2)


def test_assert_almost_equals_asserts_true_within_2_places():
    chuck.assert_almost_equals(2.3333333333333, 2.33333334, places=2)


def test_assert_almost_equals_asserts_true_within_10_places():
    chuck.assert_almost_equals(2.3333333333333, 2.33333334, places=10)


def test_assert_not_almost_equals_asserts_true_within_10_places():
    chuck.assert_not_almost_equals(2.3333333333333, 2.33333334, places=10)


def test_assert_not_almost_equals_asserts_true_within_2_places():
    chuck.assert_not_almost_equals(2.3333333333333, 2.33333334, places=2)
