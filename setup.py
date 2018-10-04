#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement

from setuptools import setup, find_packages

with open('README.rst') as fl:
    LONG_DESCRIPTION = fl.read()

with open('LICENSE') as fl:
    LICENSE = fl.read()

setup(
    name='CurrencyConverter',
    version='0.0.1',
    author='Fabio Curti',
    author_email='fabio.curti@gmail.com',
    url='https://github.com/fcurti/currencyConverter',
    description='A pythonic currency converter with Docker containerization and unit test',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'currencyConverter=currencyConverter.__main__:main'
        ]
    },
)
