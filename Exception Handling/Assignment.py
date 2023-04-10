# Write a program that illustrates the use of 
# TypeError, ValueError, AttributeError, ZeroDivisionError, IndexError
import math

try:
    print(5 + '5')
except TypeError as te:
    print(te)
finally:
    print("Program continues\n")

try:
    print(math.sqrt(-20))
except ValueError as ve:
    print("The number given is negative", ve)
finally:
    print("Program continues\n")

try:
    number = 20
    print("I am {} years old".fmt(number))
except AttributeError as ae:
    print(ae)
finally:
    print("Program continues\n")

try:
    print(0/0)
except ZeroDivisionError as ze:
    print(ze)
finally:
    print("Program continues\n")

try:
    list1 = [1, 2, 4]
    print(list1[5])
except IndexError as ie:
    print(ie)
finally:
    print("Program continues\n")

# Output: 
# unsupported operand type(s) for +: 'int' and 'str'
# Program continues

# The number given is negative math domain error
# Program continues

# 'str' object has no attribute 'fmt'
# Program continues

# division by zero
# Program continues

# list index out of range
# Program continues