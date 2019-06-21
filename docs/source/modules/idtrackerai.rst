===========
Idtrackerai
===========

This plugin adds functionalities to correct the tracking and manipulate Idtrackerai projects.
You can visit the project @ `idtracker.ai <https://www.idtracker.ai/>`_

Correct the tracking
____________________

Select the Idtrackerai object in the project tree.

.. image:: /_static/modules/idtrackerai_1_select_obj.png

On the details section will see the options available to manipulate the tracking.

**Delete centroid** - This button is only available in a crossing where a single blob has multiple centroids associated to it. To delete the centroid you should select the centroid first, after the delete button will appear and you can select it for deletion.

**Add centroid** - This functionality is only available if the user selects a blob centroid. To add a new centroid to the selected blob, check the checkbox "Add centroid" and click on the video where you which to add the centroid.

**Interpolate trajectories** - You can interpolate trajectories for all the objects IDs or just for a single ID.
To do the interpolation just for a single ID you should select first in the video a centroid of that ID.


**Clear updates** - You can interpolate trajectories for all the objects IDs or just for a single ID.
To do the interpolation just for a single ID you should select first in the video a centroid of that ID.


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

