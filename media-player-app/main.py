# import required packages
import os.path
import sqlite3

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

# import kivymd prerequisites
from kivymd.app import MDApp
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
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


class CustomImage(Image):
    def on_load(self, *args):
        # Add your custom animation or loading behavior here
        # For example, display a fade-in animation:
        self.canvas.opacity = 0
        self.canvas.add(Color(1, 1, 1, 0))
        self.canvas.add(Rectangle(size=self.texture_size, texture=self.texture))
        anim = Animation(opacity=1, duration=0.5)
        anim.start(self)

class Splash(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 11)

    def switch_to_home(self, dt):
        self.manager.current = "HomeScreen"


class MainScreen(Screen):
    ''''''


class PlayWindow(MDScreen):
    pass

class MusicBar(CommonElevationBehavior, MDFloatLayout):
    def __init__(self, current_track, **kwargs):
        super(MusicBar, self).__init__(**kwargs)
        self.current_track = os.path.basename(current_track)
        self.update_playing_text(self.current_track)

    def update_playing_text(self, text):
        self.ids.playing.text = text


class DrawerClickableItem(MDNavigationDrawerItem):
    ''''''

class Bottom_Navigation(MDBoxLayout):
    pass

class LoginScreens(MDScreen):
    pass
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
        self.current_music_bar = None

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

        for screen in self.wm.ids.WindowManager.screens[:-1]:
            screen.ids.page_start.add_widget(Bottom_Navigation())

        # load the homescreen on appstart
        home_screen = homescreen.HomeScreen()
        home_screen.my_widgets(MDApp.get_running_app())

        # Return the main screen
        return self.wm

    def on_window_resize(self, window, width, height):
        # Update the size and position of the button widget
        self.root.size = (width, height)
        self.root.pos = (0, 0)

    def play_audio(self, media_dirs, curr_iter=0):
        if curr_iter >= len(media_dirs):
            curr_iter = 0

        # Stop the currently playing song
        if self.sound:
            self.sound.stop()

        track = media_dirs[curr_iter]
        self.sound = SoundLoader.load(track)

        if self.sound:
            self.sound.play()

        # Remove the existing MusicBar widget if it exists
        if self.current_music_bar:
            current_screen = self.wm.ids.WindowManager.current_screen
            current_screen.ids.page_start.remove_widget(self.current_music_bar)

        # Add MusicBar widget to the current screen
        current_screen = self.wm.ids.WindowManager.current_screen
        self.current_music_bar = MusicBar(track)
        current_screen.ids.page_start.add_widget(self.current_music_bar)

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
        with sqlite3.connect("db.sqlite3") as mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT COUNT(*) FROM folders")
            result = mycursor.fetchone()

    except:
        from db.db import create_database
        create_database()

    MainApp().run()