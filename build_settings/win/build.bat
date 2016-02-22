set WINPYDIR=C:\Users\swp\Python\WinPython-32bit-2.7.10\python-2.7.10
set WINPYVER=2.7.10
set HOME=%WINPYDIR%\..\settings
set WINPYARCH="WIN32"

set PATH=%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;

rem keep nbextensions in Winpython directory, rather then %APPDATA% default
set JUPYTER_DATA_DIR=%WINPYDIR%\..\settings

set PROJECTNAME="pythonVideoAnnotator"
set BUILDSETTINGSDIR="%WORKSPACE%\build_settings\win"
set MAINSCRIPT="%WORKSPACE%\pythonvideoannotator\__main__.py"
set BUILDOUTDIR="%WORKSPACE%\build"
set DISTOUTDIR="%WORKSPACE%\dist"

echo %PROJECTNAME%
echo %BUILDSETTINGSDIR%
echo %WORKSPACE%
echo %MAINSCRIPT%
echo %BUILDOUTDIR%
echo %DISTOUTDIR%

@RD /S /Q %BUILDOUTDIR%
@RD /S /Q %DISTOUTDIR%

python setup.py sdist

pyinstaller --additional-hooks-dir %BUILDSETTINGSDIR%\hooks --name %PROJECTNAME% --icon %BUILDSETTINGSDIR%\mouse.ico %MAINSCRIPT%