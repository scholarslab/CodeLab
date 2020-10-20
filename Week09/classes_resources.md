# Python Classes
Python classes are great for storing complex data structures, but they can also be simple.

Here's how you define a simple class that does nothing.

```python
# Define a class
class student:
    pass  # Pass means "Move along, please. Nothing to see here."

# Create an instance of the class and invoke it
student()
```

What exactly gets invoked in this case since the class has no actual logic in it. For any class, when you invoke it, it executes the `__init__` method. Since our simplistic example above didn't define any logic for the built-in `__init__` method, nothing happened.

## Simple Class

Let's define a class that actually does something when it's initialized.

```python
class Student:
    def __init__(self, name):
        self.name = name

zoe = Student("Zoe")
print(zoe.name)
```

The class instance is the first argument to **_any_** function defined in a class.

```python

class Student:
    """Contains methods for creating a stuent

    Methods:
    --------
    get_full_name
    set_age
    add_hobbies
    get_info
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.hobbies = []


    def get_full_name(self):
        """Returns student's full name
        """
        return self.first_name +' '+self.last_name


    def set_age(self, age):
        """Adds an age to a student

        Method argument:
        -----------------
        age(int) -- Student's age
        """

        self.age = age


    def add_hobbies(self, hobbies):
        """Add a hobby to student's hobbies

        Method arguments:
        -----------------
        hobbies(list) -- List of hobbies
        """

        self.hobbies = self.hobbies + hobbies

    def get_info(self):
        """Return all information about the student
        """
        self_to_dict = {
            'full_name': self.first_name +' '+self.last_name, 'hobbies': ' '.join(self.hobbies),
            'age': self.age
            }
        return self_to_dict
zoe = Student("Zoe", "LeBlanc")
zoe.add_hobbies(["programming", "history"])
zoe.set_age(5000)

print(zoe.get_info()) # To view the docstring for the method
```


    

# Additional Reading

1. [An Introduction to Python Classes and Inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)
2. [Here is a very helpful video series on class inheritance](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)