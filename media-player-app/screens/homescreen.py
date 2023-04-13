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
                            text=img,
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
            self.wm.ids.WindowManager.screens[0].ids.playlists.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="150dp",
                            width="130dp",
                            source=img,
                        ),
                        MDLabel(
                            text=img,
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
            for img in img_list[:6]:
                self.wm.ids.WindowManager.screens[0].ids.playlists.add_widget(
                    MDCard(
                        MDBoxLayout(
                            FitImage(
                                size_hint=(None, None),
                                height="150dp",
                                width="130dp",
                                source=img,
                            ),
                            MDLabel(
                                text=img,
                            ),
                            orientation="horizontal"
                        ),
                        size_hint=(None, None),
                        height="50dp",
                        width="100dp",
                        focus_behavior=True,
                        elevation=3,
                    )
                )


class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass
