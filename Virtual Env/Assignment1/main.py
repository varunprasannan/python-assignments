from services.math.mod1 import square_root, cube_root, fibonacci
from services.sorting.sorts import merge_sort, binary_sort
from services.sorting.merge_and_sort import merge_list
from services.sorting.square_sorted import squared_sorted

print("---------TASK A------------")
print(square_root(9))
print(cube_root(8))
print(fibonacci(10), "\n")

print("---------TASK B------------")
print(merge_sort([7, 9, 12, 44, 66, 22, 12, 6]))
print(binary_sort([7, 9, 12, 44, 66, 22, 12, 6]))
print(merge_list([23, 5, 66, 12, 2, 13, 6],[11, 89, 22, 3, 54, 65, 77]))

print(squared_sorted([7, 9, 12, 44, 66, 22, 12, 6]))

#Output:

# (venv) PS C:\Users\Varun.P\PycharmProjects\Assignment2> python main.py
# ---------TASK A------------
# 3.0
# 2.0
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# ---------TASK B------------
# [6, 7, 9, 12, 12, 22, 44, 66]
# [6, 7, 9, 12, 12, 22, 44, 66]
# [2, 3, 5, 6, 11, 12, 13, 22, 23, 54, 65, 66, 77, 89]
# ('The squared sorted list is:', [36, 49, 81, 144, 144, 484, 1936, 4356])
# (venv) PS C:\Users\Varun.P\PycharmProjects\Assignment2>



