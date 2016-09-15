#vector.py
from visual import *
import math

def make_grid(unit, n):
    nunit = unit * n
    f = frame()
    for i in xrange(n+1):
        if i%5==0: 
            color = (1,1,1)
        else:
            color = (0.5, 0.5, 0.5)

        curve(pos=[(0,i*unit,0), (nunit, i*unit, 0)],color=color,frame=f)
        curve(pos=[(i*unit,0,0), (i*unit, nunit, 0)],color=color,frame=f)
    return f

arrow(pos=(0,0,0), axis=(5,0,0), color=(1,0,0), shaftwidth=0.1)    
arrow(pos=(0,0,0), axis=(0,5,0), color=(0,1,0), shaftwidth=0.1)    
arrow(pos=(0,0,0), axis=(0,0,5), color=(0,0,1), shaftwidth=0.1)    
grid_xy = make_grid(0.5, 10)
grid_xz = make_grid(0.5, 10)
grid_xz.rotate(angle=pi/2, axis=(1,0,0), origin=(0,0,0))
grid_yz = make_grid(0.5, 10)
grid_yz.rotate(angle=-pi/2, axis=(0,1,0), origin=(0,0,0))
sphere(radius=0.3)

obj = arrow(pos=(0,0,0), axis=(1,2,3), shaftwidth=0.3)
th = 0
while True:
    rate(20)
    obj.axis = (3*math.cos(th), 3*math.sin(th), 2)
    th += 0.04