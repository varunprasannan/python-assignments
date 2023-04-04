# 1. Write a program to create a list of tuples from given list having
# number and its square in each tuple? Also, convert the list of tuples
# to a dictionary. (Using Comprehension)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_of_squares = [(num, num**2) for num in numbers]
dict_of_squares = dict(tuple_of_squares)
print(dict_of_squares)
