import helloWorld

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + "." + last_name + "@afourtech.com"

    # Actual representation of the Object for the User
    def __repr__(self):
        return "<Employee('{}', '{}', '{}')>".format(self.first_name, self.last_name, self.salary)

    # Simple representation of the Object for the User
    def __str__(self):
        return "The Employee's name is {} {} and has a salary of {}".format(self.first_name, self.last_name, self.salary)
    
    # Used to define the various attributes that can be used for the local class
    def __dir__(self):
        return ['salary', 'first_name', 'last_name']


def main():
    # invoking the imported module's function
    helloWorld.hello()
    print(helloWorld.__file__)

    # creating an object of the class created
    employee1 = Employee('Varun','Prasannan', 30000)
    print(employee1.__repr__())
    print(employee1.__str__()) 
    print(employee1.__dir__()) # by default returns an unsorted list
    print(dir(employee1)) # returns a sorted list


if __name__ == "__main__":
    main()