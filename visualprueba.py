from visual import *

ball = sphere(pos=(-5,0,0 ), radius=0.5, color=color.red)
caja = box(pos=(6,0,0), size=(0.2, 12, 12), color=color.blue)
vscale = 0.1
ball.velocity = vector(25,5,0)
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.yellow)
ball.trail = curve(color=ball.color)


tiempo=0.005
t=0

while t<3:
    rate(50)
    if ball.pos.x > caja.pos.x:
        ball.velocity.x = -ball.velocity*tiempo
        
    ball.pos = ball.pos + ball.velocity*tiempo
    ball.trail.append(pos=ball.pos)
        
    t= t+ tiempo
