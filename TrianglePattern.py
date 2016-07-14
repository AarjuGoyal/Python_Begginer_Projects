import turtle

def draw_triangle(side):
     Pointer.begin_fill()
     
     Pointer.left(60)
     Pointer.forward(side)
     Pointer.right(60)
     Pointer.backward(side)
     Pointer.right(60)
     Pointer.forward(side)
     Pointer.left(60)

     Pointer.end_fill()

def draw_set_triangle(SideOfBiggest, ToDrawSmaller):
     
     Pointer.forward(SideOfBiggest/2)
     if(ToDrawSmaller):
          draw_set_triangle(SideOfBiggest/2, False)
     else:
          draw_triangle(SideOfBiggest/2)
 #    draw_triangle(SideOfBiggest/2)
     Pointer.backward(SideOfBiggest/2)
     draw_triangle(SideOfBiggest)
     print "2nd triangle drawn"
     Pointer.backward(SideOfBiggest/2) #error somehow solved
     if(ToDrawSmaller):
          draw_set_triangle(SideOfBiggest/2, False)
     else:
          draw_triangle(SideOfBiggest/2)
 #    draw_triangle(SideOfBiggest/2)
     Pointer.penup()
     Pointer.forward(SideOfBiggest/2) #till here the turtle is at the foot of bigger triangle
     Pointer.left(120)
     Pointer.forward(SideOfBiggest) #Pointer at the upper left corner of the bigger triangle
     Pointer.right(120)
     Pointer.forward(SideOfBiggest/2)
     
     Pointer.pendown()
     if(ToDrawSmaller):
          draw_set_triangle(SideOfBiggest/2, False)
     else:
          draw_triangle(SideOfBiggest/2)
 #    draw_triangle(SideOfBiggest/2)

     #till now all triangles are drawn
     #Now to bring the cursor to original position
     Pointer.penup()
     Pointer.forward(SideOfBiggest/2)
     Pointer.right(120)
     Pointer.forward(SideOfBiggest)
     Pointer.left(120)
     Pointer.pendown()
     
     

Pointer = turtle.Turtle()
Pointer.color("black", "green")
y = 200
#Pointer.speed(1)
Pointer.begin_fill()
#Pointer.backward(y/2)
Pointer.forward(y/2)
Pointer.left(120)
Pointer.forward(y)
Pointer.left(120)
Pointer.forward(y)
Pointer.left(120)
Pointer.forward(y/2)
Pointer.end_fill()
Pointer.color("black", "white")
draw_set_triangle(y/2, True)     
     
