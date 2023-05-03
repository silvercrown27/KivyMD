import os

from kivymd.toast import toast
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MusicWindow(MDScreen):
    def my_widgets(self):
        # scan for media files when the user enters the screen
        media_extensions = ('.mp3', '.wav', '.ogg')  # add other extensions if needed
        media_files = []

        # traverse directory tree and find all media files
        for dirpath, dirnames, filenames in os.walk('C:/Users/USER/Documents/GitHub/') or os.walk('/'):
            for filename in filenames:
                if filename.endswith(media_extensions):
                    media_files.append(os.path.join(dirpath, filename))

        # add each media file as a widget to the tracks list
        for filepath in media_files:
            filename = os.path.basename(filepath)
            self.wm.ids.WindowManager.screens[1].ids.tracks.add_widget(
                TwoLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="music-note-quarter",
                    ),
                    IconRightWidget(
                        icon="dots-vertical",
                    ),
                    text=filename,
                    on_release=lambda filepath=filepath: self.play_audio(filepath),
                )
            )
