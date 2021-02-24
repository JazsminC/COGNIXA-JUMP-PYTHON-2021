def weird_arthimetic(x, y, z): # function definition line
    print((x**x + y**z) // z)  # code block


weird_arthimetic(5, 6, 7) #function call with passed parameters

#function using strings
def Greeting(greet, name):
    print(greet, name + "!")

Greeting("Hello", "Jazsmin")

# Another way to use functions
#def weird_arthimetic(x, y, z): # function definition line
#    output = (x**x + y**z) // z)  # code block
 #   return output

#some_number = weird_arthimetic(5, 6, 7)

#print("some_number:", some_number)


def area_of_circle(r):
    c_area = (3.14 * r**2)
    return c_area

area_of_circle(4)  # gives the radius the value of 4

def vol_of_cylinder(h):
    volume = area_of_circle(4) * h
    print("The area of a circle is", area_of_circle(4))
    print("The volume of the cylinder is", volume)
    return volume

vol_of_cylinder(10)    # Give the height the value of 10