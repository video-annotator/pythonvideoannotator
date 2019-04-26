#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

VERSION = 3.106

# REQUIREMENTS BEGIN
REQUIREMENTS = [
    "geometry_designer==0.3",
    "modular-computer-vision-api-gui==0.2",
    "pyforms-gui==4.9",
    "modular-computer-vision-api==0.2",
    "mcv-gui==0.1",
    "python-video-annotator-models-gui==0.4",
    "python-video-annotator-models==0.4",
    "python-video-annotator-module-timeline==0.3",
    "python-video-annotator-module-eventstats==0.2",
    "python-video-annotator-module-virtual-object-generator==0.3",
    "python-video-annotator-module-deeplab==0.3",
    "python-video-annotator-module-contours-images==0.2",
    "python-video-annotator-module-tracking==0.3",
    "python-video-annotator-module-smooth-paths==0.2",
    "python-video-annotator-module-distances==0.2",
    "python-video-annotator-module-path-map==0.3",
    "python-video-annotator-module-motion-counter==0.2",
    "python-video-annotator-module-create-paths==0.2",
    "python-video-annotator-module-regions-filter==0.2",
    "python-video-annotator-module-import-export==0.2",
    "python-video-annotator-module-background-finder==0.2",
    "python-video-annotator-module-find-orientation==0.2",
    "python-video-annotator-module-path-editor==0.2"
]
# REQUIREMENTS END

setup(
    name='Python video annotator',
    version=VERSION,
    description="""""",
    author=['Ricardo Ribeiro'],
    author_email='ricardojvr@gmail.com',
    url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-models',
    packages=find_packages(),
    install_requires=[
        'simplejson',
        'pypi-xmlrpc',
        'send2trash',
        'scipy',
        'sklearn',
        'confapp',
    ] + REQUIREMENTS,
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
