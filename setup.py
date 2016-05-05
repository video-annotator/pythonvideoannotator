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

with open('pythonvideoannotator/__init__.py', 'r') as fd:
    __version__     = eval(fd.readline().split('=')[1])
    __author__      = eval(fd.readline().split('=')[1])
    __credits__     = eval(fd.readline().split('=')[1])
    __license__     = eval(fd.readline().split('=')[1])
    __maintainer__  = eval(fd.readline().split('=')[1])
    __email__       = eval(fd.readline().split('=')[1])
    __status__      = eval(fd.readline().split('=')[1])


setup(

    name='pythonVideoAnnotator',
    version=__version__,
    description=""" Python Video Annotator is a standalone application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos. """,
    author=__author__,
    author_email=__email__,
    license=__license__,
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
