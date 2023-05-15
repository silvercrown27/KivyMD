# import required packages
import sqlite3

from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

# import kivymd prerequisites
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationDrawerItem
# import other dependencies
from screens import homescreen, musicwindow, videoswindow, picturesWindow, libraryWindow, explorewindow, menuscreen


Window.size = (348, 688)

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


class PlayWindow(MDScreen):
    pass


class DrawerClickableItem(MDNavigationDrawerItem):
    def builder(self):
        self.focus_color = "#0000FF"
        self.ripple_color = "#c5bdd2"
        self.selected_color = "#0c6c4d"


class MainApp(MDApp):
    def build(self):
        # Set up theme and title
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "A700"
        self.title = "Media Portal"

        # Bind window resize event
        Window.bind(on_resize=self.on_window_resize)

        # Load the main screen
        self.wm = MainScreen()
        self.sound = None

        # Create screens and add them to the WindowManager
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

        # load the homescreen on appstart
        home_screen = homescreen.HomeScreen()
        home_screen.my_widgets(App.get_running_app())

        # Return the main screen
        return self.wm

    def on_window_resize(self, window, width, height):
        # Update the size and position of the button widget
        self.root.size = (width, height)
        self.root.pos = (0, 0)

    def play_audio(self, media_dirs, curr_iter=0, next_track=None):
        if curr_iter >= len(media_dirs):
            curr_iter = 0
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(media_dirs[curr_iter])
        if self.sound:
            self.sound.play()
            self.sound.bind(on_stop=lambda instance: self.play_audio(media_dirs, curr_iter + 1))

    def pause_music(self):
        if self.sound is not None and self.sound.state == 'play':
            self.paused_pos = self.sound.get_pos()  # get the current position
            self.sound.stop()  # stop the music

    def continue_music(self):
        if self.sound is not None and self.sound.state == 'stop':
            self.sound.play(seek=self.paused_pos)

    def on_start(self):
        self.wm.ids.WindowManager.current = "Splash"


if __name__ == "__main__":

    try:
        mydb = sqlite3.connect("db.sqlite3")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT COUNT(*) FROM folders")
        result = mycursor.fetchone()
        mydb.close()

    except:
        from db.db import create_database
        create_database()

    MainApp().run()
