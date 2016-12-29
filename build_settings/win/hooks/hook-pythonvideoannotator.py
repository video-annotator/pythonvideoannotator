from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# pyforms import app settings.py dinamically so we need to inform pyinstaller

hiddenimports = [
	'pythonvideoannotator.settings',
	'pythonvideoannotator_models_gui.settings',
	'pythonvideoannotator.resources',
] \
+ collect_submodules('pythonvideoannotator_module_contoursimages') \
+ collect_submodules('pythonvideoannotator_module_tracking') \
+ collect_submodules('pythonvideoannotator_module_timeline') \
+ collect_submodules('pythonvideoannotator_module_patheditor')

datas = [ ('pythonvideoannotator\\resources', 'pythonvideoannotator\\resources'),]