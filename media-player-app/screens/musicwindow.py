import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.uix.imagelist.imagelist import MDSmartTile


class MusicWindow(Screen):
    text = StringProperty()

