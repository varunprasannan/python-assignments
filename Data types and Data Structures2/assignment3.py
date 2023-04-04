# 3. Create a List comprehension to get the files with .txt


import os
path = "C:\\Users\Varun.P\TEST"

# Using normal procedure
# file_list = []
# for files in os.listdir(path):
#     if files.endswith('.txt'):
#         file_list.append(files)
# print(file_list)

# using list comprehensions
files_list = [files for files in os.listdir(path) if files.endswith(".txt")]
print(files_list)
