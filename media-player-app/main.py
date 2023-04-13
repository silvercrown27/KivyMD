# import required kivy packages
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

# import kivymd prerequisites
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationDrawerItem
# import other dependencies
from screens import homescreen, musicwindow, videoswindow, picturesWindow, libraryWindow, explorewindow, menuscreen
import os

Window.size = (328, 688)

# Load required kv filed
Builder.load_file("screens/home-screen.kv")
Builder.load_file("screens/music-screen.kv")
Builder.load_file("screens/videos-screen.kv")
Builder.load_file("screens/pictures.kv")
Builder.load_file("screens/library.kv")
Builder.load_file("screens/explore.kv")
Builder.load_file("screens/menu-screen.kv")


class Splash(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 11)

    def switch_to_home(self, dt):
        self.manager.current = "HomeScreen"


class MainScreen(Screen):
    ''''''


class DrawerClickableItem(MDNavigationDrawerItem):
    def builder(self):
        self.focus_color = "#0000FF"
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"


class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "700"
        self.title = "Media Portal"

        Window.bind(on_resize=self.on_window_resize)

        # Loading the main app
        self.wm = MainScreen()

        screens = [
            homescreen.HomeScreen(name="HomeScreen"),
            musicwindow.MusicWindow(name="MusicWindow"),
            videoswindow.VideosWindow(name="VideosWindow"),
            picturesWindow.PicturesWindow(name="PicturesWindow"),
            libraryWindow.LibraryWindow(name="LibraryWindow"),
            explorewindow.ExploreWindow(name="ExploreWindow"),
            menuscreen.MenuWindow(name="MenuWindow"),
            Splash(name="Splash"),
        ]
        for screen in screens:
            self.wm.ids.WindowManager.add_widget(screen)

        homescreen.HomeScreen.my_widgets(self)

        return self.wm

    def on_window_resize(self, window, width, height):
        # Update the size and position of the button widget
        self.root.size = (width, height)
        self.root.pos = (0, 0)


    # def on_start(self):
    #     self.wm.ids.WindowManager.current = "Splash"


if __name__ == "__main__":
    MainApp().run()
