#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = "Carlos Mão de Ferro"
__copyright__ = ""
__credits__ = "Carlos Mão de Ferro"
__license__ = "MIT"
__version__ = "0.0"
__maintainer__ = ["Ricardo Ribeiro", "Carlos Mão de Ferro"]
__email__ = ["ricardojvr at gmail.com", "cajomferro at gmail.com"]
__status__ = "Development"
__updated__ = "2016-02-25"

from setuptools import setup, find_packages
import re

version = ''
with open('pycontrolgui/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(

    name='pythonVideoAnnotator',
    version=version,
    description=""" Python Video Annotator is a standalone application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos. """,
    author='Ricardo Ribeiro',
    author_email='rribeiro@neuro.fchampalimaud.org',
    license='MIT',
    url='https://github.com/UmSenhorQualquer/pythonVideoAnnotator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
    install_requires=[
        'pyforms == 0.1.4.dev7'
    ],
    entry_points={
        'console_scripts': [
            'pythonVideoAnnotator=pythonvideoannotator.__main__',
        ],
    }
)
