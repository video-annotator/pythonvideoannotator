#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# Module scipy.linalg on some other C/C++ extensions.
# The hidden import is necessary for PythonVideoAnnotator.
# Thanks to adammenges, see issue #1430.
hiddenimports = ['scipy.linalg.cython_blas','scipy.linalg.cython_lapack']