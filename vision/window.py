from kivy.app import App
from kivy.uix.label import Label

class MyWindow(App):

    def build(self):
        return Label(text='Hello world')
