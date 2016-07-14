"""A program about basics of Inheritance and Classes"""
class Parent():
     def __init__(self, last_name_parent, eye_colour_parent):
          print "Parent constructor called"
          self.last_name = last_name_parent
          self.eye_colour = eye_colour_parent

     def print_info(self):
          print( "Last Name " + self.last_name)
          print("Eye Colour " + self.eye_colour)

class Child(Parent):
     def __init__(self, last_name_parent, eye_colour_parent, number_of_toys_child):
          print "child constructor called"
          Parent.__init__(self, last_name_parent, eye_colour_parent)
          self.number_of_toys = number_of_toys_child 

     def print_info(self):
          print( "Last Name " + self.last_name)
          print( "Eye colour " + self.eye_colour)
          print( "Number Of toys " + str(self.number_of_toys) )


billy_cyrus = Parent("cyrus", "blue")

billy_cyrus.print_info()


miley_cyrus = Child("cyrus", "blue", 5)

miley_cyrus.print_info()

