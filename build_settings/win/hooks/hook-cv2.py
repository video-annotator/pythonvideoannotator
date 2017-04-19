#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


hiddenimports = ['numpy'] 

"""
OpenCV requires opencv_ffmpeg310.dll which isn't found by PyInstaller.
"""


import ctypes.util
from PyInstaller.compat import is_win


# opencv_ffmpeg310.dll is available only for Windows.
if is_win:
	libraries = []
	library = ctypes.util.find_library('opencv_ffmpeg320_64')
	if library: libraries.append( (library, '') )
	library = ctypes.util.find_library('opencv_ffmpeg320')
	if library: libraries.append( (library, '') )
	library = ctypes.util.find_library('opencv_ffmpeg320_32')
	if library: libraries.append( (library, '') )
	
	datas = libraries