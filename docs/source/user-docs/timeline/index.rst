|

Timeline
===============

|

.. image:: /_static/user-docs/timeline/timeline.png
	:align: center

|
|


The timeline events
__________________________________________

|

- Create a new event:
	- double-click on the track an time it wish to add a new event.
- Edit the event label:
	- double-click over the event.
- Resize the event:
	- drag the left and right side of the box until you reach the desired size.
- Change the event color:
	- right click over the event and choose the option "pick a color".
- Lock the edition of an event:
	- right click over the event and choose the option "lock".
- Remove an event:
	- right click over the event and choose the option "remove".
|

Edit the properties of a track
__________________________________________

|
| With the mouse over a track, click on the right button of mouse and choose the option "Track properties". A new window will appear.
| On this window you can set the label of the track and the color which that the new events will have.

.. image:: /_static/user-docs/timeline/track-properties.png

|

Show a dataset property on the timeline
__________________________________________

|
| On the project tree select the dataset property, press the right button of the mouse and select the option "View on the timeline". The graph of property will be then shown on the timeline.

.. image:: /_static/user-docs/timeline/send-2-timeline.png

|


Import & export events
__________________________________________

|

Use the buttons on the bottom right side to export events to a csv file or import graphs, events or bonsai events files.

|

Edit the graphs properties
__________________________________________

|
| Press the right mouse button and select the "Graphs" option to access the graphs properties window.
| On these window it is possible to edit the graphs names and their display.
| Also you can use this window to visualize the value of a graph in a certain time point. Just select the graph, mouse over it and you will see the values of the graph displayed on the window.
|

.. image:: /_static/user-docs/timeline/graphs-properties.png

|

Convert graphs to events
__________________________________________

|
| Press the right mouse button and select option "Convert graphs to events".
| A new window will be shown. On the left-side list, double click on the graph you would like to use for the equation, and write the rest of it.
| Use the fields **Event name** to define the name of the new events, use the **row number** field to define the row where the events should be created, and the **Minimum number of frames** to define the necessary number of consecutive frames where the equation is verified to be create the events.
|
Equation example:

.. code-block:: python

	[Deeplearning result]>0.5 and [value(6)]<10
|

.. note:: Use spaces only on between logic operators: **and** or **or**.

|

.. image:: /_static/user-docs/timeline/convert-graphs-2-events.png

|

.. image:: /_static/user-docs/timeline/convert-graphs-2-events-window.png