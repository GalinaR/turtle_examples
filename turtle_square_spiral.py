import turtle

def square_spiral():
  for i in range(10, 210, 20):
    turtle.shape('turtle')
    turtle.forward(0 + i)
    turtle.left(90)  
    turtle.forward(5 + i)
    turtle.left(90)  
    turtle.forward(10 + i)
    turtle.left(90)  
    turtle.forward(15 + i)
    turtle.left(90)  