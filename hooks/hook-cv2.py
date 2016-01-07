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
    library = ctypes.util.find_library('opencv_ffmpeg310')
    # :todo: Should be issue a warning-message, if the libary is not
    # found?
    if library:
        datas = [(library, '')]
