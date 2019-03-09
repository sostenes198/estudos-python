#coding: utf-8


from kivy.app import App
from kivy.uix.label import Label

class MeuProg(App):

    def build(self):
        lbl = Label()
        return lbl

MeuProg().run()