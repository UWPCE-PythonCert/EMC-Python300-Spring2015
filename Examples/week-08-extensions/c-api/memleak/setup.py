#!/usr/bin/env python
import warnings
from setuptools import setup, Extension

"""
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
"""

setup(
    name='memleak',
    version='0.0.1',
    description='memleaks are fun -- high kicks!',
    ext_modules=[Extension('memleak', sources=['memleak.c'])],
)
