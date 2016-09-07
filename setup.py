#!/usr/bin/python2
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
import re

version = ''
with open('pythonvideoannotator/__init__.py', 'r') as fd: version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                                                                      fd.read(), re.MULTILINE).group(1)
if not version: raise RuntimeError('Cannot find version information')

requirements = [
	'pysettings>=0.1',
	'pyforms>=0.1.7.2',
	'pyforms_generic_editor>=0.1',
	'logging-bootstrap>=0.1',
]

setup(

	name='pythonVideoAnnotator',
	version=version,
	description=""" Python Video Annotator is a standalone application written in python, which provides a GUI for users to analyze and to take notes of events occurred in the videos. """,
	author=['Ricardo Ribeiro', 'Carlos Mão de Ferro'],
	author_email=['ricardojvr@gmail.com', 'cajomferro@gmail.com'],
	license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
	url='https://github.com/UmSenhorQualquer/pythonVideoAnnotator',
	packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
	# install_requires=requirements,
	entry_points={
		'console_scripts': [
			'pythonVideoAnnotator=pythonvideoannotator.__main__',
		],
	}
)
