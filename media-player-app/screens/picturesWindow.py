from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

import random
from .tools import search

class PicturesWindow(MDScreen):
    def on_enter(self, *args):
        app = App.get_running_app()
        self.my_widgets(app)

    def on_leave(self, *args):
        app = App.get_running_app()
        app.wm.ids.WindowManager.screens[3].ids.camera.clear_widgets()
        app.wm.ids.WindowManager.screens[3].ids.educational.clear_widgets()
        app.wm.ids.WindowManager.screens[3].ids.professional.clear_widgets()
        app.wm.ids.WindowManager.screens[3].ids.memes.clear_widgets()

    def my_widgets(self, app):
        img_ext = ['.jpg', '.png', '.jfif']
        img_list = [d for i in img_ext for d in search(i)]

        def create_card(img_path):
            return MDCard(
                MDBoxLayout(
                    FitImage(
                        size_hint=(None, None),
                        height="150dp",
                        width="130dp",
                        source=img_path,
                    ),
                    MDLabel(
                        text=img_path.split("/")[-1],
                    ),
                    orientation="vertical"
                ),
                size_hint=(None, None),
                height="180dp",
                width="130dp",
                focus_behavior=True,
                elevation=3,
            )

        screens = app.wm.ids.WindowManager.screens[3]

        for category in ['camera', 'professional', 'educational', 'memes']:
            category_widget = screens.ids[category]

            # randomly select six images from the list
            selected_imgs = random.sample(img_list[-6:], 6)

            # create a card for each selected image and add it to the widget
            for img in selected_imgs:
                category_widget.add_widget(create_card(img[1]))