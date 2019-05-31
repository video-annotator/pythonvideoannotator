# !/usr/bin/python2
# -*- coding: utf-8 -*-

import logging, traceback, pythonvideoannotator, sys, platform

from confapp import conf
from urllib.parse import urlencode
from uuid import getnode as get_mac
from AnyQt.QtWidgets import QMessageBox
from urllib.request import Request, urlopen
from AnyQt.QtWidgets import QApplication

try:
	import pyforms
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

try:
	from confapp import conf
except ImportError as err:
	logging.getLogger().critical(str(err), exc_info=True)
	exit("Could not load pyforms! Is it installed?")

from pythonvideoannotator.base_module import BaseModule

logging.getLogger('PyQt5').setLevel(logging.INFO)

print()
print('**************************************')
print()

VideoAnnotator = type(
	'VideoAnnotator',
	tuple(conf.VIDEOANNOTATOR_MODULES.find_class('module.Module') + [BaseModule]),
	{}
)


def start(parent_win=None):

	try:
		res = pyforms.start_app(
			VideoAnnotator,
			geometry=conf.MAIN_WINDOW_GEOMETRY,
			parent_win=parent_win
		)
		return res

	except Exception as e:
		report = traceback.format_exc()

		app = QApplication(sys.argv)
		m = QMessageBox(
			QMessageBox.Question,
			"Send report",
			"<h2>Would you like to send us a report of the bug?</h2>"
			"This will help us improving the software."
			"<p>{bug}</p>".format( bug=str(e) ),
			QMessageBox.Yes | QMessageBox.No
		)
		reply = m.exec_()

		if reply==QMessageBox.Yes:
			try:
				app_id = conf.USERSTATS_APP_ID
				reg_id = get_mac()
				os_name = platform.platform()
				version = pythonvideoannotator.__version__

				data = {'app-id': app_id, 'reg-id': reg_id, 'os-name' : os_name, 'version': version, 'report': report}
				url = "{}/register-bug".format(conf.USERSTATS_URL)
				request = Request(url, urlencode(data).encode())
				urlopen(request).read().decode()
			except Exception as ex:
				print("Could not register new access", ex )

		exit()
		app.exec_()


if __name__ == '__main__': start()
