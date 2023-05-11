import os
import threading

from kivy.app import App
from kivy.clock import Clock

from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
class MusicWindow(MDScreen):
    def on_enter(self):
        # start a new thread to scan for media files
        threading.Thread(target=self.scan_media_files, args=(App.get_running_app(),)).start()

    def scan_media_files(self, app):
        # scan for media files
        media_extensions = ('.mp3', '.wav', '.ogg')  # add other extensions if needed
        media_files = []

        # traverse directory tree and find all media files
        for dirpath, dirnames, filenames in os.walk('C:/Users/USER/Documents/GitHub/') or os.walk('/'):
            for filename in filenames:
                if filename.endswith(media_extensions):
                    media_files.append(os.path.join(dirpath, filename))

        # add each media file as a widget to the tracks list (on the UI thread)
        def add_widget(filepath):
            filename = os.path.basename(filepath)
            self.ids.tracks.add_widget(
                TwoLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="music-note-quarter",
                    ),
                    IconRightWidget(
                        icon="dots-vertical",
                    ),
                    text=filename,
                    on_release=lambda btn, filepath=filepath: app.play_audio(filepath)
                )
            )
        Clock.schedule_once(lambda dt: [add_widget(filepath) for filepath in media_files])
