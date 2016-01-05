from pythonvideoannotator.modules.events_statistics.stats import Stats


class EventsStatistics(object):

    def __init__(self, title):
        super(EventsStatistics, self).__init__(title)

        self.mainmenu.append(
            {'Statistics': [
                {'Events stats': self.__open_events_statistics_window}
            ]
            }
        )

    def __open_events_statistics_window(self):
        win = Stats(self._time, parentWindow=self)
        win.show()
