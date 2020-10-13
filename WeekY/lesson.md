# Classes

Okay, let's talk classes!

Say we have this function:

```python
def whos_a_good_dog():
    return("Hazel")
print(whos_a_good_dog())
```

![bad pun hazel](assets/bad_pun_hazel.jpg)

This is very simple. Let's make it a bit more complicated. `return` only takes one object, so if we want to return multiple dogs, we can return a list of strings (a list is one object, which contains multiple elements within):

```python
def whos_a_good_dog():
    return(["Hazel","Maple","Bofur","Toby"])
print(whos_a_good_dog())
```

This is pretty legible because these are all the same type of things. But what if we want to return more than just the dog's name? Does "Hazel" really capture the full goodness of this dog?

What if we want to return other attributes about Hazel? She's some sort of Beagle mix. She's "Shane's" dog. She likes treats, naps, and raccoons; she doesn't like thunder. How would we have this function return all of this information?

One way is to return all of this data in a list:

```python
def whos_a_good_dog():
    return(["Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
print(whos_a_good_dog())
```

But this has become not very legible. Unlike a list of dogs, this list contains dissimilar elements. It's hard to read because the meanings of its values depend on understanding that the value in the first index is the name, the second index is breed, etc. Indices are easy for a computer to keep track of, but if a human gets mixed up, it can be very difficult to figure out what's going wrong and where it's going wrong.

How do we do better?

One way is to use more structured data, like a dictionary:

```python
def whos_a_good_dog():
    return({"name":"Hazel","breed":"Beagle","owner":"Shane","likes":["treats","naps","raccoons"],"dislikes":["thunder"]})
print(whos_a_good_dog())
```

Dictionaries are great and this is much easier to read and to use.  It's a perfectly fine way to describe complex data within a single object.

But a dog isn't just data. I think this is one of the Four Noble Truths.

We've described largely static information about Hazel. But a dog has behaviors and feelings. In code-speak, we can say that it has logic and states. 

A class is really useful to encapsulate both data and functions in a single cohesive unit. 

A class is a particular type of objects. We can create ("instantiate") an object of a class and store it as a variable. A variable therefore contains (technically, contains a reference to) an *instance* of a class.

We've already used a lot of built-in classes. Strings, lists, dictionaries are all classes. We can have Python tell us what kind of class it is using the built-in function `type()`.

```
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> b = "123"
>>> type(b)
<class 'str'>
```

We can define our classes too. Let's make a simple dog class with a "speak" method.

```python
class Dog:
    name = ""
    def speak(self):
        print("Bork bork! I'm",self.name,"!")

maple = Dog()
maple.name = "Maple"
maple.speak()

hazel = Dog()
hazel.name = "Hazel"
hazel.speak()

print(hazel == maple)
```

So, here we define a Dog class, then instantiate two Dogs using `Dog()`. We store those to `maple` and `hazel`. Each of the Dogs are distinct Dog instances and have their own independent data. Whenever we call a class method, we actually implicitly pass in the object itself. That's why the method definitions have `self` in the arguments list. In methods, we refer to `self` when we want to access the variables that belong to the class rather than the method. If you're curious about why we use `self`, [the Python documentation on class scope](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) is useful, but you can get by for now just using `self` whenever you want to refer to any class data.

We can see that instantiation is done with a function: `Dog()`. Instead of setting the data for each bit by bit, we can create a *constructor* method that takes in parameters and then handles them. We can do this by defining a special method `__init__` (with two underscores on either side).

```python
class Dog:
    def __init__(self, name, owner, breed, likes, dislikes):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.likes = likes
        self.dislikes = dislikes
    
    def speak(self):
        print("Bork bork! I'm",self.name,"! I like",self.likes[0], "and dislike ",self.dislikes[0],"!")

hazel = Dog("Hazel","Shane","beagle",["treats","naps","raccoons"],["thunder"])
hazel.speak()

```

Classes can be as simple or complex as you want.

Let's try to model a dog class that includes some simple logic to track mood.

```python
class Dog:

    def __init__(self, name, owner, breed, likes, dislikes):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.likes = likes
        self.dislikes = dislikes
        
        # default mood value, range 0-5
        self.mood = 2

    def speak(self):
        if self.mood > 3:
            print("*happy bork!*")
        elif self.mood > 1:
            print("*regular bark*")
        else:
            print("*grrrrr!*") 
    
    def stimulate(self, stimulus):
        if stimulus in self.likes and self.mood<5:
            self.mood += 1
        elif stimulus in self.dislikes and self.mood>0:
            self.mood -= 1

hazel = Dog("Hazel","Shane","beagle",["treats","naps","raccoons"],["thunder"])
hazel.stimulate("thunder")
hazel.stimulate("thunder")
hazel.speak()
hazel.stimulate("treats")
hazel.stimulate("treats")
hazel.speak()
hazel.stimulate("naps")
hazel.stimulate("raccoons")
hazel.speak()
```

When we call the constructor (`hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])`), we create a new dog object with the parameters we pass in and have the variable `hazel` point to it. We say that the object we created is an *instance* of the class Dog. The variable `hazel` is a *reference* to that instance. Two different variables can point to the same object. Two different objects that contain identical data are not the same.

For example:

```python
hazel = Dog("Hazel","Shane","beagle",["treats","naps","raccoons"],["thunder"])
hazel_clone = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])

print(hazel is hazel_clone)
hazel.likes.append("smells")
print("smells" in hazel_clone.likes)

hazel_clone = hazel
print(hazel is hazel_clone)
print("smells" in hazel_clone.likes)
```

The `is` operator returns True if the object is literally the same (that is, they have the same memory address) and false if they aren't. If we don't do anything special, printing an object will actually print its type and memory address.

One important thing to understand is that we use classes even when we're not defining them. The class is the primary way that Python organizes its standard library and the wider ecosystem of external libraries. So when we do `file_input = open("text.txt","r")`, we get back a File object that is defined as a class in the Python Standard Library.

```
>>> file_input = open("test.txt","r")
>>> type(file_input)
<class '_io.TextIOWrapper'>
```

We can see why the properties of classes are so useful there: each File Object contains distinct data (the filename and the mode and all sorts of things under the hood) and methods that operate on that data.
