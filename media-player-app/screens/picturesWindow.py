from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty

from kivymd.uix.hero import MDHeroFrom
from kivymd.uix.screen import MDScreen

import os

class HeroItem(MDHeroFrom):
    text = StringProperty()
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.tile.ids.image.ripple_duration_in_fast = 0.05

    def on_transform_in(self, instance_hero_widget, duration):
        Animation(
            radius=[0, 0, 0, 0],
            box_radius=[0, 0, 0, 0],
            duration=duration,
        ).start(instance_hero_widget)

    def on_transform_out(self, instance_hero_widget, duration):
        Animation(
            radius=[24, 24, 24, 24],
            box_radius=[0, 0, 24, 24],
            duration=duration,
        ).start(instance_hero_widget)


    def on_release(self):
        def switch_screen(*args):
            self.manager.current_heroes = [self.tag]
            self.manager.ids.hero_to.tag = self.tag
            self.manager.current = "screen B"

        Clock.schedule_once(switch_screen, 0.2)

class PicturesWindow(MDScreen):
    def my_widgets(self):
        img_dir = f"img/"
        img_list = []

        for filename in os.listdir(img_dir):
            f = os.path.join(img_dir, filename)
            if f.endswith('.jpg'):
                img_list.append(f)

    def on_start(self):
        for i in range(12):
            hero_item = HeroItem(
                text=f"Item {i + 1}", tag=f"Tag {i}", manager=self.root
            )
            if not i % 2:
                hero_item.md_bg_color = "lightgrey"
            self.wm.ids.WindowManager.screens[3].ids.playlists.add_widget(hero_item)
