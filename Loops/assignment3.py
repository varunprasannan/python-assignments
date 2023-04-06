# 3. Write a program using loops and closure to find the multipliers of
# 4 (4,8,12,16,....,40)? 

def calculate():
    num = 0
    def inner_func():
        nonlocal num
        num += 4
        return num
    return inner_func


multipliers = calculate()


for i in range(0, 10):
    print(multipliers())
