import turtle

def square10():
  for i in range(10, 110, 10):
    turtle.shape('turtle')
    turtle.pendown()
    turtle.forward(10 + i)
    turtle.left(90)  
    turtle.forward(10 + i)
    turtle.left(90)  
    turtle.forward(10 + i)
    turtle.left(90)  
    turtle.forward(10 + i)
    turtle.left(90)  
    turtle.penup()
    turtle.goto(-i/2, -i/2)