# coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    print(txt.text)


def build():
    layout = FloatLayout()

    txt = TextInput(text="Text base")
    global txt
    txt.size_hint = None, None
    txt.height = 300
    txt.width = 400
    txt.x = 200
    txt.y = 250

    btn = Button(text="Clique aqui")
    btn.height = 50
    btn.width = 260
    btn.x = 250
    btn.y = 100
    btn.size_hint = None, None
    btn.on_press = click

    layout.add_widget(txt)
    layout.add_widget(btn)

    return layout


janela = App()
janela.title = "Meu primeiro app"
janela.build = build
janela.run()
