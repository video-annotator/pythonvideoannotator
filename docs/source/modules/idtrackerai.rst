===========
Idtrackerai
===========

This plugin adds functions to correct the tracking and manipulate Idtrackerai projects.
You can visit the project @ `idtracker.ai <https://www.idtracker.ai/>`_

Correct the tracking
____________________

Select the Idtrackerai object in the project tree.

.. image:: /_static/modules/idtrackerai_1_select_obj.png

On the details section will see the options available to manipulate the tracking.

**Interpolate trajectories** - You can interpolate trajectories for all the objects IDs or just for a single ID.
To interpolate the trajectory of a single ID you should select the Its centroid first.

**Clear updates** - You can interpolate trajectories of all the objects at the same time or just for a single ID.
To do the interpolation just for a single ID you should select its centroid first.

**Update a centroid ID** - Double click over a centroid and sets the new centroid ID in the window that will popup.

**Update a centroid position** - Select the centroid and drag it the the new position.

**Delete centroid** - The button is only available when you select a centroid from a single blob that has multiple centroids associated to it.

**Add centroid** - Adds a new centroid to the selected blob. The function is only available if the user selects a blob's centroid. To add a new centroid the user should first check the checkbox "Add centroid" and click in a position of the video.


Select a centroid
____________________

Click over a centroid of a blob.

.. image:: /_static/modules/idtrackerai_2_select_centroid.png

Keys events
____________

==========================================================================  =================================
EVENT                                                                       SHORT KEYS
==========================================================================  =================================
Go to the next crossing.                                                     Ctrl+M
Go to the previous crossing.                                                 Ctrl+N
==========================================================================  =================================

