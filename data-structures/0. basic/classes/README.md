``` python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1

```

self :
self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

__init__ :
"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.


https://dbader.org/blog/python-repr-vs-str

repr 
- **repr**

- We got Store with **str** printed out. With the **str** representation you can print out whatever you want.
- There's another version of this called repr, the programmatic representation of the string.
- repr should return a string that you could use to re-create that object - actual Python code. This will return a string that has some Python code it in to make this object.
- repr sholud return exactly the same string `Store("Olympia's Store")` - some Python code we could run to recreate this object exactly how it is
- Two places this will show up. Main way to see it is to use the repor functino which works like this `print(repr(my_store)) -` repr you give it an object of any time and it'll give you the Python code that'll create this object
- So **repr** gives you some Python back to recreate that code - repr stands for **representation or reproduce or read, evaluate print repeat, prints our something weird UNLESS you have a repr defined**
- Another place you see repr appear is in the REPL - so bring up the REPL, import oop the name of that file and it'll run this code during the import. But if I make myself a new store in the repl `s = oop.Store("Foo")`  now if I say hey what is s, it gives me the **repr** of that
- repr is primarily used for debugging- exactly what is this object made of? What would I need to run to re-create this object




str 





**To Sum It All Up...**

- We can create **classes** [nouns]  that are used to model real-world objects, usually nouns (Animals, a Player, diff People, Employee)
- Think of then as **blueprints** to make multiple instances of the same object
- Classes contain two main components
    - Attributes [adjectives]- used to describe out class objects
    - Methods [verbs] - diff things our class is able to do


    - **4 principles: encapsulation, data abtraction, inheritance, and polymorphism**
- **Inheritnace** - start with a v broad example and then goto more specific. For ex, may have an Animal a broad general class then you have a Dog which is a subset of animals.
- **Polymorphism** - every child class wil have properties inherited from its parent class and has ability to define its own properties
- **Abtraction**- Idea of thinking things from an abtract level without getting too into code to be able to abstract ideas away, think of it as an obnject instead of code and ones and zeros
- **Encapsulation**- Idea of having private variables / methods and only allowing certain object things public and everything else sholud be private and internal to that ufnction
    - Python doesnt have private variables and doesn't do this v well. It simulates private variables with underscore. Means dont mess with this.


    Make a class that inherits from parent class - core principle: Inheritance and Polymorphism



    - instance attributes vs methods
- We want to differentiate these from class variables and class methods
- The difference between a class and an instance is:
    - The class is the blueprint for creating instances/objects
    - An instance is a specific object