import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition

from kivymd.app import MDApp

Window.size = (328, 692)
Builder.load_file("homescreen.kv")


class WindowManager(ScreenManager):
    """"""


class HomeScreen(Screen):
    """"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Blue"
        self.theme_cls.accent_hue = "700"
        self.title = "Media Verse"

        screens = [
            HomeScreen(name="Home")
        ]
        self.wm = WindowManager(transition=SwapTransition())

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item):

        self.root.ids.screen_manager.current = (
            instance_navigation_rail_item.icon.split("-")[1].lower()
        )


if __name__ == "__main__":
    MainApp().run()