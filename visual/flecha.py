from visual import *





#pointer = arrow(pos=(0,2,1), axis=(5,0,0), shaftwidth=1)
ball = sphere(pos=(x,2,1), radius=0.5)
x= 0
ball.velocity= vector(25,0,0)

while x<10:
	rate(5)
	pointer = arrow(make_trail=False, pos=(x,0,0), axis=(5,0,0),  color=color.red)
	ball = sphere(pos=(x,2,1), radius=0.5)
	ball.velocity.x = -ball.velocity.x
	ball.pos = ball.pos+ball.velocity*0.05
	x=x+1
