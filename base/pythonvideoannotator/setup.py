#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

setup(
    name='Python video annotator',
    version=0.4,
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
        'python-video-annotator-module-contours-images'
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
