#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re, os

PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(PACKAGE_PATH, 'pythonvideoannotator','__init__.py'), 'r') as fd:
    content = fd.read()
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)

with open(os.path.join(PACKAGE_PATH, '..','..','README.md'), 'r') as fd:
    long_description = fd.read()


# REQUIREMENTS BEGIN
REQUIREMENTS = [
    "geometry_designer==0.3.36",
	"modular-computer-vision-api-gui==0.2.29",
	"confapp==1.0.9",
	"pyforms-gui==4.904.147",
	"modular-computer-vision-api==0.2.26",
	"python-video-annotator-models-gui==0.6.57",
	"python-video-annotator-models==0.7.74",
	"python-video-annotator-module-timeline==0.5.24",
	"python-video-annotator-module-eventstats==0.4.13",
	"python-video-annotator-module-virtual-object-generator==0.5.24",
	"python-video-annotator-module-deeplab==0.901.19",
	"python-video-annotator-module-contours-images==0.4.26",
	"python-video-annotator-module-tracking==0.5.36",
	"python-video-annotator-module-smooth-paths==0.4.17",
	"python-video-annotator-module-distances==0.4.16",
	"python-video-annotator-module-path-map==0.5.14",
	"python-video-annotator-module-motion-counter==0.4.24",
	"python-video-annotator-module-create-paths==0.4.13",
	"python-video-annotator-module-regions-filter==0.4.16",
	"python-video-annotator-module-idtrackerai==0.0.41",
	"python-video-annotator-module-import-export==0.4.21",
	"python-video-annotator-module-background-finder==0.4.19",
	"python-video-annotator-module-find-orientation==0.4.16",
	"python-video-annotator-module-path-editor==0.4.26"
]
# REQUIREMENTS END

setup(
    name='Python video annotator',
    version=version,
    description="""""",
    author=['Ricardo Ribeiro'],
    author_email='ricardojvr@gmail.com',
    url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-models',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
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
