# coding: UTF-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import kivy
kivy.require("1.10.1")

class MinhaTela(BoxLayout):

    def click(self):
        self.ids.lb1.text = ""
        self.ids.lb2.text = "10"



class Root(App):

    def build(self):
        pass


janela = Root()
janela.run()