@echo off
set WINPYDIR=C:\Users\swp\Python\WinPython-32bit-2.7.10.3-PythonVideoAnnotator\python-2.7.10
set WINPYVER=2.7.10.3
set HOME=%WINPYDIR%\..\settings
set WINPYARCH="WIN32"

set PATH=%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;

rem keep nbextensions in Winpython directory, rather then %APPDATA% default
set JUPYTER_DATA_DIR=%WINPYDIR%\..\settings

set BUILDSETTINGSDIR="%WORKSPACE%\build_settings\win"
set MAINSCRIPT="%WORKSPACE%\pythonvideoannotator\main.py"

echo %BUILDSETTINGSDIR%
echo %WORKSPACE%

pyinstaller --additional-hooks-dir %BUILDSETTINGSDIR%\hooks --name pythonVideoAnnotator --icon %BUILDSETTINGSDIR%\mouse.ico --onefile %MAINSCRIPT%