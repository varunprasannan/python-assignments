from services.sorting.sorts import merge_sort
from services.math.mod1 import square


def squared_sorted(arr):
    for i in range(len(arr)):
        arr[i] = square(arr[i])
    return "The squared sorted list is:", merge_sort(arr)
