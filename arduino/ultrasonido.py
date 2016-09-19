#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
###################################
# Sistema para simular un sensor de ultrasonido de arduino
###################################
###################################
# Diseañado por: Luis Americo Auyadermont
###################################

from visual import *

#w = window(menus=False, title="VPython", x=0, y=0, width=600, height=600)
#display(window=w, x=50, y=30, width=640, height=480)


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

###################################
# Mostrar el objeto cuando el sensor lo encuentre
###################################
objeto= sphere(pos=(-7,2,32), radius=2.5, color=color.black)
text(text='Ultra Sonido', pos=(-4,8,2),align='center', depth=-0.3, color=color.green)

