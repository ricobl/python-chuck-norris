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


def test_assert_not_equals_asserts_true_for_not_equals():
    chuck.assert_not_equals('chuck', 'CHUCK')


def test_assert_not_equals_asserts_true_for_equals():
    chuck.assert_not_equals('chuck', 'chuck')
