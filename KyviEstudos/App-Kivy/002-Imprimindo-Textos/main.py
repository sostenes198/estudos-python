#coding: utf-8


from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = "Curso de python kivy"
    lb.italic = True
    lb.font_size = 50
    return lb
    #return Label(text="Curso de python kivy", italic=True, font_size=50)

app = App()
app.build = build

app.run()