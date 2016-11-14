"""
Create a stand-alone Mac OS X app using py2app
To be used like this:
$: python setup.py build         (to update the docs)
$: python create-osx-app.py py2app   (to build the app)
$: hdiutil create dist/$PROJECT_NAME.dmg -srcfolder dist/$PROJECT_NAME.app/

WARNING:

py2app has a bug. On module build_app.py, line 178, put a try / except 
(os.symlink(os.path.basename(dest), link_dest))
https://bitbucket.org/ronaldoussoren/py2app/issues/159/fails-with-file-exists-while-copying

DO NOT FORGET TO INSTALL THIS APP ON PIP BEFORE RUNNING THIS SCRIPT!!!!

"""

import os
from setuptools import setup

BUILD_SETTINGS_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = 'pythonVideoAnnotator'
MAIN_SCRIPT_PATH = os.path.join(BUILD_SETTINGS_PATH, '../../pythonvideoannotator/__main__.py')


APP = [MAIN_SCRIPT_PATH]
DATA_FILES = []
PACKAGES = ['distutils', 'PyQt4', 'pyforms', 'visvis', 'pythonvideoannotator', 'pysettings', 'loggingbootstrap']
INCLUDES= []

OPTIONS = {
   'argv_emulation': True,
   'compressed' : False,
   'optimize': 0,
   'packages': ['distutils', 'PyQt4', 'pyforms', 'visvis', 'pysettings', 'pyforms_generic_editor', 'loggingbootstrap', 'pythonvideoannotator'],
   'includes': INCLUDES,
   'iconfile': os.path.join(BUILD_SETTINGS_PATH, 'cf_icon_128x128.icns'),
}

setup(
   name=PROJECT_NAME,
   app=APP,
   options={'py2app': OPTIONS},
   setup_requires=['py2app'],
)

