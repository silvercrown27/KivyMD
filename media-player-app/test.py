from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

kv = '''
#:kivy 2.0.0

<CustomTabbedPanel>:
    do_default_tab: False
    tab_width: 150
    tab_height: 50
    size_hint_y: 0.8
    background_color: [0.2,0.2,0.2,1]
    pos_hint: {'center_x': .5, 'center_y': .5}

<Tab1Content>:
    Label:
        text: 'Tab 1 Content'

<Tab2Content>:
    Label:
        text: 'Tab 2 Content'

<Tab3Content>:
    Label:
        text: 'Tab 3 Content'

<Tab4Content>:
    Label:
        text: 'Tab 4 Content'

<TopAppBar>:
    size_hint_y: 0.1
    padding: 10
    Label:
        text: 'App Title'
        font_size: '20sp'
        valign: 'center'

<RootLayout>:
    TopAppBar:
        pos_hint: {'top': 1}
    CustomTabbedPanel:
        Tab1Content:
            text: 'Tab 1'
        Tab2Content:
            text: 'Tab 2'
        Tab3Content:
            text: 'Tab 3'
        Tab4Content:
            text: 'Tab 4'
    BottomAppBar:
        pos_hint: {'bottom': 1}
        size_hint_x: 0.9
        padding: 10
        Button:
            text: 'FAB 1'
            size_hint: None, None
            size: 50, 50
        Button:
            text: 'FAB 2'
            size_hint: None, None
            size: 50, 50

'''
class RootLayout(FloatLayout):
    pass


class CustomTabbedPanel(TabbedPanel):
    pass


class TopAppBar(FloatLayout):
    pass


class Tab1Content(FloatLayout):
    pass


class Tab2Content(FloatLayout):
    pass


class Tab3Content(FloatLayout):
    pass


class Tab4Content(FloatLayout):
    pass


class BottomAppBar(FloatLayout):
    pass


class MyApp(App):

    def build(self):
        Builder.load_file('my.kv')
        return RootLayout()


if __name__ == '__main__':
    MyApp().run()
