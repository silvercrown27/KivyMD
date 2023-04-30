from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

import os


class PicturesWindow(MDScreen):
    def my_widgets(self):
        img_dir = f"img/"
        img_list = []

        for filename in os.listdir(img_dir):
            f = os.path.join(img_dir, filename)
            if f.endswith('.jpg'):
                img_list.append(f)

        for img in img_list[-6:]:
            self.wm.ids.WindowManager.screens[3].ids.camera.add_widget(
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
            self.wm.ids.WindowManager.screens[3].ids.professional.add_widget(
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
            self.wm.ids.WindowManager.screens[3].ids.educational.add_widget(
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
            self.wm.ids.WindowManager.screens[3].ids.memes.add_widget(
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