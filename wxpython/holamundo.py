#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

###########################################################
# Definición de la aplicacion
###########################################################

class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, pos=(0, 0), size=(320, 240))
        panel = wx.Panel(self, wx.ID_ANY)
        text = wx.StaticText(panel, wx.ID_ANY, "Aplicación, de hola mundo!", wx.Point(10, 5), wx.Size(-1, -1))


###########################################################
# Marco de la Ventana
###########################################################
class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, wx.ID_ANY, " Ventana:Hello, world!")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = TestApp()
    app.MainLoop()
