@echo off
SETLOCAL enableextensions enabledelayedexpansion

:: 1
:: WINPYTHON SETTINGS

set "WINPYDIR=C:\WinPython\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64"
set "WINPYVER=3.5.3.0Qt5"
set "HOME=%WINPYDIR%\..\settings"
set "WINPYARCH=WIN-AMD64"

:: SET PATH FOR PYTHON
SET "PYTHON_PATH=%WINPYDIR%\Lib\site-packages\PyQt5;%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;"

:: SAVE CURRENT PATH AND OVERRIDE FOR PYTHON
SET "ORIGINAL_PATH=%PATH%"
SET "PATH=%PYTHON_PATH%"

ECHO Python path activated

:: keep nbextensions in Winpython directory, rather then %APPDATA% default
SET "JUPYTER_DATA_DIR=%HOME%"

:: force default pyqt5 kit
SET "QT_API=pyqt5"

:: http://stackoverflow.com/questions/38674400/missing-dll-files-when-using-pyinstaller
SET "QT5_DLL_PATH=C:\WinPython\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\Lib\site-packages\PyQt5\Qt\bin"

:: 2
:: PYINSTALLER SETTINGS

echo "PYTHON VERSION:"
python --version

set "PROJECTNAME=pythonVideoAnnotator"
set "BUILDSETTINGSDIR=%WORKSPACE%\build_settings\win"
set "MAINSCRIPT=%WORKSPACE%\pythonvideoannotator\__main__.py"
set "BUILDOUTDIR=%WORKSPACE%\build"
set "DISTOUTDIR=%WORKSPACE%\dist"
set "ICONNAME=cf_icon_128x128.ico"


python setup.py --version > software_version.txt
"C:\Program Files\Git\bin\git.exe" rev-list  --all --count > git_version.txt
SET /p DEV_VERSION= < software_version.txt
SET /p GIT_VERSION= < git_version.txt
SET DEV_VERSION=%DEV_VERSION%_git%GIT_VERSION%_build%BUILD_NUMBER%
DEL software_version.txt
DEL git_version.txt

ECHO Removing old build dir...
@RD /S /Q %BUILDOUTDIR%

ECHO Removing old dist dir...
@RD /S /Q %DISTOUTDIR%

:: install pip dependencies

IF "%BUILD_DEPENDENCIES%"=="true" (

   ECHO Installing dependencies with pip...

   pip install pyserial --upgrade
   pip install Send2Trash --upgrade

   pip install https://github.com/UmSenhorQualquer/pysettings/archive/"%PYSETTINGS_GIT_BRANCH%".zip --upgrade
   pip install https://github.com/UmSenhorQualquer/pyforms/archive/"%PYFORMS_GIT_BRANCH%".zip --upgrade

   pip install https://bitbucket.org/fchampalimaud/logging-bootstrap/get/"%LOGGING_BOOTSTRAP_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybranch/get/"%PYBRANCH_GIT_BRANCH%".zip --upgrade

   pip install https://bitbucket.org/fchampalimaud/pybpod-api/get/"%PYBPODAPI_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/get/"%PYBPODGUIPLUGIN_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-timeline/get/"%PYBPODGUIPLUGIN_TIMELINE_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/session-log-plugin/get/"%SESSIONLOGPLUGIN_GIT_BRANCH%".zip --upgrade
)

:: python setup.py sdist

:: RUN PYINSTALLER

ECHO Running pyinstaller now...

IF /I "%GIT_BRANCH%" EQU "master" (
   set "DISTJOBDIR=%PROJECTNAME%_v%DEV_VERSION%"
   pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "!DISTJOBDIR!" --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --onedir  --noconsole --paths "%QT5_DLL_PATH%" "%MAINSCRIPT%"
) ELSE (
   set "DISTJOBDIR=%PROJECTNAME%_v%DEV_VERSION%.DEV"
   pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "!DISTJOBDIR!" --exclude-module IPython --exclude-module sqlalchemy --exclude-module PIL --exclude-module matplotlib.backends --exclude-module matplotlib --exclude-module requests --exclude-module xml.dom.domreg --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --debug --onedir --paths "%QT5_DLL_PATH%" "%MAINSCRIPT%"
)

:: SAVE VARS ON FILE

echo DEV_VERSION=%DEV_VERSION% > env.propsfile
echo GIT_VERSION=%GIT_VERSION%  >> env.propsfile
echo DISTOUTDIR=%DISTOUTDIR:\=\\%  >> env.propsfile
echo PROJECTNAME=%PROJECTNAME% >> env.propsfile
echo DISTJOBDIR=!DISTJOBDIR! >> env.propsfile

SET "PATH=%ORIGINAL_PATH%"
ECHO System path activated

ECHO Copying user settings
xcopy /Y "%WORKSPACE%\build_settings\win\bpod\pyforms_generic_editor_user_settings.py"  "%WORKSPACE%\dist\%DISTJOBDIR%"

:: echo "Running pyinstaller --additional-hooks-dir %BUILDSETTINGSDIR%\hooks --name %PROJECTNAME% --icon %BUILDSETTINGSDIR%\%ICONNAME% --onefile %MAINSCRIPT%"
IF %COMPILE_2_FOLDER% EQU true (
	echo pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "%PROJECTNAME%_v%DEV_VERSION%_DEV" --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --onedir --debug "%MAINSCRIPT%"
	pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "%PROJECTNAME%_v%DEV_VERSION%_DEV" --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --onedir --debug "%MAINSCRIPT%"
	IF %SOURCEFORGE_UPLOAD% EQU true (
		echo cd "%WORKSPACE%\dist\" & python c:\Users\swp\Python\zip.py "%PROJECTNAME%_v%DEV_VERSION%_DEV" "%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%_DEV.zip"
		cd "%WORKSPACE%\dist\" & python c:\Users\swp\Python\zip.py "%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%_DEV" "%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%_DEV.zip"
		echo "Uploading to SourceForge..."
		echo c:\curl\curl.exe --progress-bar --netrc-file c:\curl_auth\bitbucket_auth.txt -X POST https://api.bitbucket.org/2.0/repositories/fchampalimaud/pythonvideoannotator/downloads -F files=@"%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%_DEV.zip"
		c:\curl\curl.exe --progress-bar --netrc-file c:\curl_auth\bitbucket_auth.txt -X POST https://api.bitbucket.org/2.0/repositories/fchampalimaud/pythonvideoannotator/downloads -F files=@"%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%_DEV.zip" > curl_output.log
	) ELSE (
		echo "Skipping upload to SourceForge"
	)
) ELSE (
	echo pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "%PROJECTNAME%_v%DEV_VERSION%_DEV" --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --debug --onefile "%MAINSCRIPT%"
	pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "%PROJECTNAME%_v%DEV_VERSION%_DEV" --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --debug --onefile "%MAINSCRIPT%"
	IF %SOURCEFORGE_UPLOAD% EQU true (
		echo "Uploading to SourceForge..."
		echo c:\curl\curl.exe --progress-bar --netrc-file c:\curl_auth\bitbucket_auth.txt -X POST https://api.bitbucket.org/2.0/repositories/fchampalimaud/pythonvideoannotator/downloads -F files=@"%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%.exe"
		c:\curl\curl.exe --progress-bar --netrc-file c:\curl_auth\bitbucket_auth.txt -X POST https://api.bitbucket.org/2.0/repositories/fchampalimaud/pythonvideoannotator/downloads -F files=@"%WORKSPACE%\dist\%PROJECTNAME%_v%DEV_VERSION%.exe" > curl_output.log
	) ELSE (
		echo "Skipping upload to SourceForge"
	)
)