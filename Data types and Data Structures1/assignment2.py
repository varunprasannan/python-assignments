# 2. Program to create a copy of an object1 to object2 and append
# new element to object2
# Input:
# object1 = [[1,1,1],[2,2,2],[3,3,3]]
# Output:
# object1 = [[1,1,1],[2,2,2],[3,3,3]]
# object2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

object1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
object2 = object1.copy()
object2.append([4, 4, 4])
print(object1)
print(object2)
