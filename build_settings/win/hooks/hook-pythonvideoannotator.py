# pyforms import app settings.py dinamically so we need to inform pyinstaller

hiddenimports = ['pythonvideoannotator.settings']

datas = [ ('pythonvideoannotator\\resources', 'pythonvideoannotator\\resources'),]