import socket
import pyautogui

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from kivy.uix.screenmanager import ScreenManager

def touch_read_func():
    # Set up a socket connection to receive touch input from Android device
    HOST = ''  # Use default host (localhost)
    PORT = 5000  # Choose an arbitrary port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()

    # Define the screen size of the PC
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

    # Receive touch input from Android device and move the mouse cursor accordingly
    while True:
        data = conn.recv(1024)
        if not data:
            break
        x, y = data.decode().split(',')
        x = int(x)
        y = int(y)
        x = int(x * SCREEN_WIDTH / 100)  # Convert x-coordinate to match PC screen size
        y = int(y * SCREEN_HEIGHT / 100)  # Convert y-coordinate to match PC screen size
        pyautogui.moveTo(x, y)


class HomeScreen(MDScreen):
    ''''''
    touch_read_func()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_hue = "700"

        self.sm = ScreenManager()

        screens = [
            HomeScreen(name="Home"),
        ]

        for screen in screens:
            self.sm.add_widget(screen)

        return self.sm


if __name__ == "__main__":
    MainApp().run()