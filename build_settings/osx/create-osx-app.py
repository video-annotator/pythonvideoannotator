"""
Create a stand-alone Mac OS X app using py2app
To be used like this:
$: pyenv activate python-video-annotator-py3.5.3 # do this if you use pyenv virtualenv
$: python create-osx-app.py py2app   (to build the app)
$: hdiutil create dist/$PROJECT_NAME.dmg -srcfolder dist/$PROJECT_NAME.app/

DO NOT FORGET TO INSTALL THIS APP AND DEPENDENCIES ON PIP BEFORE RUNNING THIS SCRIPT!!!!

DO NOT FORGET TO UPDATE VERSION BEFORE RUNNING THIS SCRIPT!!!!

"""

import os
from setuptools import setup
from shutil import copyfile
import pythonvideoannotator as app_package

MAIN_SCRIPT_PATH = ['../../pythonvideoannotator/__main__.py']
DATA_FILES = []
PACKAGES = ['PyQt5',
            'OpenGL',
            'OpenGL_accelerate',
            'loggingbootstrap',
            'mcvapi',
            'mcvgui',
            'geometry_designer',
            'pyforms',
            'pythonvideoannotator',
            'pythonvideoannotator_models',
            'pythonvideoannotator_models_gui',
            'pythonvideoannotator_module_backgroundfinder',
            'pythonvideoannotator_module_backgroundfinder',
            'pythonvideoannotator_module_contoursimages',
            'pythonvideoannotator_module_createpaths',
            'pythonvideoannotator_module_distances',
            'pythonvideoannotator_module_eventsstats',
            'pythonvideoannotator_module_importexport',
            'pythonvideoannotator_module_motioncounter',
            'pythonvideoannotator_module_patheditor',
            'pythonvideoannotator_module_pathmap',
            'pythonvideoannotator_module_regionsfilter',
            'pythonvideoannotator_module_smoothpaths',
            'pythonvideoannotator_module_timeline',
            'pythonvideoannotator_module_tracking',
            'pythonvideoannotator_module_virtualobjectgenerator',
            ]
INCLUDES = []
EXCLUDES = ['PyQt4']

APP_VERSION = app_package.__version__

EXECUTABLE_NAME = "PythonVideoAnnotator-v{version}".format(version=APP_VERSION)

OPTIONS = {
	'argv_emulation': True,
	'compressed': False,
	'optimize': 0,
	'packages': PACKAGES,
	'includes': INCLUDES,
	'excludes': EXCLUDES,
	'iconfile': 'cf_icon_512x512.icns',
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
