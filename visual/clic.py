from visual import *
scene.range = 4
box() # display a box for context

def showSphere(evt):
    loc = evt.pos
    sphere(pos=loc, radius=0.2, color=color.cyan)

scene.bind('click', showSphere)