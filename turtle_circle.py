import turtle

def circle():
  for step in range(360):
    turtle.forward(1)
    turtle.left(1)

turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('black')
turtle.speed(50)
