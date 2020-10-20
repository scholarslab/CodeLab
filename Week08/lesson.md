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

This is pretty legible because these are all the same type of things. But what if we want to return more than just the dog's name? Does "Hazel" really capture the full goodness of this dog? Of course not.

What if we want to return other attributes about Hazel? She's a Beagle/Heeler mix. She's Shane's dog. She likes treats, naps, and raccoons; she doesn't like thunder. How would we have this function return all of this information?

We've experimented already with using data structures to describe, er, data in a more *ahem* structured way. We can return all of this data using lists and dictionaries:

```python
def whos_a_good_dog():
    return({"name":"Hazel","breed":"beagle/heeler","owner":"Shane","likes":["treats","naps","raccoons"],"dislikes":["thunder"]})
print(whos_a_good_dog())
```

This isn't too bad, but we can do better. It's a perfectly fine way to describe complex data within a single object, but if we add more dogs, we'd want to add logic to ensure that they have the same keys and maybe to compare likes and dislikes. Where would that logic go?

On top of that problem, a dog isn't just data. I think this is one of the Four Noble Truths.

Here, we've described largely static information about Hazel. But a dog has behaviors and feelings. In code-speak, we can say that it has logic and states.

A "class" is a really useful mechanism to encapsulate both data and functions in a single cohesive unit. Classes describe a type of object, like "dog" or "praxis fellow". We can create ("instantiate") an "instance" or "object" of a class and reference it using a variable.

We've already used a lot of built-in classes. Strings, lists, dictionaries are all classes. We can have Python tell us what kind of class it is using the built-in function `type()` (terminologically, "type" is often used interchangably with "class", though there are subtle differences depending on the particular language).

```
>>> a = [1,2,3]
>>> type(a)
<class 'list'>
>>> b = "123"
>>> type(b)
<class 'str'>
```

So, in this example, `a` is a variable that serves as a reference to an object that is an instance of the built-in Python class `list`.

We can define our own classes just like we defined out own functions. Let's make a simple dog class with a "speak" method.

Methods are basically the same as functions, except that instead of being "anonymous", methods are attached to particular objects. Here, we could have defined `speak()` as a function that takes a dog as an argument and achieved the same result, but it's easier to think of speech as being an action that a dog performs than as an unembodied abstraction that you pass a dog to.

```python
class Dog:
    name = "None"
    def speak(self):
        print("Bork bork! My name is ",self.name,"!")

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

hazel = Dog("Hazel","Shane","beagle/heeler",["treats","naps","raccoons"],["thunder"])
hazel.speak()

```

Classes can be as simple or complex as you want.

Let's try to model a dog class that includes some simple behavioral and state logic.

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
            print("*bork bork!*")
        elif self.mood > 1:
            print("*bark*")
        else:
            print("*grrrrr!*") 
    
    def pet(self):
        self.mood += 1

hazel = Dog("Hazel","Shane","beagle/heeler",["treats","naps","raccoons"],["thunder"])
hazel.speak()
hazel.pet()
hazel.pet()
hazel.speak()
```

When we call the constructor (`hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])`), we create a new dog object with the parameters we pass in and have the variable `hazel` point to it. We say that the object we created is an *instance* of the class Dog. The variable `hazel` is a *reference* to that instance. Two different variables can point to the same object. Two different objects that contain identical data are not the same.

For example:

```python
hazel = Dog("Hazel","Shane","beagle/heeler",["treats","naps","raccoons"],["thunder"])
hazel_clone = Dog("Hazel","beagle/heeler","Shane",["treats","naps","raccoons"],["thunder"])

print(hazel is hazel_clone)

hazel_clone = hazel
print(hazel is hazel_clone)
```

The `is` operator returns True if the object is literally the same (that is, they have the same memory address) and false if they aren't. If we don't do anything special, printing an object will actually print its type and memory address. In this example, we see that even though `hazel` and `hazel_clone` are dogs comprising the same data, they aren't the same *object*. If we use assignment (`=`) to assign the object referenced by `hazel` to `hazel_clone`, we're explicitly telling `hazel_clone` to point to the same object as `hazel` (in some other languages, references are called "pointers") and so they become the same.

(The reason that we're using `is` instead of `==` is because the equality operator can be *overriden* under the hood if we wanted to have some fancy kind of comparison logic. By default, it is the same as `is`, but it's often overriden. We can compare two distinct, but identical lists using `==` and it will return `True` because `list` overrides the equality operator. But that isn't something we need to get into here.)

Classes underpine an influential way of organizing computer programs: Object Oriented Programming (OOP), where the basic unit of code are class. Python was created originally as a primarily Object Oriented language, because Object Orientation was ascendant in the 1990s when Python was first created. Many important programming languages of that broad era are OO languages: C++, C#, Java, Javascript, and Ruby to name a few of the most famous. However, Object Orientation is not the only "programming paradigm" and Python code can organized both procedurally and functionally.

It's not necessary or useful to organize our code into classes, especially if that code is fairly simple. However, it is a useful option and important to understand for another reason: we use classes even when we're not defining them. The class is the primary way that Python organizes its own standard library and the wider ecosystem of external libraries.