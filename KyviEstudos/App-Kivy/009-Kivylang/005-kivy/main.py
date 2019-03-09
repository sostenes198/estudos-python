# coding: UTF-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import kivy
kivy.require("1.10.1")

def funcSelf(x):
    print("funcSelf")

Button.funcSelf = funcSelf



class MinhaTela(BoxLayout):

    def funcRoot(self):
        print("funcRoot")



class Root(App):

    def funcApp(self):
        print("funcApp")


janela = Root()
janela.run()