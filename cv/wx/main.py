#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################################
#
#    File Name:    main.py
#    Description:  main routine
#
#######################################################################

#######################################################################
#
#    Author:       esnmlt@gmail.com	
#    Blog:         http://blog.zesn.info (in English)
#                  http://zesn.blogspot.com (in Chinese)
#    Upadate:
#      2009/03/19  File founded
#
#
#######################################################################

from anim import Animation
from gui import MainWindow
import wx

def main():
    anim = Animation()

    app = wx.App()
    frame = MainWindow(None, wx.ID_ANY, anim)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()
    

if __name__ == "__main__":
    main()
