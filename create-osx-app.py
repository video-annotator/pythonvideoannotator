
"""
Create a stand-alone Mac OS X app using py2app
To be used like this:

(from the pybpod-gui-plugin folder)
$: pyenv activate pybpod-gui-py3.5.3 # do this if you use pyenv virtualenv
$: pip install -r requirements-dev-YOURNAME.txt 

(from this file folder)
$: python create-osx-app.py py2app   (to build the app)
$: hdiutil create dist/$PROJECT_NAME.dmg -srcfolder dist/$PROJECT_NAME.app/


WARN: DO NOT FORGET TO UPDATE VERSION BEFORE RUNNING THIS SCRIPT!!!!

IF YOU NEED MATPLOTLIB, YOU MAY NEED THE LATEST VERSION OF py2app
"SyntaxError: 'yield' inside async function"
https://github.com/pyinstaller/pyinstaller/commit/48d5554ae74c2759d1fc099d4b2546288cad59fb
https://github.com/pyinstaller/pyinstaller/issues/2434
Solution:
pip install py2app

"""

import os
from setuptools import setup
from shutil import copyfile, copytree
from os import getcwd
from pathlib import Path

import re

version = ''
with open('pythonvideoannotator/__init__.py', 'r') as fd: 
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
		fd.read(), re.MULTILINE).group(1)
if not version: raise RuntimeError('Cannot find version information')

DIST_DIR = os.path.join( os.getcwd(), '..','videoannotator-build', 'dist')
BUILD_DIR = os.path.join( os.getcwd(), '..','videoannotator-build','build')

MAIN_SCRIPT_PATH = ['pythonvideoannotator/__main__.py']
DATA_FILES = []
PACKAGES = [
	'PyQt5', 'pyforms', 'pysettings', 'loggingbootstrap', 
	'mcvapi','mcvgui','geometry_designer',
	'pythonvideoannotator', 'pythonvideoannotator_models', 'pythonvideoannotator_models_gui',
	'pythonvideoannotator_module_importexport', 	'pythonvideoannotator_module_virtualobjectgenerator', 
	'pythonvideoannotator_module_motioncounter', 	'pythonvideoannotator_module_distances', 
	'pythonvideoannotator_module_pathmap', 			'pythonvideoannotator_module_smoothpaths', 
	'pythonvideoannotator_module_createpaths', 		'pythonvideoannotator_module_backgroundfinder', 
	'pythonvideoannotator_module_contoursimages', 	'pythonvideoannotator_module_regionsfilter', 
	'pythonvideoannotator_module_tracking', 		'pythonvideoannotator_module_timeline', 
	'pythonvideoannotator_module_patheditor'
]
INCLUDES = []
EXCLUDES = []

APP_VERSION = version

EXECUTABLE_NAME = "videoannotator-{version}".format(version=APP_VERSION)

OPTIONS = {
	'argv_emulation': True,
	'bdist_base': BUILD_DIR, 
	'dist_dir':   DIST_DIR,
	'compressed': False,
	'optimize': 0,
	'packages': PACKAGES,
	'includes': INCLUDES,
	'excludes': EXCLUDES,
	'iconfile': os.path.join('build_settings','osx','cf_icon_512x512.icns'),
	'strip': True,  # strip debug and local symbols from output (default is True for compatibility)
	'plist': {
		'CFBundleName': EXECUTABLE_NAME,
		'CFBundleDisplayName': EXECUTABLE_NAME,
		'CFBundleGetInfoString': "CF Scientific Software Platform",
		'CFBundleIdentifier': "org.champalimaud.swp.pythonvideoannotator",
		'CFBundleVersion': APP_VERSION,
		'CFBundleShortVersionString': APP_VERSION,
		'NSHumanReadableCopyright': u"Copyright (C) 2007 Free Software Foundation, Inc."
	}
}

setup(
	name=EXECUTABLE_NAME,
	app=MAIN_SCRIPT_PATH,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)

#settings_dest_path = os.path.join(DIST_DIR,EXECUTABLE_NAME,'.app/Contents/Resources/lib/python3.5/user_settings.py')
#copytree('simple_user_settings.py', settings_dest_path)



print("hdiutil create {0}/{1}.dmg -srcfolder {0}/{1}.app/".format(DIST_DIR, EXECUTABLE_NAME))
os.system("hdiutil create {0}/{1}.dmg -srcfolder {0}/{1}.app/".format(DIST_DIR, EXECUTABLE_NAME))