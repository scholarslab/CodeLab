# Python Classes
Python classes are great for storing complex data structures, but they can also be simple.

Here's how you define a simple class that does nothing.

```python
# Define a class
class noop:
    pass  # Pass means "Move along, please. Nothing to see here."

# Create an instance of the class and invoke it
noop()
```

What exactly gets invoked in this case since the class has no actual logic in it. For any class, when you invoke it, it executes the `__init__` method. Since our simplistic example above didn't define any logic for the built-in `__init__` method, nothing happened.

## Simple Class

Let's define a class that actually does something when it's initialized.

```python
class Zoo:
    def __init__(self, name):
        self.zoo_name = name

a_zoo = Zoo("Zoolandia")
a_zoo.zoo_name
```

The class instance is the first argument to **_any_** function defined in a class.

```python

class Zoo:
    """Contains methods for maintaining a Zoo

    Methods:
    --------
    build_habitat
    sell_family_ticket
    purchase_animal
    """
    def __init__(self, name):
        self.zoo_name = name
        self.animals = dict()
        self.habitats = set()
        self.visitors = list()


    def build_habitat(self, name, type):
        """Adds tuples to the habitats set in the format (name, type)

        Method arguments:
        -----------------
        name(string) -- The marketing name of the habitat
        type(string) -- The type of habitat (e.g. Saltwater, Savanna, Swamp, etc.)
        """

        self.habitats.add((name, type))


    def sell_family_ticket(self, family):
        """Adds an entire family to the list of visitors

        Method argument:
        -----------------
        family(list) -- A list of people in a family of visitors
        """

        self.visitors.extend(family)


    def purchase_animal(self, type, name):
        """Add an animal to the zoo

        Method arguments:
        -----------------
        type(string) -- The type of animal to add
        name(string) -- The given name of the animal
        """

        self.animals[name] = type


    def list_animals(self):
        """Lists all animals in the zoo

        Method arguments:
        n/a
        """

        [print(k + ' the ' + v) for k, v in self.animals.items()]


a_zoo = Zoo("Zoolandia")
a_zoo.purchase_animal("Tortoise", "Tommy")
a_zoo.list_animals()

print(a_zoo.list_animals.__doc__) # To view the docstring for the method
```

## Subclassing

In the previous example, we used strings to define an animal. Let's be more detailed in what an animal is by defining an `Animal` class.

```python
class Animal:
    def __init__(self, name = None, species = None):
        self.name = name
        self.species = species
        self.speed = 0
        self.legs = 0

    def get_name(self):
        return self.name

    def walk(self):
        print("Parent class walk method")
        self.speed = self.speed + (0.1 * self.legs)

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    # __str__ is a special function equivalent to toString() in JavaScript
    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(name, "Dog")

    def walk(self):
        self.speed = self.speed + (0.2 * self.legs)
```

    

# Additional Reading

1. [An Introduction to Python Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
2. [Here is a very helpful video series on class inheritance](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)