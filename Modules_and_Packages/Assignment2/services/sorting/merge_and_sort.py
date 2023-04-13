from services.sorting.sorts import merge_sort

def merge_list(list1, list2):
    list1.extend(list2)
    return merge_sort(list1)