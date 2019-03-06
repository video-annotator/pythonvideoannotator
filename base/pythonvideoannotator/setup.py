#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

with open('pythonvideoannotator/__init__.py', 'r') as fd:
    content = fd.read()
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

setup(
    name='Python video annotator',
    version=version,
    description="""""",
    author=['Ricardo Ribeiro'],
    author_email='ricardojvr@gmail.com',
    url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-models',
    packages=find_packages(),
    install_requires=[
        'simplejson',
        'pypi-xmlrpc',
        'pyforms-gui',
        'send2trash',
        'scipy',
        'sklearn',
        'confapp',
        'logging-bootstrap',
        'mcv-gui',
        'geometry-designer',
        'modular-computer-vision-api',
        'modular-computer-vision-api-gui',
        'python-video-annotator',
        'python-video-annotator-models',
        'python-video-annotator-models-gui',
        'python-video-annotator-module-tracking',
        'python-video-annotator-module-eventstats',
        'python-video-annotator-module-import-export',
        'python-video-annotator-module-regions-filter',
        'python-video-annotator-module-background-finder',
        'python-video-annotator-module-virtual-object-generator',
        'python-video-annotator-module-timeline',
        'python-video-annotator-module-smooth-paths',
        'python-video-annotator-module-motion-counter',
        'python-video-annotator-module-create-paths',
        'python-video-annotator-module-path-editor',
        'python-video-annotator-module-distances',
        'python-video-annotator-module-find-orientation',
        'python-video-annotator-module-contours-images',
        'python-video-annotator-module-path-map'
    ],
    entry_points={
        'console_scripts': [
            'start-video-annotator=pythonvideoannotator.__main__:start',
        ],
    },
    package_data={'pythonvideoannotator': [
        'resources/icons/*.png',
        'resources/themes/default/*.css',
        ]
    },
)
