from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '550')
Config.set('graphics', 'custom_titlebar', '0')

# ラベルとボタン情報を設定
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner

class Menubar(Spinner):
    pass

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def hi_on(self):
        self.ids.menubuttonsource.source = "icons/top_button_pressed.png"
        #self.ids.menubuttonsource.center_x = self.parent.center_x
        #self.ids.menubuttonsource.center_y = self.parent.center_y
        print("Hi")
    def hi_off(self):
        self.ids.menubuttonsource.source = "icons/top_button.png"

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "window"
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
