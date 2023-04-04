# 5. Create a Dictionary comprehension to get the length of each
# word in the list?

input_string = "Youre braver than you believe, and stronger than you seem, and smarter than you think"
list_of_words = input_string.split()  #converts the string into a list :)

dict_of_words = {word:len(word) for word in list_of_words}
print(dict_of_words)
