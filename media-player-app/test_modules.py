from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Go to Screen 2", on_release=self.goto_screen2))
        self.add_widget(MDRaisedButton(text="Go to Screen 3", on_release=self.goto_screen3))
        self.add_widget(MDRaisedButton(text="Close Drawer", on_release=self.close_drawer))

    def goto_screen2(self, *args):
        self.parent.parent.current = "screen2"
        self.close_drawer()

    def goto_screen3(self, *args):
        self.parent.parent.current = "screen3"
        self.close_drawer()

    def open_drawer(self):
        self.parent.parent.toggle_nav_drawer()

    def close_drawer(self, *args):
        self.parent.parent.toggle_nav_drawer()


class Screen2(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Go back to Main Screen", on_release=self.goto_main))

    def goto_main(self, *args):
        self.parent.parent.current = "main"


class Screen3(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Go back to Main Screen", on_release=self.goto_main))

    def goto_main(self, *args):
        self.parent.parent.current = "main"


class NavigationDrawer(MDNavigationDrawer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDRaisedButton(text="Main Screen", on_release=self.goto_main))
        self.add_widget(MDRaisedButton(text="Screen 2", on_release=self.goto_screen2))
        self.add_widget(MDRaisedButton(text="Screen 3", on_release=self.goto_screen3))

    def goto_main(self, *args):
        self.parent.parent.current = "main"
        self.toggle_nav_drawer()

    def goto_screen2(self, *args):
        self.parent.parent.current = "screen2"
        self.toggle_nav_drawer()

    def goto_screen3(self, *args):
        self.parent.parent.current = "screen3"
        self.toggle_nav_drawer()


class TestApp(MDApp):
    def build(self):
        layout = MDNavigationLayout()

        screen_manager = MDScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(Screen2(name="screen2"))
        screen_manager.add_widget(Screen3(name="screen3"))

        nav_drawer = NavigationDrawer()

        layout.add_widget(screen_manager)
        layout.add_widget(nav_drawer)

        return layout


if __name__ == '__main__':
    TestApp().run()
