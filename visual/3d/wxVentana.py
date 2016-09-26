#!/usr/bin/python
# -*#- coding: utf-8 -*-


import wx
from visual import *

Escena= display(title='Impresion 3d',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1)) 
sphere(pos=(0,0,0), radius=0.2, color=color.cyan)   

class Example(wx.Frame):
    #Escena= display(title='Impresion 3d',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1)) 
    #sphere(pos=(0,0,0), radius=0.2, color=color.cyan)
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):

        pnl = wx.Panel(self)
        exitButton = wx.Button(pnl, wx.ID_ANY, 'Salir', (10, 10))
        pararButton = wx.Button(pnl, wx.ID_ANY, 'Parar', (10, 50))
        avanzarButton = wx.Button(pnl, wx.ID_ANY, 'Avanzar', (100, 50))

        self.Bind(wx.EVT_BUTTON,  self.OnExit, id=exitButton.GetId())
        self.Bind(wx.EVT_BUTTON,  self.caja, id=avanzarButton.GetId())

        self.SetTitle("Automatic id")
        self.Centre()
        self.Show(True)

    def OnExit(self, event):

        self.Close()

    def caja(self, event):
            #Escena= display(title='Control 3D',x=0, y=0, width=600, height=500,center=(0,0,0), background=(0.2,0.3,1)) 
            sphere(pos=(0,0,0), radius=1.2, color=color.cyan)   

def main():


    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  