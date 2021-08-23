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
from kivy.storage.jsonstore import JsonStore
import webbrowser, cv2

from scripts.smart_splitter import smart_splitter
from scripts.get_input import get_input
from scripts.frames_stitcher import stitchy_code
from scripts.write_output import write_output
from scripts.smart_split_gui_loop import smart_split_gui_loop

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

class MachiApp(MDApp):

    input_selection=[]
    input_images=[]
    store = JsonStore('config.json')
    if store.exists('configstuff'):
        pass
    else:
        store.put('configstuff',theme='dark')
    if store.get('configstuff')['theme']=='dark':
        btheme = False
    else:
        btheme = True
    print(f"btheme = {btheme}")

    def on_start(self):
        #bad code, replace with set_bg later
        if self.store.get('configstuff')['theme']=='light':
            self.theme_cls.theme_style = "Light"
        elif self.store.get('configstuff')['theme']=='dark':
            self.theme_cls.theme_style = "Dark"

    def build(self):
        yolo="hahaha"
        # Create the screen manager
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"

        #load config stuff


        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

    def setbg(self, checkbox, value):
        if value:
            self.store.put('configstuff',theme='light')
        else:
            self.store.put('configstuff',theme='dark')
        if self.store.get('configstuff')['theme']=='light':
            self.theme_cls.theme_style = "Light"
        elif self.store.get('configstuff')['theme']=='dark':
            self.theme_cls.theme_style = "Dark"

    def open_repo(self):
        toast('Opening repo',  duration=1)
        Clock.schedule_once(lambda repo: webbrowser.open("https://github.com/jayrfs/Machi"), .5)
    
    def file_chooser(self):
        Clock.schedule_once(lambda repo: filechooser.open_file(on_selection=self.selected, multiple=True), .3)

    def selected(self, selection):
        self.input_selection = selection
        print(self.input_selection)
        get_input(self.input_selection)
        return()

    def call_splitter(self):
        smart_split_gui_loop(0)
        

    def call_stitcher(self):
        finelimages = stitchy_code(self)
        write_output(finelimages)

if __name__ == '__main__':
    MachiApp().run()