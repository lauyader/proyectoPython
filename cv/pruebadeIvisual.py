from ivisual import *

print """
Click left mouse button in 3D window background to add small sphere.
"""
scene = canvas(title="mouse click")
scene.range = 3

box = box() # display a box for contexts

def showSphere(evt):
    loc = evt.pos
    sphere(pos=loc, radius = 0.05, color=color.cyan)

scene.bind('click', showSphere)