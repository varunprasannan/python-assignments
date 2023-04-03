# 1. Write any python program that makes use of variables,
# constants, operators, atleast 5 keywords and print statements of
# different forms ?

def area_of_circle(radius):
    # creating conditional statements
    if radius < 0:
        print("Radius cannot be negative")
        return
    elif radius == 0:
        print("Area of circle with radius 0 is 0")
        return
    else:
        print("Calculating area of circle with radius", radius)
    PI = 3.14  # a constant
    area = PI * radius**2  # use of multiplication and exponentiation operators
    print("Area of circle with radius", radius, "is", area)
    # use of keywords such as return, def, if, else, elif, print


area_of_circle(5)

# defining variables
first_name = "Varun"
last_name = "Prasannan"

# use of print statements
print("Hello, my name is", first_name, last_name)  # use of print statement
print("Hello, my name is " + first_name + " " + last_name)
print("Hello, my name is %s %s" % (first_name, last_name))
print("Hello, my name is {} {}".format(first_name, last_name))
