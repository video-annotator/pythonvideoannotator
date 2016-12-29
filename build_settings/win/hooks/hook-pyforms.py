from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ["pyforms.Controls", "pyforms.gui.settings", "pyforms.settings"]

datas = collect_data_files('pyforms')
