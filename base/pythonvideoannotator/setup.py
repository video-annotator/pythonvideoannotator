#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

setup(
	name='Python video annotator',
	version=0.0,
	description="""""",
	author=['Ricardo Ribeiro'],
	author_email='ricardojvr@gmail.com',
	url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-models',
	packages=find_packages(),
	install_requires=[
        'simplejson',
        'pyforms-gui',
        'send2trash',
        'scipy',
        'sklearn'
    ]
)
