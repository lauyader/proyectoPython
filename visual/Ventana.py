#Ventana.py

from visual import *

w = window(menus=False, title="VPython", x=0, y=0, width=600, height=600)
display(window=w, x=50, y=30, width=200, height=150) 


from visual.controls import *
 
def change(): # Called by controls when button clicked
    if b.text == 'Click me':
        b.text = 'Try again'
    else:
        b.text = 'Click me'
 
c = controls() # Create controls window
# Create a button in the controls window:
#b = button( pos=(0,0), width=60, height=60,text='Click me', action=lambda: change() ) 
d =toggle ( pos=(0,20), width=60, height=60,text='Click me', action=lambda: change() ) 

scene2 = display(title='Objetos',x=0, y=0, width=600, height=500,center=(5,0,0), background=(0.2,0.3,1))
n1 = sphere(pos=(1,0,1), radius=5, color = color.green)
suelo= box(pos=(-5,-10,0), lenght=10,width=60, height=50, axis=(0,1,0.2),color=color.orange)

grupo=frame()
cilindro = cylinder(frame=grupo, pos=(3,3,2), length=10, axis=(0,1,1), radius=3,color=color.red)
mybox = box(frame=grupo, pos=(3,3,2), length=5, height=25) 



#cilindro.rotate(angle=180, axis=(1,1,0))
sapo1=sphere(frame=grupo, pos=(5,-1,0),radius=1.5, color=color.green)
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

