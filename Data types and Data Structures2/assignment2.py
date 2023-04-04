# 2. Create a Set comprehension to get the unique words in the string

input_string = "You're braver than you believe, and stronger than you seem, and smarter than you think"

new_set = {word for word in input_string.split()}
print(new_set)
