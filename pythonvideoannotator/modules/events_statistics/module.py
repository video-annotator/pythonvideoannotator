from pythonvideoannotator.modules.events_statistics.stats import Stats


class Module(object):

    def __init__(self):
        super(Module, self).__init__()

        self.mainmenu.append(
            {'Statistics': [
                {'Events stats': self.__open_events_statistics_window}
            ]
            }
        )

    def __open_events_statistics_window(self): Stats(self._time, parentWindow=self).show()
