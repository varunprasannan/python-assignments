# 1. Define a class which has at least two methods:
#  get_string: to get a string from console input
#  print_string: to print the string in upper case

class Methods:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())


example = Methods()
example.get_string()
example.print_string()

# Output:

# Enter a string: Hi my name is Varun Prasannan
# HI MY NAME IS VARUN PRASANNAN
