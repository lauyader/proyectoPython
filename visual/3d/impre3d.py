#!/usr/bin/python2.7
# -*- coding: utf-8 -*-.
from visual import *


###################################
# Cosntrucción de un Simulador de impresion 3d para arduino
# Autor: Luis Americo Auyadermont Muñoz
# Version:0.02
###################################


Escena= display(title='Impresion 3d',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1))

#n1 = sphere(pos=(1,0,1), radius=5, color = color.green)

###################################
# Construcción del riel de la impresora horizontal
###################################

 
suelo= box(pos=(0,-3,0), lenght=0,width=80, height=80, axis=(0,1,0),color=color.black)

soporteizq=box(pos=(-30,5,0), lenght=5,width=5, height=5, axis=(0,15,0),color=color.green) # axis(0,altura Y,0)
soporteder=box(pos=(30,5,0), lenght=5,width=5, height=5, axis=(0,15,0),color=color.green)

rielHorizontal = cylinder(pos=(-30,5,0), length=60, axis=(5,0,0), radius=1,color=color.red)


###################################
# Construcción del riel de la impresora vertical
###################################

soporteSup=box(pos=(-30,5,-32), lenght=5,width=5, height=5, axis=(0,15,0),color=color.orange) # axis(0,altura Y,0)
soporteInf=box(pos=(-30,5,32), lenght=5,width=5, height=5, axis=(0,15,0),color=color.orange)

rielVertical = cylinder(pos=(-30,5,-30), length=60, axis=(0,0,5), radius=1,color=color.red)

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
	posRiel=-25

	while posRiel < 26:
		rate(10)
		
		cabezal.pos.x=posRiel+0.2

		posRiel= posRiel+ 1
		soporteizq.pos.z= posRiel+0.2
		soporteder.pos.z= posRiel+.02
		rielHorizontal.pos.z= posRiel+0.2
		cabezal.pos.z=posRiel+0.2


def cabDer_Izq():
	posRiel=25	
	while posRiel>-26:
		rate(10)
		print posRiel
		cabezal.pos.x=posRiel-.2
		posRiel = posRiel -1
		soporteizq.pos.z= posRiel+0.2
		soporteder.pos.z= posRiel+.02
		rielHorizontal.pos.z= posRiel+0.2
		cabezal.pos.z=posRiel+0.2



cabIzq_Der()
cabDer_Izq()

cabIzq_Der()
cabDer_Izq()

cabIzq_Der()
cabDer_Izq()
