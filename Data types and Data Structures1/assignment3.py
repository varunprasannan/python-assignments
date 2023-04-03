# 3. Write a program to find the maximum number from 3 given
# numbers using normal function and then using ternary operator.

def normal_function(a, b, c):
    return max(a, b, c)


def ternary_operator(a, b, c):
    return a if (a > b and a > c) else (b if b > c else c)


print(normal_function(1, 2, 3))
print(ternary_operator(4, 5, 6))
