# class BaseModule([BaseWidget](http://pyforms.readthedocs.io/en/v1.0.beta/api-documentation/basewidget/))

Implements the main interface.

### \_\_init\_\_()


## **Variables**
***************************

### self._player

Player control

### self._time

Timeline Control

### self._dock

Dock window that contains the timeline control.


## **Properties**
***************************

### timeline

Returns the timeline control.

### player

Returns the player control.
	
### video

Returns a cv2.VideoCapture object of the video active in the player, and also sets the cv2.VideoCapture or video path in the player.

### project

Return the active project.

## **Functions**
***************************

### init_form()

Calls [BaseWidget](http://pyforms.readthedocs.io/en/v1.0.beta/api-documentation/basewidget/) super.
Opens a default Project, or Graph (check Settings section).

### load_project(project_path=None)

Loads a project from a directory.
If the project_path parameter is **None** it will open a dialog for the user to choose a directory.

### save_project(project_path=None)

Save the project to a directory.
If the project_path parameter is **None** it will open a dialog for the user to choose a directory.

## **Events**
***************************

### added_video_event(video)

Function called when a new video is added to the project.
This functions is used to update the interface.

### removed_video_event(video)

Function called when a new video is removed from the project.
This functions is used to update the interface.

### added_object_event(obj)

Function called when a new object is added to a video.
This functions is used to update the interface.

### removed_object_event(obj)

Function called when a new video is removed from a video.
This functions is used to update the interface.

### added_dataset_event(dataset)

Function called when a new video is added to an object.
This functions is used to update the interface.

### removed_dataset_event(dataset)

Function called when a new video is removed from an object.
This functions is used to update the interface.

### on_player_click_event(event, x, y)

Function called whenever the mouse press click in the player image.

### process_frame_event(frame)

Function called before a frame is rendered into the player.
Should return the frame to render or a list of frames.

### \_\_open_project_event()

Function called by the main menu option, "Open project".

### \_\_save_project_event()

Function called by the main menu option, "Save project".

### \_\_save_project_as_event()

Function called by the main menu option, "Open project as".
	
### \_\_timeline_key_release_event(event)

Function called when a key is pressed in the timeline control.

