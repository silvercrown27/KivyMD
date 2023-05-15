import sqlite3

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, IconRightWidget, IconLeftWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

conn = sqlite3.connect('../db.sqlite3')

cursor = conn.cursor()
data = cursor.execute("SELECT name, id FROM folders WHERE folder_id IS NULL")
data = data.fetchall()
items = data
print(items)


class HomeScreen(Screen):
    def on_pre_enter(self):
        self.load_items(items)

    def load_items(self, items):
        self.ml = MDApp.get_running_app().ml
        self.ml.clear_widgets()

        items = sorted(items, key=lambda i: (not "." in i[0], i[0].split(".")[-1]))

        for i in items:
            icon = "folder" if self.is_folder(i[1]) else "file"
            self.ml.add_widget(
                TwoLineAvatarIconListItem(
                    IconLeftWidget(
                        icon=icon,
                    ),
                    text=i[0],
                    on_release=lambda btn, item=i: self.load_items(search_database(item[1]))
                    if self.is_folder(item[1]) else None
                )
            )

    def is_folder(self, id):
        data = cursor.execute(f"SELECT id FROM folders WHERE folder_id='{id}'")
        data = data.fetchone()
        return True if data else False



class MainApp(MDApp):
    def on_start(self):
        self.load_items()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.wm = ScreenManager()
        self.hs = HomeScreen(name='home')
        self.ds = MDListScreen(name='details')

        self.sview = MDScrollView()
        self.bl = MDBoxLayout(adaptive_height=True)
        self.ml = MDList()

        self.bl.add_widget(self.ml)
        self.sview.add_widget(self.bl)
        self.hs.add_widget(self.sview)

        self.wm.add_widget(self.hs)
        self.wm.add_widget(self.ds)

        return self.wm

    def load_items(self, items=None):
        if items is None:
            items = search_database(None)

        self.hs.load_items(items)

    def show_details(self, items):
        self.ds.ml.clear_widgets()

        for i in items:
            self.ds.ml.add_widget(
                MDCard(
                    TwoLineAvatarIconListItem(
                        IconRightWidget(
                            icon="dots-vertical",
                        ),
                        text=i[0],
                        on_release=None
                    ),
                    size_hint=(.9, .3),
                    radius=(10, 10, 10, 10),
                )
            )

        self.wm.current = 'details'


def search_database(id):
    if id is None:
        data = cursor.execute("SELECT name, id FROM folders WHERE folder_id IS NULL UNION SELECT name, id FROM files WHERE folder_id IS NULL")
        data = data.fetchall()

        return data

    data = cursor.execute(f"SELECT name, id FROM folders WHERE folder_id='{id}' UNION SELECT name, id FROM files WHERE folder_id='{id}'")
    data = data.fetchall()

    return data


class MDListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sview = MDScrollView()
        self.bl = MDBoxLayout(adaptive_height=True)
        self.ml = MDList()

        self.bl.add_widget(self.ml)
        self.sview.add_widget(self.bl)
        self.add_widget(self.sview)


if __name__ == "__main__":
    MainApp().run()