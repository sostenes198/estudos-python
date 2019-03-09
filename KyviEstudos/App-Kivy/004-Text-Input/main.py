#coding: utf-8

from kivy.app import App
from kivy.uix.textinput import  TextInput

def build():
    txtInput = TextInput()
    txtInput.text = "Era um garoto"
    return txtInput
    #return TextInput(text)

janela = App()
janela.build = build
janela.run()