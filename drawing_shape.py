import turtle
def draw_square():
     window = turtle.Screen()
     window.bgcolor("red")
     
     Pointer = turtle.Turtle()
     Pointer.width(10)
     Pointer.shape("square")     
     Pointer.color("black", "blue")
     Pointer.begin_fill()
     
     i = 0
     while(i < 4):
          Pointer.forward(100)
          Pointer.right(90)
          i = i + 1

     Pointer.end_fill()     
 
def draw_circle():

     Pointer2 = turtle.Turtle()
     Pointer2.shape("circle")
     Pointer2.color("white")
     Pointer2.circle(80)

def draw_triangle():

     Pointer3 = turtle.Turtle()
     Pointer3.shape("triangle")
     Pointer3.color("black", "pink")
     Pointer3.begin_fill()
     Pointer3.backward(120)
     Pointer3.left(90)
     Pointer3.backward(90)
     Pointer3.right(53)
     Pointer3.forward(150)
     Pointer3.right(37)
     Pointer3.end_fill()
     
draw_square()
draw_circle()
draw_triangle()
