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
+ collect_submodules('pythonvideoannotator_module_patheditor') \
+ collect_submodules('pythonvideoannotator_module_backgroundfinder') \
+ collect_submodules('pythonvideoannotator_module_virtualobjectgenerator') \
+ collect_submodules('pythonvideoannotator_module_smoothpaths') \
+ collect_submodules('pythonvideoannotator_module_createpaths') \
+ collect_submodules('pythonvideoannotator_module_motioncounter') \
+ collect_submodules('pythonvideoannotator_module_distances') \
+ collect_submodules('pythonvideoannotator_module_pathmap') \
+ collect_submodules('pythonvideoannotator_module_importexport') \
+ collect_submodules('mcvapi') \
+ collect_submodules('mcvgui') \
+ collect_submodules('geometry_designer') \


datas = [ ('pythonvideoannotator\\resources', 'pythonvideoannotator\\resources'),]