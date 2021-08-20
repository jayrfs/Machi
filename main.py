from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.utils import rgba
from kivy.clock import Clock
from plyer import filechooser
import webbrowser

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Window.size = (360, 640)

Builder.load_string("""
<MenuScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Machi"
            elevation: 12
            type: "top"
            right_action_items: [["penguin", lambda github: app.open_repo()]]
            
        MDFloatLayout:
            MDTextField:
                id: input_path
                icon_right: 'folder-open-outline'
                icon_right_color: rgba("#EC407A")
                hint_text: "Input Path"
                mode: "rectangle"
                color_mode: "custom"
                pos_hint: {"center_x":0.5, "center_y":0.9}
                size_hint_x: .8
                height: "30dp"
                on_focus:
                    app.file_chooser()

            MDRectangleFlatButton:
                text: 'About'
                pos_hint: {"center_x":.5, "y":0.1}
                size_hint_x: .3
                on_release:
                    root.manager.current = 'settings'
                    root.manager.transition.direction = 'left'
            MDRectangleFlatButton:
                text: 'Go to settings'
                size_hint_x: .3
                pos_hint: {"center_x":0.5, "center_y":0.6}
                on_release:

<SettingsScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Machi"
            type: "top"
            right_action_items: [["penguin"]]
        MDFloatLayout:
            MDRectangleFlatButton:
                text: 'My settings MDRectangleFlatButton'
                pos_hint: {"center_x":0.5, "center_y":0.6}
            MDRectangleFlatButton:
                text: 'Back to menu'
                on_release: 
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
                pos_hint: {"center_x":0.5, "center_y":0.3}
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"
        #self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

    def open_repo(self):
        toast('Opening repo',  duration=1)
        Clock.schedule_once(lambda repo: webbrowser.open("https://github.com/jayrfs/Machi"), .5)
    
    def file_chooser(self):
        Clock.schedule_once(lambda repo: filechooser.open_file(on_selection=self.selected), .3)

    def selected(self, selection):
        print(selection)

if __name__ == '__main__':
    TestApp().run()