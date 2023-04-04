# 2. Write a function that will take one list as input and return three
# different types of list as illustrated in the output. In object2, you can
# append a list containing triplet of a number but object 3 should be
# evaluated based on the elements present in the object2 (Note:You
# have to take care of both the space and time complexities as well)
# Input: object1 = [[1,1,1],[2,2,2],[3,3,3]]
# Output:
# object1 = [[1,1,1],[2,2,2],[3,3,3]]
# object2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
# object3 = [[1,1,1],[2,4,2],[3,9,3],[4,16,4]]

def squared_triplet(object1, num):
    print("object1 = {}".format(object1))

    object1.append([num for i in range(0, 3)])
    print("object2 = {}".format(object1))

    # object1 = [[object1[i][j], object1[i][j]**2, object1[i][j]]
    # for i in range(4) for j in range(3)]
    object1 = [[lists[0], lists[1]**2, lists[2]] for lists in object1]
    print("object3 = {}".format(object1))


squared_triplet([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 4)
