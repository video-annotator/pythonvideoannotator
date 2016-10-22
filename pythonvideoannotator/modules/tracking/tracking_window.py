from pyforms import BaseWidget

from pyforms.Controls import ControlText
from pyforms.Controls import ControlList
from pyforms.Controls import ControlCombo
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCheckBox


class TrackingWindow(BaseWidget):

	def __init__(self):
		super(TrackingWindow, self).__init__('Tracking')

		self._start = ControlText('Start on frame')
		self._end 	= ControlText('End on frame')

		self._avail_objs = ControlCombo('Objects')
		self._sel_objs 	 = ControlList('Track the objects')
		self._add_obj 	 = ControlButton('Add object')

		self._formset = [
			('_start', '_end'),
			('_avail_objs', '_add_obj'),
			'_sel_objs',
			('_use_bgsubract', '_use_adapt_thresh', '_use_colors_thresh', '_use_formula')
		]

		self._use_bgsubract 	= ControlCheckBox('Use background subtraction')
		self._use_adapt_thresh 	= ControlCheckBox('Use adaptative threshold')
		self._use_colors_thresh = ControlCheckBox('Use colors threshold')
		self._use_formula 		= ControlCheckBox('Use formula')