class Dept:
    def __init__(self, name):  # Constructor, this code executes when we make a new Store
        self.name = name  # has-a' relationship

    def __str__(self):
        return f'Dept: {self.name}'

    def __repr__(self):
        return f'Dept({repr(self.name)})'


class Store:
    def __init__(self, name, depts):  # Constructor, this code executes when we make a new Store
        self.name = name
        self.name = depts

    def __str__(self):
        # this is what gets called to print out the name of the object as a string, return any string and that's what will get printed when we print out the object
        return f'Store: {self.name}'

    def __repr__(self):
        return f'Store({repr(self.name)})'


depts = [
    Dept("Department 1"),
    Dept("Department 2"),
    Dept("Department 3")
]

# my_store = Store("Olympia's Store", depts)
# print(my_store)
# print(repr(my_store))