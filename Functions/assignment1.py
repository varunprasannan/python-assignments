# 1. Write a program to illustrate the use of default, keyword, optional and variable length args (*args and **kwargs)?

def default_args(a,b,c=10):
    sum = a+b+c
    return sum


def keyword_args(first_name, last_name):
    return "The name entered is {} {}".format(first_name, last_name)


def optional_args(a,b,c=10):
    return a+b+c


def variable_args(*numbers):
    total=0
    for i in numbers:
        total+=i


def variable_kwargs(**personal_details):
    return personal_details


print(default_args(1, 2, 3)) # here value of c is updated to 3 from default value of 10
print(default_args(1, 2)) # default value of c is 10
print(keyword_args(last_name="Prasannan", first_name="Varun")) # using keyword args we can interchange the position of the arguments
print(optional_args(1, 2)) # here c is the optional argument which by default is 10
print(variable_kwargs(Varun=21, rakesh=22, samiksha=23))























# def default_args(a, b, c=1, d=2):
#     print("a =", a)
#     print("b =", b)
#     print("c =", c)
#     print("d =", d)
#     print()

# def keyword_args(a, b, c, d):
#     print("a =", a)
#     print("b =", b)
#     print("c =", c)
#     print("d =", d)
#     print()

# def optional_args(a, b, c=1, d=2):
#     print("a =", a)
#     print("b =", b)
#     print("c =", c)
#     print("d =", d)
#     print()


# def variable_length_args(*args):
#     print("args =", args)
#     print("type(args) =", type(args))
#     print()

# def variable_length_kwargs(**kwargs):
#     print("kwargs =", kwargs)
#     print("type(kwargs) =", type(kwargs))
#     print()

# default_args(1, 2)


# keyword_args(a=1, b=2, c=3, d=4)

# optional_args(1, 2)

# variable_length_args(1, 2, 3, 4, 5)

# variable_length_kwargs(a=1, b=2, c=3, d=4)


