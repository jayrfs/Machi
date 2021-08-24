from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import rgba
from kivy.clock import Clock
from plyer import filechooser
from kivy.storage.jsonstore import JsonStore
import webbrowser, cv2, os
from kivymd.uix.picker import MDThemePicker
from kivymd.toast import toast

from kivymd.uix.list import OneLineListItem

from natsort import natsorted, ns

from scripts.smart_splitter import smart_splitter
from scripts.get_input import get_input
from scripts.frames_stitcher import stitchy_code
from scripts.write_output import write_output
from scripts.smart_split_gui_loop import smart_split_gui_loop
from scripts.smart_stitch_gui_loop import smart_stitch_gui_loop

Window.size = (360, 640)
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.

# Declare both screens
class MachiApp(MDApp):

    local_theme = {}
    input_selection=[]
    files_in_input_folder=[]
    store = JsonStore('config.json')

    def yoda(self):
        self.files_in_input_folder = os.listdir(".//input//")
        files_in_input_folder_sorted = []
        files_in_input_folder_sorted = natsorted(self.files_in_input_folder, alg=ns.IGNORECASE)
        for i in files_in_input_folder_sorted:
            self.root.ids.input_lister_text.add_widget(
                OneLineListItem(text=f"{i}")
            )
        

    def on_start(self):
        self.set_theme_on_start()
        self.yoda()

    def build(self):
        yolo="hahaha"
        # Create the screen manager
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"
        pass

    def open_repo(self):
        toast('Opening repo',  duration=1)
        Clock.schedule_once(lambda repo: webbrowser.open("https://github.com/jayrfs/Machi"), .5)
    
    def file_chooser(self):
        Clock.schedule_once(lambda repo: filechooser.open_file(on_selection=self.selected, multiple=True), .3)

    def flush_input(self):
        self.input_selection = []
        for ffile in os.listdir('.//input//'):
            print(f"remove .//input//{ffile}")
            os.remove(f".//input//{ffile}")
        return()

    def flush_output(self):
        for ffile in os.listdir('.//output//'):
            print(f"remove .//output//{ffile}")
            os.remove(f".//output//{ffile}")
        return()

    def output_to_input(self):
        self.input_selection = []
        for ffile in os.listdir('.//output//'):
            self.input_selection.append(f".//output//{ffile}")
            print(f"copy .//output//{ffile}")
            get_input(self.input_selection)
        return()

    def selected(self, selection):
        self.input_selection = selection
        print(self.input_selection)
        get_input(self.input_selection)
        self.yoda()
        return()

    def call_splitter(self):
        smart_split_gui_loop(0)
        
    def call_smart_stitcher(self):
        smart_stitch_gui_loop(0)

    def call_stitcher(self):
        finelimages = stitchy_code(self)
        write_output(finelimages)

    def set_prefix(self, text):
        text = self.root.get_screen('menu').ids.output-name-box.text
        print(text)

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
        pass

    def set_theme_on_start(self):
        self.local_theme=self.store.get('theme')['local_theme']
        self.theme_cls.theme_style = self.local_theme['self.theme_cls.theme_style']
        self.theme_cls.primary_palette = self.local_theme['self.theme_cls.primary_palette']
        self.theme_cls.accent_palette = self.local_theme['self.theme_cls.accent_palette']
        pass

    def on_stop(self):
        self.local_theme['self.theme_cls.theme_style'] = str(self.theme_cls.theme_style)
        self.local_theme['self.theme_cls.primary_palette'] = str(self.theme_cls.primary_palette)
        self.local_theme['self.theme_cls.accent_palette'] = str(self.theme_cls.accent_palette)
        self.store.put('theme',local_theme = self.local_theme)
        return


if __name__ == '__main__':
    MachiApp().run()