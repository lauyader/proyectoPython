#!/usr/bin/python
# -*- coding: utf-8 -*- 
''' Aplicación para Encender un led con python y Arduino'''
'''Realmente es sencillo programar con python, y  su interfaz Tkinter'''

import serial
import Tkinter as tk
from Tkinter import *

''' Hago la conección con Arduino desde GNU/linux'''
try:
    arduino = serial.Serial( '/dev/ttyACM1', 9600 )
except:
    print "Cannot conect to the port"

''' Función que recibe las opciones desde un boton y reenvia al arduino '''

def LED1():
    arduino.write('U')
    print "Se encendio el led 13"

def ApagarLED1():
    arduino.write('X')
    print "Se Apaga el led 13"


''' definimos la interfaz gráfica para Tkinter'''
root = Tk()

button1 = Button(root, text="Encender LED 13", command=LED1)
button1.grid(row=1, column=1)
button2 = Button(root, text="Apagar el LED 13", command=ApagarLED1)
button2.grid(row=1, column=2)

''' Marco de la Ventana '''

root.title('GUI de Leds')
root.geometry("320x70")
root.mainloop()
