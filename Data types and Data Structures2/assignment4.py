# 4. Create a generator expression to find the sum of cube of first 20
# elements?

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sum_of_cubes = sum(num**3 for num in elements)
print(sum_of_cubes)
