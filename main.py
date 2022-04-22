"""
░█████╗░░█████╗░██╗░░░░░░█████╗░  ██████╗░██╗░░░██╗  ░██████╗███████╗██╗░░░░░██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗╚██╗░██╔╝  ██╔════╝██╔════╝██║░░░░░╚██╗░██╔╝██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝  ██████╦╝░╚████╔╝░  ╚█████╗░█████╗░░██║░░░░░░╚████╔╝░███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗  ██╔══██╗░░╚██╔╝░░  ░╚═══██╗██╔══╝░░██║░░░░░░░╚██╔╝░░██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝  ██████╦╝░░░██║░░░  ██████╔╝███████╗███████╗░░░██║░░░██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░  ╚═════╝░░░░╚═╝░░░  ╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝
"""

import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics','resizable', 0)
Config.set('graphics','width', 400)
Config.set('graphics','height', 500)


class CalcApp(App):
    def calc_operation(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = '0'

    def update_label(self):
        self.lbl.text = self.formula

    def press_number(self, instance):
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)

        self.update_label()


    def press_znak(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += "*"
        else:
            self.formula += str(instance.text)
 
        self.update_label()

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = 'vertical', padding = 25)
        gl = GridLayout(cols=4, spacing=3, size_hint = (1, .6))

        self.lbl = Label(text = '0', font_size = 40, halign = 'right', size_hint = (1, .4), text_size = (400-50, 500 * .4), valign = 'center')

        bl.add_widget(self.lbl)

        bl.add_widget(gl)

        gl.add_widget(Button(text='7',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='8',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='9',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='/',background_color = (0,0,0,1),font_size = 25, on_press = self.press_znak))

        gl.add_widget(Button(text='4',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='5',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='6',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='X',background_color = (0,0,0,1),font_size = 25, on_press = self.press_znak))

        gl.add_widget(Button(text='1',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='2',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='3',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='+',background_color = (0,0,0,1),font_size = 25, on_press = self.press_znak))

        gl.add_widget(Button(text='.',background_color = (0,0,0,1),font_size = 25, on_press = self.press_znak))
        gl.add_widget(Button(text='0',background_color = (0,0,0,1),font_size = 25, on_press = self.press_number))
        gl.add_widget(Button(text='=',background_color = (0,0,0,1),font_size = 25, on_press = self.calc_operation))
        gl.add_widget(Button(text='-',background_color = (0,0,0,1),font_size = 25, on_press = self.press_znak))

        return bl

if __name__ == '__main__':
    CalcApp().run()