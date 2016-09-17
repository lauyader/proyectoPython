#Animar varios objetos y enlazarlos.py

from visual import *


###################################
# Muestro los objetos que estaran en la ventana
###################################

Escenario1 = display(title='Objetos',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1))
n1 = sphere(pos=(1,0,1), radius=5, color = color.green)
suelo= box(pos=(-5,-10,0), lenght=10,width=60, height=50, axis=(0,1,0.2),color=color.orange)


###########################
# Asigno el nombre al grupo de objeto declarandolo como frame()
###########################
grupo=frame()
cilindro = cylinder(frame=grupo, pos=(3,3,2), length=10, axis=(0,1,1), radius=3,color=color.red)
mybox = box(frame=grupo, pos=(3,3,2), length=5, height=25) 
#cilindro.rotate(angle=180, axis=(1,1,0))
sapo1=sphere(frame=grupo, pos=(5,-1,0),radius=1.5, color=color.green)

###########################
# fin  al grupo de objeto declarandolo como frame()
###########################

while 1:
    rate(10)
    for i in range(30):
        #n1.pos.x +=i/200.0
        #suelo.pos.y -=i/200.0
        #cilindro.pos.z +=i/300.0
        n1.rotate(angle=i, axis=(1,1,0))
        sapo1.rotate(angle=i, axis=(1,1,0))
        cilindro.rotate(angle=i, axis=(1,1,0))
        mybox.rotate(angle=i, axis=(1,1,0))

