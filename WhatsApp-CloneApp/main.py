import kivy
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (342, 720)

Builder.load_file("story.kv")

class WindowManager(ScreenManager):
    """"""


class MessageScreen(Screen):
    """"""


class StoryWithImage(MDBoxLayout):
    text = StringProperty()
    source = StringProperty()


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = 'Cyan'
        self.theme_cls.accent_hue = '600'
        self.title = "WhatsApp Design"

        screens = [
            MessageScreen(name="message")
        ]

        self.wm = WindowManager(transition=FadeTransition())

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm


if __name__ == "__main__":
    MainApp().run()