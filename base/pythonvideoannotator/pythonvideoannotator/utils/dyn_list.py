

class DynList(object):

	def __init__(self, lenfunc, getfunc):
		self._lenfunc = lenfunc
		self._getfunc = getfunc

	def __len__(self): return self._lenfunc

	def __getitem__(self, index): 
		return self._getfunc(index)

