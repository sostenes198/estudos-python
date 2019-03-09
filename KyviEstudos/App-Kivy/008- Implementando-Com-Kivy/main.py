
from tkinter import Widget


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config
Config.set("modules", "console", "")

class Tela1(BoxLayout):
    
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())



class Tela2(BoxLayout):
    
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())
    

class Root(App):
    pass


janela = Root()
janela.run()
