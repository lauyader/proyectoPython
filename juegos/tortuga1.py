import turtle

turtle.shape("turtle")

turtle.forward(25)

def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)

line_without_moving()
turtle.right(90)
line_without_moving()
turtle.right(90)
line_without_moving()
turtle.right(90)
line_without_moving()


turtle.exitonclick()
