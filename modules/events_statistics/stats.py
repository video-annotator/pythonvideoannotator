from __init__ import *
import numpy as np, csv, os
from PyQt4 import QtCore, QtGui

class Stats(BaseWidget):
    
    def __init__(self, parent=None, parentWindow=None):
        BaseWidget.__init__(self,'Events stats', parentWindow=parentWindow)
        self._parent = parent

        self._bounds          = ControlBoundingSlider('Frames range', 1, 100, horizontal=True) 
        self._nframes         = ControlNumber('Merge in a group of', 1)
        self._analyseButton   = ControlButton('Calculate graphs')
        self._events          = ControlCheckBoxList()
        self._graph           = ControlVisVis('Graph')
        self._showTotalCounts = ControlCheckBox('Show total events counting')
        self._showEvtsCounts  = ControlCheckBox('Show events counting', True)
        self._progress        = ControlProgress()
        self._exportDurations = ControlButton('Export durations')

        self._formset = [
            (' ','_showEvtsCounts','|','_showTotalCounts','|','_nframes','_analyseButton','_exportDurations'),
            '_bounds', 
            {   'a:Graph':['_graph'],
                'c:Events selection':['_events']   }, 
            '_progress'
        ]

        self._analyseButton.value = self.__generate_graph
        self._exportDurations.value = self.__export_durations
        self._progress.hide()

        self.__load_events()

    
        
    def __load_events(self):
        """
        This function load the events present in the main window
        """
        self._events_list = []

        event_types = []
        start       = None 
        end         = None
        for track in self._parent.tracks:
            for delta in track.periods:
                if delta.title not in event_types:
                    self._events += (delta.title, True)
                    event_types.append(delta.title)
                
                if start==None or start>delta._begin:   start = delta._begin
                if end==None or end<delta._end:         end = delta._end

                self._events_list.append( (delta._begin,delta._end, delta.title) )

        if len(self._events_list)==0: return

        self._events_list = sorted(self._events_list, key=lambda x: (x[1], x[0]) )

        #Set the bounding bar for the frames selection
        self._bounds.min = start-10
        self._bounds.max = end+10
        self._bounds.value = (start, end)
        self._nframes.min = 1
        self._nframes.max = end

        
        self.__generate_graph()


    def __do_the_calculations(self):
        self._values2display = []
        self._legends        = []
        self._duration       = {}

        events_to_include = self._events.value

        #If no events are selected, clean the graph and exit the function 
        if  len(events_to_include)==0 or \
            (not self._showTotalCounts.value and not self._showEvtsCounts.value): 
            return

        self._progress.min = 0
        self._progress.max = self._bounds.value[1]
        self._progress.value = 0
        self._progress.show()
        

        framesBin       = self._nframes.value
        totalFrames     = int(self._bounds.value[1]+1)
        #Stores the counting related to a all the events
        totalcounts     = np.array([0 for x in range( totalFrames )]) 
        #Stores the counting related each event
        counts          = {} 
        

        for label in events_to_include: 
            counts[label]   = np.array([0 for x in range( totalFrames )])
            self._duration[label] = np.array([0 for x in range( totalFrames )])

        
        for i in range(0,totalFrames):
            #events_counted - this variable is used to 
            #avoid repeating the same event in the current BIN counting
            if (i % framesBin)==0: events_counted = []

            self._progress.value = i

            for j, (start, end, event) in enumerate(self._events_list):
                if start<=i and end>=i and \
                    (event in events_to_include) and \
                    (j not in events_counted):  #Do not count again a event that was already counted for this BIN

                    lowerBound = i - (i % framesBin)
                    upperBound = lowerBound + framesBin
                    totalcounts[lowerBound:upperBound] += 1
                    counts[event][lowerBound:upperBound] += 1
                    
                    events_counted.append(j)

                if start<=i and end>=i and (event in events_to_include):
                    self._duration[event][i] += 1

    
        
        
        if self._showTotalCounts.value:
            self._values2display.append(totalcounts)
            self._legends.append('All selected events')

        if self._showEvtsCounts.value:
            for label, values in counts.items():
                self._legends.append(label)
                self._values2display.append(values)

        self._progress.hide()


    def __export_durations(self):
        directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select directory to save the data"))
        if directory!='':
            self.__do_the_calculations()

            events_to_include = self._events.value

            self._progress.min = 0
            self._progress.max = self._bounds.value[1]*len(events_to_include)
            self._progress.value = 0
            self._progress.show()

            framesBin       = self._nframes.value
            totalFrames     = int(self._bounds.value[1]+1)
            


            for j, label in enumerate(events_to_include):
                with open(os.path.join(directory, '{0}.csv'.format(label)), 'wb') as csvfile:

                    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(['Event', 'start', 'end', 'duration in frames'])
                    for i in range(0,totalFrames, framesBin):
                        count = sum(self._duration[label][i:i+framesBin])
                        if count>0: spamwriter.writerow([label, i, i+framesBin, count])
                        self._progress.value = i+self._bounds.value[1]*j





    def __generate_graph(self):
        self.__do_the_calculations()

        self._graph.value   = self._values2display
        self._graph.legends = self._legends
        
        
if __name__ == "__main__":  pyforms.startApp(Stats)
