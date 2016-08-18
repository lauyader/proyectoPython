
from turtle import *

setup(640, 480, 0, 0)

title("Ejemplo de ventana con Turtle")
n=1
def cuadrado():
    shape("turtle")
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)


def circulo():
    shape("turtle")
    circle(50,360)

def flor():
    n=1
    while n<=3:
        pencolor("red")
        cuadrado()
        fillcolor("red")
        begin_fill()
        pencolor("green")
        circulo()

        pencolor("red")
        cuadrado()
        fillcolor("blue")
        begin_fill()
        pencolor("blue")
        circulo()
        cuadrado()
        n=n+1




flor()
exitonclick()