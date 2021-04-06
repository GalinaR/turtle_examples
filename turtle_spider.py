import turtle

def spider():
  for step in range(12):
    turtle.right(30)
    turtle.forward(150)
    turtle.stamp()
    turtle.backward(150)

turtle.shape('turtle')
turtle.width(2)
turtle.speed(2)
