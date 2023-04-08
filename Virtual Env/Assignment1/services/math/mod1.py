# a. Functions to return the square root and cube root
def square_root(x):
    return x ** 0.5


def cube_root(x):
    return x ** (1/3)


# b. Function to return the fibonacci series
def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib


def square(x):
    return x**2
