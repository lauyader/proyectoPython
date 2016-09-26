#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################################
#
#    File Name:    gui.py
#    Description:  generate GUI window
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

from __future__ import division

import os
import sys
import wx
import  wx.lib.scrolledpanel as scrolled

from anim import Animation

fps = 30        # Frames per second


class MainWindow(wx.Frame):

    def __init__(self, parent, id, animation=None):


        # Animation direction. 1 forward, -1 backward
        self.simuDirect = 1

        wx.Frame.__init__(self, parent, id, 'Controller', size=(600, 400))

        self.animation = animation

        self.dashboard = scrolled.ScrolledPanel(self, -1, style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)

        # Text
        text = "Anmimation speed"
        self.explaination = wx.StaticText(self.dashboard, -1, text)

        # Animation speed control
        self.slider = wx.Slider(self.dashboard, -1, fps, 1, 2*fps, pos=(30, 10), size=(250, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
        # Start button
        self.button_st = wx.Button(self.dashboard, -1, "Start", (70, 30))
        # Stop button
        self.button_sp = wx.Button(self.dashboard, -1, "Stop", (70, 30))

        # Next button
        self.button_nt = wx.Button(self.dashboard, -1, "Next", (70, 30))
        # Previous button
        self.button_pr = wx.Button(self.dashboard, -1, "Previous", (70, 30))

        # Timer
        self.timer = wx.Timer(self)

        self.CenterOnScreen()
        self.CreateStatusBar()
        self.SetStatusText("Demo of Vpython & wxPython")

        # Menu
        # Prepare the menu bar
        self.menuBar = wx.MenuBar()
        # 1st menu from left
        self.menu1 = wx.Menu()

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):

        # 2nd menu from left
        self.menu1.Append(101, "About")
        self.menuBar.Append(self.menu1, "&Help")
        self.SetMenuBar(self.menuBar)
        self.Bind(wx.EVT_MENU, self.ShowAbout, id=101)

        # Start & Stop Button
        self.Bind(wx.EVT_BUTTON, self.startAnim,self.button_st)
        self.Bind(wx.EVT_BUTTON, self.stopAnim,self.button_sp)
        self.button_sp.Disable()

        # Next & Previous Button
        self.Bind(wx.EVT_BUTTON, self.nextAnim,self.button_nt)
        self.Bind(wx.EVT_BUTTON, self.previousAnim,self.button_pr)

        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        self.slider.SetTickFreq(5, 1)
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate)

        self.dashboard.SetAutoLayout(1)
        self.dashboard.SetupScrolling()


    def __do_layout(self):

        # sizer for dashboard
        sizer_db = wx.BoxSizer(wx.VERTICAL)

        sizer_db_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_db_1.Add(self.button_st, 0)
        sizer_db_1.Add(self.button_sp, 0, wx.ALIGN_LEFT | wx.LEFT | wx.BOTTOM , 5)

        sizer_db_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_db_2.Add(self.button_nt, 0)
        sizer_db_2.Add(self.button_pr, 0, wx.ALIGN_LEFT | wx.LEFT | wx.BOTTOM , 5)

        sizer_db.Add((-1, 25))
        sizer_db.Add(self.explaination, 0, wx.LEFT, 20)
        sizer_db.Add((-1, 25))
        sizer_db.Add(self.slider, 0, wx.LEFT, 10)
        sizer_db.Add((-1, 25))
        sizer_db.Add(sizer_db_1, 0, wx.ALIGN_LEFT | wx.LEFT, 5)
        sizer_db.Add(sizer_db_2, 0, wx.ALIGN_LEFT | wx.LEFT, 5)
        self.dashboard.SetSizer(sizer_db)

        sizer = wx.BoxSizer()
        sizer.Add(self.dashboard,1, wx.EXPAND)
        self.SetSizer(sizer)



    def CloseWindow(self, event):
        self.Close()


    def ShowAbout(self, event):
        dlg = wx.MessageDialog(self, 'Demo of Vpython & wxPython by esnmlt@gmail.com',
                               'About',
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()



    # Under modification
    def sliderUpdate(self, evt):
        if self.timer.IsRunning():
            self.timer.Start(1000/self.slider.GetValue())
    

    def update(self, evt=None):
        #print "update!"
        if self.animation != None:
            self.animation.update(direct=self.simuDirect)
        else:
            self.showInfo(msg="Initialize First!", title='Warning')
            #print "Initialize first!"


    def startAnim(self, evt):
        self.simuDirect = 1

        if self.animation is not None:
            self.timer.Start(1000/self.slider.GetValue())
            self.button_sp.Enable()
        else:
            self.showInfo(msg="Initialize First!", title='Warning')
            #print "Initialize first!"

    def stopAnim(self, evt):
        if self.timer.IsRunning():
            self.timer.Stop()
            self.button_sp.Disable()
        
    def nextAnim(self, evt):
        self.simuDirect = 1
        self.update()


    def previousAnim(self, evt):
        self.simuDirect = -1
        self.update()


    def showInfo(self, msg='Hello World!', title='Information'):
        dlg = wx.MessageDialog(self, msg, title,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()


# end of class MainWindow

if __name__ == '__main__':
    #app = wx.PySimpleApp()
    app = wx.App()
    frame = MainWindow(None, wx.ID_ANY, None)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

