from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# Set up the screens
class HomeScreen(Screen):
    pass

class MusicScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

# Create a screen manager
class ScreenManagement(ScreenManager):
    pass

# Create the app
class MediaApp(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = ScreenManagement()
        
        # Load the kv files
        Builder.load_file('media.kv')
        
        return self.screen_manager

    # Navigation functions
    def go_home(self):
        self.screen_manager.current = 'home'
        
    def go_music(self):
        self.screen_manager.current = 'music'
        
    def go_video(self):
        self.screen_manager.current = 'video'

# Home screen
class HomeScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cards = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.add_widget(self.cards)
        
    def add_playlist(self, playlist):
        card = MDCard(orientation='vertical', padding=20)
        card_title = MDTopAppBar(title=playlist['title'])
        card.add_widget(card_title)
        card_content = GridLayout(cols=2, spacing=20, padding=20)
        card.add_widget(card_content)
        card_artwork = ObjectProperty(None)
        card_artwork.source = playlist['artwork']
        card_content.add_widget(card_artwork)
        card_info = BoxLayout(orientation='vertical')
        card_content.add_widget(card_info)
        card_description = ObjectProperty(None)
        card_description.text = playlist['description']
        card_info.add_widget(card_description)
        card_play_button = MDIconButton(icon='play', pos_hint={'center_x': 0.5})
        card_play_button.bind(on_press=lambda x: MediaApp().go_music())
        card_info.add_widget(card_play_button)
        self.cards.add_widget(card)

# Music screen
class MusicScreen(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tracks = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.add_widget(self.tracks)
        
    def add_track(self, track):
        card = MDCard(orientation='vertical', padding=20)
        card_title = MDTopAppBar(title=track['title'])
        card.add_widget(card_title)
        card_content = GridLayout(cols=2, spacing=20, padding=20)
        card.add_widget(card_content)
        card_artwork = ObjectProperty(None)
        card_artwork.source = track['artwork']
        card_content.add_widget(card_artwork)
        card_info = BoxLayout(orientation='vertical')
        card_content.add_widget(card_info)
        card_description = ObjectProperty(None)
        card_description.text = track['description']
        card_info.add_widget(card_description)
        card_play_button = MDIconButton(icon='play', pos_hint={'center_x': 0.5})
        card_play_button.bind(on_press=lambda x: MediaApp().play)


if __name__ == '__main__':
    MediaApp().run()

