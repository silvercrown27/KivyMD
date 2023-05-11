import os

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior

class HomeScreen(MDScreen):
    def my_widgets(self, app):
        img_dir = "img/"
        img_list = [os.path.join(img_dir, filename) for filename in os.listdir(img_dir) if filename.endswith('.jpg')]

        fav_places = app.wm.ids.WindowManager.screens[0].ids.fav_places
        recents_bar = app.wm.ids.WindowManager.screens[0].ids.recents_bar
        playlists = app.wm.ids.WindowManager.screens[0].ids.playlists
        plays = app.wm.ids.WindowManager.screens[0].ids.plays

        for img in img_list[:6]:
            fav_places.add_widget(
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

        def create_card(widget_id, img, height, width, radius=(0, 0, 0, 0)):
            widget_id.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height=height,
                            width=width,
                            radius=radius,
                            source=img,
                        ),
                        MDLabel(
                            text=img[4:-3],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height=height+30,
                    width=width,
                    spacing="10dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )

        for img in img_list:
            create_card(recents_bar, img, 150, 130)

        for img in img_list[-4:]:
            create_card(playlists, img, 150, 160)

        for img in img_list[-6:]:
            create_card(plays, img, 45, 55, radius=(36, 36, 36, 36))

class NavBar(CommonElevationBehavior, MDFloatLayout):
    pass
