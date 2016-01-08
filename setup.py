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
__updated__ = "2016-01-08"

from setuptools import setup, find_packages

setup(

    name='pythonVideoAnnotator',
    version='1.0.0',
    description=""" Python Video Annotator is a standalone application written in python, which provides a GUI for users to analyse and to take notes of events occurred in the videos. """,
    author='Carlos Mao de Ferro',
    author_email='carlos.maodeferro@neuro.fchampalimaud.org',
    license='MIT',
    url='https://github.com/UmSenhorQualquer/pythonVideoAnnotator',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
    install_requires=[
        'pyforms == 0.1.3'
    ],
    entry_points={
        'console_scripts': [
            'pythonVideoAnnotator=pythonvideoannotator.__main__',
        ],
    }
)
