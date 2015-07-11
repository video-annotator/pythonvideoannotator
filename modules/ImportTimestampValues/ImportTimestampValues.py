import csv
		
class ImportTimestampValues(object):

	def __init__(self, title):
		"""
		This implements the Path edition functionality
		"""
		super(ImportTimestampValues,self).__init__(title)
		
	def initForm(self):
		#Add the options to the player popup menu

		self.mainmenu.append(
				{ 'Import data': [
						{'Import timestamp data': self.__open_timestamp_data},
					]
				}
			)

		super(ImportTimestampValues,self).initForm()


	def __open_timestamp_data(self):
		filename = str(QtGui.QFileDialog.getOpenFileName(None, 'Choose a file', '.'))
		if filename!='':
			with open(filename, 'rb') as csvfile:
				spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				for spamreader in spamreader[:30]:
					print spamreader

