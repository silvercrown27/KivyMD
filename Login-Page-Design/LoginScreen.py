from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

from kivymd.app import MDApp

Window.size = (320, 698)
Builder.load_file('LoginScreen.kv')


class WindowManager(ScreenManager):
    """"""


class LoginScreen(Screen):
    """"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "600"
        self.title = "Re-Connect"

        screens = [
            LoginScreen(name="Login"),
        ]
        self.wm = WindowManager(transition=FadeTransition())

        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm


if __name__ == "__main__":
    MainApp().run()