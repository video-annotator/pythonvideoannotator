#!/usr/bin/python
# -*- coding: utf-8 -*-


from ast import literal_eval
from setuptools import setup, find_packages
import re

PROJECT_PACKAGE = 'pythonvideoannotator'

with open('{0}/__init__.py'.format(PROJECT_PACKAGE), 'r') as fd:
    project_metadata = fd.read()
    try:
        __version__ = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __version__ = '0.0'
    try:
        __copyright__ = re.search(r'^__copyright__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __copyright__ = ''
    try:
        __license__ = re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __license__ = ''
    try:
        __status__ = re.search(r'^__status__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __status__ = ''
    try:
        line = literal_eval(re.search(r'^__author__\s*=\s*(.+)', project_metadata, re.MULTILINE).group(1))
        if isinstance(line, list):
            __author__ = line
        else:
            __author__ = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __author = ''
    try:
        line = literal_eval(re.search(r'^__credits__\s*=\s*(.+)', project_metadata, re.MULTILINE).group(1))
        if isinstance(line, list):
            __credits__ = line
        else:
            __credits__ = re.search(r'^__credits__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __credits__ = ''
    try:
        line = literal_eval(re.search(r'^__maintainer__\s*=\s*(.+)', project_metadata, re.MULTILINE).group(1))
        if isinstance(line, list):
            __maintainer__ = line
        else:
            __maintainer__ = re.search(r'^__maintainer__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __maintainer__ = ''
    try:
        line = literal_eval(re.search(r'^__email__\s*=\s*(.+)', project_metadata, re.MULTILINE).group(1))
        if isinstance(line, list):
            __email__ = line
        else:
            __email__ = re.search(r'^__email__\s*=\s*[\'"]([^\'"]*)[\'"]', project_metadata, re.MULTILINE).group(1)
    except:
        __email__ = ''


setup(

    name='pythonVideoAnnotator',
    version=__version__,
    description=""" Python Video Annotator is a standalone application written in python, which provides a GUI for users to analyze and to take notes of events occurred in the videos. """,
    author=__author__,
    author_email=__email__,
    license=__license__,
    url='https://github.com/UmSenhorQualquer/pythonVideoAnnotator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
    install_requires=[
        'pyforms == 0.1.5'
    ],
    entry_points={
        'console_scripts': [
            'pythonVideoAnnotator=pythonvideoannotator.__main__',
        ],
    }
)
