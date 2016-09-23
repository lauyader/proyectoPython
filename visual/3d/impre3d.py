#!/usr/bin/python2.7
# -*- coding: utf-8 -*-.
from visual import *


###################################
# Simulador de impresion 2d con arduino
# Autor: Luis Americo Auyadermont
###################################


Escena= display(title='Impresion 3d',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1))

#n1 = sphere(pos=(1,0,1), radius=5, color = color.green)

###################################
# Construcción del riel de la impresora
###################################

 
suelo= box(pos=(0,-3,0), lenght=0,width=60, height=80, axis=(0,1,0),color=color.orange)

soporteizq=box(pos=(-30,5,0), lenght=5,width=5, height=5, axis=(0,15,0),color=color.green) # axis(0,altura Y,0)
soporteder=box(pos=(30,5,0), lenght=5,width=5, height=5, axis=(0,15,0),color=color.green)

cilindro = cylinder(pos=(-30,5,0), length=60, axis=(5,0,0), radius=1,color=color.red)

###################################
# Cabezal
###################################


cabezal= pyramid(pos=(-25,5,0), size=(8,3,2), axis=(0,-10,0), color=color.blue) #size(altura,0,0)

###################################
# Definir las funciones que harán  
# la animación del cabezal de izquierda a derecha 
# derecha a izquierda.
###################################

def cabIzq_Der():	
	riel=-25

	while riel < 26:
		rate(10)
		
		cabezal.pos.x=riel+0.2

		riel= riel+ 1
		print riel

def cabDer_Izq():
	riel=25	
	while riel>-26:
		rate(10)
		print riel
		cabezal.pos.x=riel-.2
		riel = riel -1



cabIzq_Der()
cabDer_Izq()

cabIzq_Der()
cabDer_Izq()

cabIzq_Der()
cabDer_Izq()
