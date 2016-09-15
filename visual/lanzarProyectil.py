# module name 2d_motion_angle_animation_graphs_sample2.py
# software development environment:
# Visual 5.0
# Python 2.6
# Windows XP Tablet PC Edition
# (HP EliteBook 2730P)
# edited using VIDLE
# programmer your-name-here
# last activity 23 oct 2009

# this program models two-dimensional motion with uniform acceleration
# this version includes animation and graphs
# note that the graphing takes time - so this simulation runs unevenly

# import some modules and functions needed for animation:
from visual import *
from visual.graph import *
import time

# equations of motion: ###################################
#   Vx = Vxo + Ax*t
#   Vy = Vyo + Ay*t
#   Sx = Sxo + Vxo * t + .5 * Ax * t**2
#   Sy = Syo + Vyo * t + .5 * Ay * t**2
##########################################################

# parameters to change for experimentation: ##############
Sxo = 0             # m = x coordinate of center of ball
Vo = 6.             # m/s
angle = 45.         # degrees
Axo =  0            # m/s**2
Syo = 1.            # m = y coordinate of center of ball
Ayo = -9.8          # m/s**2
ball_diam = 0.015   # m
delta_t = .01       # s
##########################################################

# convert degrees to radians for Python:
angle = angle * (pi/180.) # convert to radians
# use trigonometry to calculate Vxo, Vyo:
Vyo = Vo * sin(angle) 
Vxo = Vo * cos(angle)

# set up animation scene
#
# create scene object by instantiating display class:
# position, height, width are in pixels 
# ##############################################
scene_range=vector(4,4,4)    # change to get animation in scene display
# ##############################################
scene_center=vector(0.8*scene_range.x,0.2*scene_range.y,0)  
scene=display(
    title="animation with relative velocity vectors, ball not to scale, by your-name-here",
    x=0, y=0,
    width=800,height=300,
    autoscale=0,
    range=scene_range,
    center=scene_center)

# Put objects in animation scene:
# create ball object by instantiating sphere class:
# .pos property is given as a vector, i.e. x,y,z coordinates with respect to scene.center
# make animated ball a reasonable size so we can see it in the animation (experiment with ball.radius)
# (note that trajectory is plotted for ball center, so size of ball doesn't affect it)
ball = sphere(pos=(Sxo,Syo,0),radius=scene.range.x/50,color=color.green)
trail = curve()
# create ground object by instantiating box class: .pos coordinates are for its center
ground = box(pos=(scene_center.x,-ball.radius,0),size=(2*scene_center.x,2*ball.radius,0))

# create vectors to be represented by arrows:
############################################
# experiment to select animated vector scale factor and width appropriately
vector_scale=scene.range.y/50       # by trial & error
vector_width=ball.radius/2          # by trial & error
############################################
delta_t = .001                       # s, change to change time resolution
############################################

# initialize
Sx = Sxo
Vx = Vxo
Ax = Axo
Sy = Syo
Vy = Vyo
Ay = Ayo
t = 0

# scale the vector components of velocity, and the sum vector:
Vy_scaled=Vy*vector_scale
Vy_vector=vector(0,Vy_scaled,0)
Vx_scaled=Vx*vector_scale
Vx_vector=vector(Vx_scaled,0,0)
Vsum_vector=Vx_vector+Vx_vector         # add the vectors
# set up arrows to represent vector components of velocity, and the sum vector:
Vy_arrow=arrow(axis=Vy_vector,color=color.red,shaftwidth=vector_width)
Vy_arrow.fixedwidth=1
Vy_arrow.pos=ball.pos
Vx_arrow=arrow(axis=Vx_vector,color=color.blue,shaftwidth=vector_width)
Vx_arrow.fixedwidth=1
Vx_arrow.pos=ball.pos
Vsum_arrow=arrow(axis=Vsum_vector,color=color.green,shaftwidth=vector_width)
Vsum_arrow.fixedwidth=1
Vsum_arrow.pos=ball.pos

# set up graphs of position and velocity vs time
#
graphSx = gdisplay(x=0, y=300, width=400, height=300, 
             title='Graph: X position', xtitle='t(s)', ytitle='m',
             # experiment with xmax, ymax:        
             xmax=1.5, xmin=0, ymax=10, ymin=0,
             foreground=color.white,background=color.black)
plotSx = gcurve(gdisplay=graphSx,color=color.green)

graphSy = gdisplay(x=400, y=300, width=400, height=300, 
             title='Graph: Y position', xtitle='t(s)', ytitle='m',
             # experiment with xmax, ymax:        
             xmax=1.5, xmin=0, ymax=3.*Syo, ymin=0,
             foreground=color.white,background=color.black)
plotSy = gcurve(gdisplay=graphSy,color=color.green)

graphVx = gdisplay(x=0, y=600, width=400, height=300, 
             title='Graph: X velocity', xtitle='t(s)', ytitle='m/s',
             # experiment with ymax:        
             xmax=1.5, xmin=0., ymax=10, ymin=0,
             foreground=color.white,background=color.black)
plotVx = gcurve(gdisplay=graphVx,color=color.red)

graphVy = gdisplay(x=400, y=600, width=400, height=300, 
             title='Graph: Y velocity', xtitle='t(s)', ytitle='m/s',
             # experiment with ymax, ymin:        
             xmax=1.5, xmin=0., ymax=Vyo, ymin=-3.*Vyo,
             foreground=color.white,background=color.black)
plotVy = gcurve(gdisplay=graphVy,color=color.red)

# run algorithm:
##time.sleep(5)   # allow some time to slide windows apart (only needed in Linux: VPython bug here...)
while Sy - ball_diam/2. > 0 :   # repeat until ball hits floor
    rate(1/(10.*delta_t))    # prevent simulation from running too fast
    
    # calculate velocities from equations of motion:    
    Vx = Vxo + Ax*t
    Vy = Vyo + Ay*t

    # print, animate, and plot before incrementing time
    # (we do this so as to include datapoint when t=0):
    print "t=%g s: Sx=%g m, Vx=%g m/s, Sy=%g m, Vy=%g m/s" % (t,Sx,Vx,Sy,Vy)
    ball.pos=(Sx,Sy,0)
    trail.append(ball.pos)

    Vx_vector.x=Vx*vector_scale     # (doesn't change)
    Vy_vector.y=Vy*vector_scale
    Vsum_vector=Vx_vector+Vy_vector
    Vy_arrow.axis=Vy_vector
    Vy_arrow.pos=ball.pos
    Vx_arrow.pos=ball.pos
    Vsum_arrow.axis=Vsum_vector
    Vsum_arrow.pos=ball.pos   

    plotSx.plot(pos=(t,Sx))
    plotSy.plot(pos=(t,Sy))
    plotVx.plot(pos=(t,Vx))
    plotVy.plot(pos=(t,Vy))
    
    # increment the time:
    t = t + delta_t

    # calculate new position from equations of motion:
    Sx = Sxo + Vxo * t + .5 * Ax * t**2
    Sy = Syo + Vyo * t + .5 * Ay * t**2


