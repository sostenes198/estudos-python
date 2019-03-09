# coding: UTF-8

from kivy.app import App
from kivy.lang import Builder

import kivy
kivy.require("1.10.1")

code = """

    BoxLayout:
        Button:
            text: "1"
        Button: 
            text: "2"
            
"""


class Root(App):

    @property
    def build(self):
        return Builder.load_string(code)


janela = Root()
janela.run()