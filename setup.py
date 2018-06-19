#!/usr/bin/env python

from setuptools import setup

setup(
    version='1.0.6',
    package_data={
        'nittygriddy': [
            'non-python-files/datasets.yml',
            'non-python-files/run.C',
            'non-python-files/GetSetting.C',
            # 'examples/flame_graph.png'
        ],
    },
    long_description=open('README.rst').read(),
    test_suite='nose.collector',
)
