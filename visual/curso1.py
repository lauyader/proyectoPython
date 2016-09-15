#Primeros pasos con visual python

# Llamamos la libreria para llamar objetos 3D
from visual import *

#Mostramos los objetos 3D que entra en la escena
esfera = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
pared = box(pos=(6,0,0), size=(0.2,12,12), color=color.yellow)

vector2  = arrow(pos=(-5,0,0), axis=(-2,0,0), color=color.blue)

# Le asignamos velocidad a la esfera para que choque con la pared
esfera.velocity = vector(25,0,0)
arrow.velocity=esfera.velocity
# Le asignamos la escala del  tiempo 
escala = 0.005
# iniciamos el tiempo 
t = 0
vscale = 0.1
vector  = arrow(pos=(-5,0,0,), axis=(2,0,0), color=color.red)
scene.autoscale = False
while t < 2:
	rate(10)
	if esfera.pos.x > pared.pos.x:
		esfera.velocity.x = -esfera.velocity.x
		print ("posicion de la pared", pared.pos.x)
	 
		#vector.velocity.x = -vector.velocity.x


	esfera.pos = esfera.pos + esfera.velocity*escala
	
	vector.pos = vector.pos + vector.velocity*escala
	
	#vector  = arrow(pos=esfera.pos, axis=(2,0,0), shaftwidth=0, color=color.red)
	print ("posicion de la esfera", esfera.pos)
	t = t + escala

    
# Ejecutamos el programa para probar