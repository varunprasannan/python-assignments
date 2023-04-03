# 2. Write a program to demonstarte use of unpacking variables in
# Python using all available synatx (like single *, ** etc)

def add_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    print("Sum of numbers is", sum, "\n")


def display_info(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))
    print("\n")


def print_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


add_numbers(1, 2, 3, 4, 5)
display_info(first_name="Varun", last_name="Sharma", age=22, Phone=1234567890)
print_args_kwargs(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5, f="Varun")
