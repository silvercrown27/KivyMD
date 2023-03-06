from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock


# Define the screens
class LoginScreen(Screen):
    pass


class ChatScreen(Screen):
    messages_box = ObjectProperty(None)
    message_input = ObjectProperty(None)

    def send_message(self):
        message_text = self.message_input.text.strip()
        if message_text:
            self.messages_box.add_widget(MDLabel(text=message_text, halign="right"))
            self.message_input.text = ''

    def receive_message(self, message_text):
        self.messages_box.add_widget(MDLabel(text=message_text))


class ScreenManagement(ScreenManager):
    pass


# Define the app
class ChatApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.screen_manager = ScreenManagement()

        # Load the kv file
        Builder.load_file('chat.kv')

        return self.screen_manager

    # Login function
    def login(self, username):
        chat_screen = ChatScreen(name='chat')
        chat_screen.messages_box.add_widget(MDLabel(text=f'Welcome {username}!', halign="center"))
        self.screen_manager.add_widget(chat_screen)
        self.screen_manager.current = 'chat'

        # Receive a welcome message after a second
        Clock.schedule_once(lambda dt: chat_screen.receive_message('Hi there! How can I help you?'), 1)


# Run the app
if __name__ == '__main__':
    ChatApp().run()
