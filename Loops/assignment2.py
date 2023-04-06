# 2. Create an iterator that returns numbers, starting with 1, and each
# sequence will increase by one (returning 1,2,3,4,5...) and raise
# StopIteration exception when the number is greater than 10 ?

i = 0
while i > =0:
    if i > 10:
        raise(StopIteration)
    print(i)
    i += 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Traceback (most recent call last):
#   File "c:\Users\Varun.P\Assignments\Loops\assignment2.py", line 8, in <module>
#     raise(StopIteration)
# StopIteration