# a. Implement binary sort
def binary_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key
    return arr


# b. Implement merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
