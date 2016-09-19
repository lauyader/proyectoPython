#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
###################################
# Sistema para simular un sensor de ultrasonido de arduino en tiempo real
###################################
###################################
# Diseñado y programado por: Luis Americo Auyadermont Muñoz
###################################

from visual import *
import sys
import serial
import time




''' Hago la conección con Arduino desde GNU/linux'''
try:
    arduino = serial.Serial( '/dev/ttyACM0', 9600 )

except:
    portArduino="desconectado!"
    port=0
    print "No pudo conectarse con la placa arduino, revisa el puerto o la conexión"

 

datos=1 
 
 

#objeto= sphere(pos=(-7,2,dist), radius=2.5, color=color.black)
###################################
# Declaración de la escena
###################################
scene = display(title='Ultra Sonido',x=0, y=0, width=640, height=480,center=(0,0,0), background=(0.2,0.3,1))


###################################
# Grupo de los objetos que forman al  ultrasonido
###################################
ultrasonido=frame()
placa = box( frame=ultrasonido,pos=(-7,2,2), axis=(0,0,55), length=1, height=10, width=20, color=color.green)
cilindro = cylinder(frame=ultrasonido, pos=(-3,2,2), length=2, axis=(0,0,1), radius=3,color=color.red)
cilindro2 = cylinder(frame=ultrasonido, pos=(-12,2,2), length=2, axis=(0,0,1), radius=3,color=color.red) 
objeto= sphere(make_trail = False, pos=(-7,2, 0), radius=1, color=color.black)

###################################
# Mostrar un texto en 3d  
###################################
text(text='Ultra Sonido', pos=(-4,8,2),align='center', depth=-0.3, color=color.green)

###################################
# Captura los datos de arduino emitido por el sensor
###################################
datos=arduino.readline()
 


###################################
# Detección del obstaculo
###################################

while True:
	###################################
	# Definimos el tiempo de captura de datos 
	###################################
	rate(50)
	datos=arduino.readline()
    ###################################
    # Definimos la posición del objeto que simula el obstaculo 
    ###################################  
	objeto.pos.z = int(datos)
	print datos

###################################
# Hay que resolver que la imagen deja rastro. 
###################################	