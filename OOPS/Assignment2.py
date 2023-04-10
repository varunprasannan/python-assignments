# 2. Define a class named American and its subclass NewYorker.
# Hints: Use class Subclass(ParentClass) to define a subclass

class American:
    def __init__(self):
        self.name = "American"
    
    def print_name(self):
        print(self.name)

    def display(self):
        print("I am an American")


class NewYorker(American):
    def __init__(self):
        self.name = "New Yorker"
    
    def print_name(self):
        print(self.name)
    
    def display(self):
        print("I am a New Yorker")

    
american = American() 
american.print_name()
american.display()

new_yorker = NewYorker()
new_yorker.print_name()
new_yorker.display()

# Output:

# American
# I am an American
# New Yorker
# I am a New Yorker