from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.utils import rgba
from kivy.clock import Clock
from plyer import filechooser
import webbrowser
import configparser

from scripts.smart_splitter import smart_splitter
from scripts.get_input import get_input

Window.size = (360, 640)
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

Builder.load_file(".\\resources\\main.kv")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(MDApp):

    input_selection=[]
    input_images=[]

    def build(self):
        # Create the screen manager
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

    def setbg(self, checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def open_repo(self):
        toast('Opening repo',  duration=1)
        Clock.schedule_once(lambda repo: webbrowser.open("https://github.com/jayrfs/Machi"), .5)
    
    def file_chooser(self):
        Clock.schedule_once(lambda repo: filechooser.open_file(on_selection=self.selected, multiple=True), .3)

    def selected(self, selection):
        self.input_selection = selection
        print(self.input_selection)
        self.input_images = get_input(self.input_selection)
        print(len(self.input_images))
        return()

    def call_splitter(self):
        smart_splitter(self.input_images[0])

if __name__ == '__main__':
    TestApp().run()