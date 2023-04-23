import os

from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MusicWindow(MDScreen):
    def my_widgets(self):
        media_dir = f"C://Users/USER/Documents/GitHub/media/"
        mymedia = []

        for filename in os.listdir(media_dir):
            f = filename
            if f.endswith('.mp3'):
                mymedia.append(f)

        for m in mymedia:
            self.wm.ids.WindowManager.screens[1].ids.tracks.add_widget(
                TwoLineAvatarIconListItem(
                    IconLeftWidget(
                        icon="music-note-quarter",
                    ),
                    IconRightWidget(
                        icon="dots-vertical",
                    ),
                    text=m,
                    on_release=self.play_audio(media_dir, m),
                )
            )
