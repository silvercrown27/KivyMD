from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

KV = '''
ScreenManager:
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'My Screen'
                md_bg_color: app.theme_cls.primary_color
                elevation: 10
            Widget:
        MDBottomAppBar:
            md_bg_color: app.theme_cls.primary_color
            elevation: 10
            mode: 'end'
            type: 'bottom'
            icon: 'android'
            on_action_button: app.action_button_click()
'''


class MyScreen(Screen):
    pass


class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        screen = Builder.load_string(KV)
        screen.add_widget(MyScreen(name='myscreen'))
        return screen

    def action_button_click(self):
        print('Action button clicked!')


if __name__ == '__main__':
    TestApp().run()
