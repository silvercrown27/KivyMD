from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel

import os

from kivymd.uix.screen import MDScreen

Window.size = (348, 688)

class HomeScreen(MDScreen):
    ''''''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Cyan"

        self.wm = HomeScreen(name="home")

        img_dir = f"../media-player-app/img/"
        img_list = []

        for filename in os.listdir(img_dir):
            f = os.path.join(img_dir, filename)
            if f.endswith('.jpg'):
                img_list.append(f)

        for img in img_list[:6]:
            self.wm.ids.home.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="50dp",
                            width="50dp",
                            source=img,
                            radius=[36, 36, 36, 36],
                        ),
                        MDLabel(
                            text=img,
                        ),
                        orientation="vertical",
                    ),
                    size_hint=(.4, None),
                    height="50dp",
                    spacing="20dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )
        return self.wm


if __name__ == "__main__":
    MainApp().run()