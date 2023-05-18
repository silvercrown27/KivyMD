import random
from json import load
from datetime import datetime

from kivymd.app import MDApp

from .tools import search

from kivy.clock import Clock

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout

day = datetime.today().strftime("%A")
time = datetime.now()

with open('db/greet.json', 'r') as f:
    greet = load(f)

if time.hour < 12:
    greeting = greet['morning']
elif time.hour < 18:
    greeting = greet['afternoon']
else:
    greeting = greet['evening']
header = greeting[3]
greeting = greeting[0]

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 1)

    def on_enter(self, *args):
        app = MDApp.get_running_app()
        app.wm.ids.WindowManager.screens[0].ids.topbar.text = header
        app.wm.ids.WindowManager.screens[0].ids.greet.text = greeting
        app.wm.ids.WindowManager.screens[0].ids.user.text = "bradley"
        self.update_time()
        app.wm.ids.WindowManager.screens[0].ids.day.text = day

    # def on_leave(self, *args):
    #     app = MDApp.get_running_app()
        # app.wm.ids.WindowManager.screens[0].ids.recents_bar.clear_widgets()
        # app.wm.ids.WindowManager.screens[0].ids.playlists.clear_widgets()

    def update_time(self, *args):
        app = MDApp.get_running_app()
        app.wm.ids.WindowManager.screens[0].ids.time.text = str(datetime.now().strftime("%H:%M:%S"))

    def my_widgets(self, app):
        img_ext = ['.jpg', '.png', '.jfif']
        img_list = set([d for i in img_ext for d in search(i)])

        fav_places = app.wm.ids.WindowManager.screens[0].ids.fav_places
        recents_bar = app.wm.ids.WindowManager.screens[0].ids.recents_bar
        playlists = app.wm.ids.WindowManager.screens[0].ids.playlists
        plays = app.wm.ids.WindowManager.screens[0].ids.plays

        img_list = set(img_list)
        img_list = [(img[0][:10], img[1]) for img in img_list]

        for img in img_list[12:18]:
            fav_places.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height="45dp",
                            width="50dp",
                            source=img[1],
                        ),
                        MDLabel(
                            text=img[0],
                        ),
                        orientation="horizontal",
                    ),
                    size_hint=(.4, None),
                    height="45dp",
                    spacing="20dp",
                    focus_behavior=True,
                    elevation=0,
                )
            )

        def create_card(widget_id, img, height, width):
            widget_id.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height=height,
                            width=width,
                            source=img[1],
                        ),
                        MDLabel(
                            text=img[0],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height=height+30,
                    width=width,
                    spacing="15dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )

        def create_new_card(widget_id, img, height, width, radius=(0, 0, 0, 0)):
            widget_id.add_widget(
                MDCard(
                    MDBoxLayout(
                        FitImage(
                            size_hint=(None, None),
                            height=height,
                            width=width / 1.5,
                            radius=radius,
                            source=img[1],
                        ),
                        MDLabel(
                            text=img[0],
                        ),
                        orientation="vertical"
                    ),
                    size_hint=(None, None),
                    height=height+30,
                    width=width,
                    spacing="15dp",
                    focus_behavior=True,
                    elevation=3,
                )
            )

        for img in img_list[:6]:
            create_card(recents_bar, img, 150, 130)

        for img in img_list[6:12]:
            create_card(playlists, img, 150, 160)

        for img in img_list[:6]:
            create_new_card(plays, img, 36, 54, radius=(36, 36, 36, 36))