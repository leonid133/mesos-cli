#!/usr/bin/env python
from setuptools import setup
import unittest


with open("README.md", 'r') as f:
    long_description = f.read()


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='mesos_http_client',
    version='0.1',
    description='CLI for Mesos HTTP API',
    long_description=long_description,
    author='Leonid Blokhin',
    author_email='leonid.blohin@gmail.com',
    install_requires=['requests>=2.0.0', 'requests_mock', 'simplejson'],
    url='https://github.com/leonid133/mesos-cli',
    packages=['mesos_http_client'],
    test_suite='setup.test_suite',
    classifiers=[
        'Programming Language :: Python'
    ]
)
