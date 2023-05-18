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
        def add_widget(filepath, media, curr_iter):
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
                    on_press=lambda btn, media_dirs=media, curr_iter=curr_iter: app.play_audio(media_dirs, curr_iter)
                )
            )

        media = [d[1] for i in media_extensions for d in search(i, folder_id)]
        for i, filepath in enumerate(media[:-1]):
            Clock.schedule_once(lambda dt, filepath=filepath, curr_iter=i: add_widget(filepath, media, curr_iter),
                                i * 0.03)
