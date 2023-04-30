import kivy
import os

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior


class HomeScreen(MDScreen):
    def my_widgets(self):
        img_dir = f"img/"
        img_list = []

        for filename in os.listdir(img_dir):
            f = os.path.join(img_dir, filename)
            if f.endswith('.jpg'):
                img_list.append(f)

        for img in img_list[:6]:
            self.wm.ids.WindowManager.screens[0].ids.fav_places.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="45dp",
                            width="50dp",
                            source=img,
                        ),
                        MDLabel(
                            text=img[4:-3],
                        ),
                        orientation="horizontal",
                    ),
                    size_hint=(.4, None),
                    height="45dp",
                    spacing="20dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )

        for img in img_list:
            self.wm.ids.WindowManager.screens[0].ids.recents_bar.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="150dp",
                            width="130dp",
                            source=img,
                        ),
                        MDLabel(
                            text=img[4:-3],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height="180dp",
                    width="130dp",
                    focus_behavior=True,
                    elevation=3,
                    )
            )

        for img in img_list[-4:]:
            self.wm.ids.WindowManager.screens[0].ids.playlists.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="150dp",
                            width="160dp",
                            source=img,
                        ),
                        MDLabel(
                            text=img[4:-3],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height="180dp",
                    width="160dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )

        for img in img_list[-6:]:
            self.wm.ids.WindowManager.screens[0].ids.plays.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            pos_hint={"center_X": .5},
                            height="40dp",
                            width="40dp",
                            radius="50dp",
                            source=img,
                        ),
                        MDLabel(
                            text=img[4:-3],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height="55dp",
                    width="60dp",
                )
            )

class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass