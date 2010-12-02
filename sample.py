# -*- coding: utf-8 -*-

import chuck

def test_something():
    print 'Before'
    assert False, 'Should not raise an error'
    print 'After'

def do_something():
    try:
        assert False, 'Should raise an error'
    except AssertionError:
        return
    raise AssertionError('Error not raised')

test_something()
do_something()
