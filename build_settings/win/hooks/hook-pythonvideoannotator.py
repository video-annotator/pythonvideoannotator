# pyforms import app settings.py dinamically so we need to inform pyinstaller

hiddenimports = [
	'pythonvideoannotator.settings',
	'pythonvideoannotator_module_contoursimages',	
	'pythonvideoannotator_module_contoursimages.settings',
	'pythonvideoannotator_module_tracking',
	'pythonvideoannotator_module_tracking.settings',
	'pythonvideoannotator_module_timeline',
	'pythonvideoannotator_module_timeline.settings',
	'pythonvideoannotator_module_patheditor',
	'pythonvideoannotator_module_patheditor.settings',
]

datas = [ ('pythonvideoannotator\\resources', 'pythonvideoannotator\\resources'),]