#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chuck import __version__
from setuptools import setup

setup(
    name='python-chuck-norris',
    version=__version__,
    description='Chuck Norris assertions to make all your tests pass',
    author=u'Enrico Batista da Luz',
    author_email='rico.bl@gmail.com',
    url='http://github.com/ricobl/python-chuck-norris',
    py_modules=['chuck'],
)

