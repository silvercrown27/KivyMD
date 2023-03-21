from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition

from kivymd.app import MDApp
from kivymd.uix.imagelist.imagelist import MDSmartTile
from screens.homescreen import HomeScreen

import os

Window.size = (328, 688)

Builder.load_file("screens/home-screen.kv")


class WindowManager(ScreenManager):
    """"""


class MainScreen(Screen):
    ''''''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.accent_hue = "700"
        self.title = "Media Portal"

        self.wm = WindowManager()

        screens = [
            HomeScreen(name="HomeScreen"),
        ]

        self.wm = WindowManager(transition=SwapTransition())

        for screen in screens:
            MainScreen().ids.WindowManager.add_widget(screen)

        # self.my_widgets()

        return Builder.load_file("MainScreen.kv")

    def my_widgets(self):
        img_dir = f"img/"
        img_list = []

        for filename in os.listdir(img_dir):
            f = os.path.join(img_dir, filename)
            if f.endswith('.jpg'):
                img_list.append(f)
        print(img_list)

        for img in img_list:
            self.wm.screens[0].ids.recents_bar.add_widget(
                MDSmartTile(
                    size_hint=(None, None),
                    height="180dp",
                    width="170dp",
                    source='img',
                )
            )


if __name__ == "__main__":
    MainApp().run()
