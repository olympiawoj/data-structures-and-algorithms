# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# super() -  allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    # def __repr__(self):
    #         return f"REPR {self.lat} {self.lon} {self.}"

    def __str__(self):
        return f"{self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)



## DEPT STORE EXAMPLE

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

my_store = Store("Olympia's Store", depts)
print(my_store)
print(repr(my_store))
