"""
Create a stand-alone Mac OS X app using py2app
To be used like this:
$ python setup.py build         (to update the docs)
$ python create-osx-app.py py2app   (to build the app)
"""

import os
from setuptools import setup

BUILD_SETTINGS_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = 'pythonVideoAnnotator'
MAIN_SCRIPT_PATH = os.path.join(BUILD_SETTINGS_PATH, '../../pythonvideoannotator/__main__.py')


APP = [MAIN_SCRIPT_PATH]
DATA_FILES = []
PACKAGES = ['distutils', 'PyQt4', 'pyforms', 'visvis', 'pythonvideoannotator']
INCLUDES= []

OPTIONS = {
   'argv_emulation': True,
   'compressed' : False,
   'optimize': 0,
   'packages': PACKAGES,
   'includes': INCLUDES,
   'iconfile': os.path.join(BUILD_SETTINGS_PATH, 'cf_icon_128x128.icns'),
}

setup(
   name=PROJECT_NAME,
   app=APP,
   options={'py2app': OPTIONS},
   setup_requires=['py2app'],
)

