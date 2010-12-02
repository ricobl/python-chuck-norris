#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.3'

import sys

_cache = {}
_source = {}
_prefix = 'test'


def _load_module(filename):
    if filename not in _cache:
        with open(filename) as f:
            contents = f.readlines()
            _source[filename] = contents
            _cache[filename] = [n + 1 for n, l in enumerate(contents)
                                if 'assert' in l]
    return _cache[filename]


def _trace(frame, event, arg):
    # Ignore function call line
    if event == 'call':
        return _trace

    # Get lines with asserts for the file
    filename = frame.f_code.co_filename
    lines = _load_module(filename)
    ln = frame.f_lineno - 1

    # Ignore module
    if frame.f_code.co_name == '<module>':
        return _trace
    # Ignore non-test functions
    if not frame.f_code.co_name.startswith(_prefix):
        return _trace

    if frame.f_lineno in lines:
        frame.f_lineno = frame.f_lineno + 1

        #if event == 'return':
        #    #print dir(frame.f_back)
        #    #print frame.f_back.f_lineno, frame.f_back.f_lasti
        #    #print frame.f_lineno, frame.f_lasti
        #    frame.f_back.f_lineno = frame.f_back.f_lineno + 1
        #else:

    return _trace

sys.settrace(_trace)
frame = sys._getframe().f_back
while frame:
    frame.f_trace = _trace
    frame = frame.f_back
