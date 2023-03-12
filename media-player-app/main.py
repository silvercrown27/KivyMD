from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.hero import MDHeroFrom

KV = '''
<HeroItem>
    size_hint_y: None
    height: "200dp"
    radius: 24

    MDSmartTile:
        id: tile
        radius: 24
        box_radius: 0, 0, 24, 24
        box_color: 0, 0, 0, .5
        source: "kivymd/images/logo/kivymd-icon-512.png"
        size_hint: None, None
        size: root.size
        mipmap: True
        on_release: root.on_release()

        MDLabel:
            text: root.tag
            bold: True
            font_style: "H6"
            opposite_colors: True


MDScreenManager:

    MDScreen:
        name: "screen A"

        ScrollView:

            MDGridLayout:
                id: box
                cols: 2
                spacing: "12dp"
                padding: "12dp"
                adaptive_height: True

    MDScreen:
        name: "screen B"
        heroes_to: [hero_to]

        MDHeroTo:
            id: hero_to
            size_hint: 1, None
            height: "220dp"
            pos_hint: {"top": 1}

        MDRaisedButton:
            text: "Move Hero To Screen A"
            pos_hint: {"center_x": .5}
            y: "36dp"
            on_release:
                root.current_heroes = [hero_to.tag]
                root.current = "screen A"
'''


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


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(12):
            hero_item = HeroItem(
                text=f"Item {i + 1}", tag=f"Tag {i}", manager=self.root
            )
            if not i % 2:
                hero_item.md_bg_color = "lightgrey"
            self.root.ids.box.add_widget(hero_item)


Test().run()