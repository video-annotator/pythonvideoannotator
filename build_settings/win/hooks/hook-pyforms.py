from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ["pyforms.Controls"]

datas = collect_data_files('pyforms')
