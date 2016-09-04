#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Convierte temperaturas
# www.pythondiario.com

import sys
import serial
from PyQt4 import QtCore, QtGui, uic


###########################################################
# Declaro la variable global del  estatus del puerto
###########################################################
port=1
''' Hago la conección con Arduino desde GNU/linux'''
try:
    arduino = serial.Serial( '/dev/ttyACM0', 9600 )

except:
    portArduino="desconectado!"
    port=0
    print "Cannot conect to the port"
    

 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("led13.ui")[0]
 
class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.btn_onLed.clicked.connect(self.btn_onLed_clicked)
  self.btn_offLed.clicked.connect(self.btn_offLed_clicked)
    
  print port
  if port==0:
    self.cArduino.setText(str(portArduino))
    self.cArduino.setStyleSheet("background-color: red; color: black")
    print "Estatus del puerto", port
  else:
    self.cArduino.setText("Esta conectado")
    
 
 
 # Evento del boton btn_CtoF
 def btn_onLed_clicked(self):
   
  estado = "Encendido"
  print estado
  print "Paso",port
  if port == 1:
   arduino.write('U')
  #self.cArduino.setText(str(portArduino))
  
  

  self.estadoLed.setText(str(estado))
  self.btn_onLed.setStyleSheet("background-color: yellow; color: black")
  self.estadoLed.setStyleSheet("background-color: yellow; color: black")
  self.btn_offLed.setStyleSheet("background-color: #ff5722")
  
   
 
# Evento del boton btn_FtoC
 def btn_offLed_clicked(self):
  estado="Apagado"
  print estado
  if port==1:
    arduino.write('X')
  
  self.estadoLed.setText(str(estado)) 
  self.btn_onLed.setStyleSheet("background-color: #ff5722")
  self.btn_offLed.setStyleSheet("background-color: black; color: white")
  self.estadoLed.setStyleSheet("background-color: black; color: white")
  #self.editCel.setText(str(cel))
 
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()