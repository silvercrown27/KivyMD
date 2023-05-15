import os
import threading

from kivy.app import App
from kivy.clock import Clock

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget

from .tools import search

folder_id = '172'
media_extensions = ('.mp3', '.wav', '.ogg')


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MusicWindow(MDScreen):
    def on_enter(self):
        # start a new thread to scan for media files
        threading.Thread(target=self.scan_media_files, args=(App.get_running_app(),)).start()

    def on_leave(self, *args):
        self.ids.tracks.clear_widgets()

    def scan_media_files(self, app):
        def add_widget(filepath, next_track):
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
                    on_release=lambda btn, filepath=filepath: app.play_audio(filepath, next_track)
                )
            )

        media = [d for i in media_extensions for d in search(i, folder_id)]
        for i, filepath in enumerate(media[:-1]):
            next_track = media[i+1][1]
            Clock.schedule_once(lambda dt, filepath=filepath[1], next_track=next_track: add_widget(filepath, next_track), i * 0.05)
        # add the last track without a next track
        Clock.schedule_once(lambda dt, filepath=media[-1][1]: add_widget(filepath, None), (len(media)-1) * 0.05)