import turtle

def draw_square():
     

     for i in range(1,5):
          Pointer.forward(100)
          Pointer.right(90)

def draw_circle():

     i = 0
     while(i<=360):
          draw_square()
          i = i + 10
          Pointer.right(10)
          
window = turtle.Screen()
Pointer = turtle.Turtle()
Pointer.color("black")
draw_circle()
