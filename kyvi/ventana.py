#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text = '¡Hola mundo!')

if __name__=='__main__':
    MyApp().run()