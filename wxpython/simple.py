#!/usr/bin/env python
# -*- coding: utf-8 -*-
try: 
    import wx 
except ImportError:
    raise ImportError,"Se requiere el modulo wxPython"

class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent         
        self.initialize()

    def initialize(self):
        grilla = wx.GridBagSizer()
        self.entrada = wx.TextCtrl(self,-1,value=u"Ingrese un texto:", style=wx.TE_PROCESS_ENTER)
        grilla.Add(self.entrada,(0,0),(1,1),wx.EXPAND)
        self.entrada.Bind(wx.EVT_TEXT_ENTER, self.SiPulsaEnter)
        boton = wx.Button(self,-1,label="Pulsame !")
        grilla.Add(boton, (0,1))
        boton.Bind (wx.EVT_BUTTON, self.SiCliqueaBoton)
        self.etiqueta = wx.StaticText(self,-1,label=u'Hola !')
        self.etiqueta.SetBackgroundColour(wx.BLUE)
        self.etiqueta.SetForegroundColour(wx.WHITE)
        grilla.Add(self.etiqueta, (1,0),(1,2), wx.EXPAND )
        grilla.AddGrowableCol(0)
        self.SetSizerAndFit(grilla)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y )
        self.entrada.SetFocus()
        self.entrada.SetSelection(-1,-1) 
        self.Show(True)

    def SiCliqueaBoton(self,event):
        self.etiqueta.SetLabel(self.entrada.GetValue() +  "Cliqueo el boton!")
        self.entrada.SetFocus()
        self.entrada.SetSelection(-1,-1) 

    def SiPulsaEnter(self,event):
        self.etiqueta.SetLabel(self.entrada.GetValue() + "Pulso enter!")
        self.entrada.SetFocus()
        self.entrada.SetSelection(-1,-1) 

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'Mi aplicacion')
    app.MainLoop()