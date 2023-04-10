# 3. Write a program to illustrate Append, Delete and Display
# Elements of a List using classes. 

class functions:
    def __init__(self):
        self.list = []
    
    def append(self):
        self.list.append(input("Enter a number to append: "))
    
    def delete(self):
        self.list.remove(input("Enter a number to delete: "))
    
    def display(self):
        print(self.list)


example = functions()
example.append()
example.append()
example.append()
example.display()
example.delete()
example.display()

# Output:
# Enter a number to append: 5
# Enter a number to append: 8
# Enter a number to append: 100
# ['5', '8', '100']
# Enter a number to delete: 100
# ['5', '8']