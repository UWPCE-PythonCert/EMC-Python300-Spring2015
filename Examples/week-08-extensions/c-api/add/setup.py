#!/usr/bin/env python
import warnings
from setuptools import setup, Extension

with warnings.catch_warnings():
    setup(
        name='Cadd',
        version='1.0',
        description='simple c extension for an example',
        ext_modules=[Extension('add', sources=['add.c'])],
    )
