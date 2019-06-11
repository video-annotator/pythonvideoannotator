from AnyQt.QtGui import QKeySequence
from pythonvideoannotator_models_gui.models.video.objects.object2d.datasets.path import Path

from .base_io import BaseIO
from confapp import conf

if conf.PYFORMS_MODE == 'GUI':
    from AnyQt import QtCore


class BaseKeysEvents(BaseIO):

    def __index__(self):
        super().__init__()

        self.player.on_key_release = self.__dummy_keys_release_evt

    def __dummy_keys_release_evt(self, event):
        pass

    def mark_point(self):
        selected = self.project.tree.selected_item

        if selected is not None and isinstance(selected.win, Path):
            path = selected.win

            if not path.mark_point_button.checked:
                path.mark_point_button.click()

    def keyReleaseEvent(self, event):

        event.ignore()

        modifier = event.modifiers()

        ######################################################################################
        #### TIMELINE SHORTCUTS ##############################################################
        ######################################################################################

        key = QKeySequence(event.modifiers() | event.key()).toString()

        print(key.encode("ascii", "ignore"))

        # Move the end of the selected event to the left.
        if key == conf.SHORT_KEYS['Move the end of the selected event to the left.']:
            self.timeline.move_selected_event_end_left()

        # Move the end of the selected event to the right.
        elif key == conf.SHORT_KEYS['Move the end of the selected event to the right.']:
            self.timeline.move_selected_event_end_right()

        # Move the begin of the selected event to the left.
        elif key == conf.SHORT_KEYS['Move the begin of the selected event to the left.']:
            self.timeline.move_selected_event_begin_left()

        # Move the begin of the selected event to the right.
        elif key == conf.SHORT_KEYS['Move the begin of the selected event to the right.']:
            self.timeline.move_selected_event_begin_right()

        # Move the selected event to the left.
        elif key == conf.SHORT_KEYS['Move the selected event to the left.']:
            self.timeline.move_selected_event_or_pointer_left()

        # Move the selected event to the right.
        elif key == conf.SHORT_KEYS['Move the selected event to the right.']:
            self.timeline.move_selected_event_or_pointer_right()

        # Move the selected event to the track above.
        elif key == conf.SHORT_KEYS['Move the selected event to the track above.']:
            self.timeline.move_selected_event_up()

        # Move the selected event to the track bellow.
        elif key == conf.SHORT_KEYS['Move the selected event to the track bellow.']:
            self.timeline.move_selected_event_down()

        # Delete the selected event.
        elif key == conf.SHORT_KEYS['Delete the selected event.']:
            self.timeline.remove_selected_event()

        # Open or close a new event.
        elif key == conf.SHORT_KEYS['Open or close a new event.']:
            self.timeline.open_and_close_event()

        # Lock or unlock the selected event.
        elif key == conf.SHORT_KEYS['Lock or unlock the selected event.']:
            self.timeline.toggle_selected_event_lock()

        # Select the first event.
        elif key == conf.SHORT_KEYS['Select the first event.']:
            self.timeline.select_last_event()

        # Select the last event.
        elif key == conf.SHORT_KEYS['Select the last event.']:
            self.timeline.select_first_event()

        # Select the next event.
        elif key == conf.SHORT_KEYS['Select the next event.']:
            self.timeline.select_next_event()

        # Select the previous event.
        elif key == conf.SHORT_KEYS['Select the previous event.']:
            self.timeline.select_previous_event()

        ######################################################################################
        #### SPECIFIC SHORTCUTS###############################################################
        ######################################################################################

        # Go to the next event and then click the mark the point button.
        elif key == conf.SHORT_KEYS['Go to the next event and then click the mark the point button.']:
            if self.timeline.timeline_widget.selected is not None and \
                    self.timeline.timeline_widget.selected != self.timeline.timeline_widget.pointer:
                self.move_to_next_event()
                self.mark_point()

        # Select the path of the next object and click the mark the point button.
        elif key == conf.SHORT_KEYS['Select the path of the next object and click the mark the point button.']:
            self.select_next_path()
            self.mark_point()

        # "Click" the Mark Point button in the current Path.
        elif key == conf.SHORT_KEYS['"Click" the Mark Point button in the current Path.']:
            self.mark_point()

        ######################################################################################
        #### PLAYER SHORTCUTS ################################################################
        ######################################################################################

        # Play or pause the video.
        elif key == conf.SHORT_KEYS['Play or pause the video.']:
            self.player.toggle_playing()

        # Jumps 1 frame backwards.
        elif key == conf.SHORT_KEYS['Jumps 1 frame backward.']:
            self.player.back_one_frame()

        # Jumps 1 frame forward.
        elif key == conf.SHORT_KEYS['Jumps 1 frame forward.']:
            self.player.forward_one_frame()

        # Jumps 20 seconds backward.
        elif key == conf.SHORT_KEYS['Jumps 20 seconds backward.']:
            self.player.jump_backward()

        # Jumps 20 seconds forward.
        elif key == conf.SHORT_KEYS['Jumps 20 seconds forward.']:
            self.player.jump_forward()

        # Set player speed to 1x.
        elif key == conf.SHORT_KEYS['Set player speed to 1x.']:
            self.player.set_speed_1x()

        # Set player speed to 2x
        elif key == conf.SHORT_KEYS['Set player speed to 2x.']:
            self.player.set_speed_2x()

        # Set player speed to 3x
        elif key == conf.SHORT_KEYS['Set player speed to 3x.']:
            self.player.set_speed_3x()

        # Set player speed to 4x
        elif key == conf.SHORT_KEYS['Set player speed to 4x.']:
            self.player.set_speed_4x()

        # Set player speed to 5x
        elif key == conf.SHORT_KEYS['Set player speed to 5x.']:
            self.player.set_speed_5x()

        # Set player speed to 6x
        elif key == conf.SHORT_KEYS['Set player speed to 6x.']:
            self.player.set_speed_6x()

        # Set player speed to 7x
        elif key == conf.SHORT_KEYS['Set player speed to 7x.']:
            self.player.set_speed_7x()

        # Set player speed to 8x
        elif key == conf.SHORT_KEYS['Set player speed to 8x.']:
            self.player.set_speed_8x()

        # Set player speed to 9x
        elif key == conf.SHORT_KEYS['Set player speed to 9x.']:
            self.player.set_speed_9x()
