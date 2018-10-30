# Week 7: Class is in Session
![bart_class dot gif](assets/bart_class.gif)

## Agenda:
- Review Homework
- File input and output in Python 
- Let's talk about classes again!
- Importance of Import
- Next week's homework


## File Input

File IO is easy in Python using the [`open` built-in function](https://docs.python.org/3/library/functions.html#open).

To open a file for reading (input), we just do:

```python
input_file = open("text.txt","r")
text = input_file.read()
print(text)
input_file.close()
```

Here, we use the `open` function to open a file in mode "r" (read). `open` returns a [File Object](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) that provides methods for reading and writing. In this case, the `read` method reads in data from the `input_file` file object and stores it as a string in `text`.

At the end, we can close the file to save some memory, but even if we don't do it explicitly, Python will eventually catch on to the fact that it isn't being used anymore and do it for us. This isn't a huge concern unless you're opening thousands of files or the files you're opening are very, very large.

One convenient way to read files is to combine the file object with a for loop to read text files line by line.

```python
input_file = open("text.txt","r")
for line in input_file:
    print(line.upper())
input_file.close(
```
This will loop through the file, line by line, until it's closed.

Often, you'll see file handling used with the `with` keyword:

```python
with open("text.txt","r") as input_file:
    for line in input_file:
        print(line.upper())
```

This is functionally the same as our last example. The only difference is that the file is automatically closed at the end of the block. You can use whichever convention you like, but keep both in mind because they're both pretty common in the wild.

## File Output

File output is very similar. We just use mode 'w', which overwrites the file specified. We can also use 'x' (which only works for new files) or 'a' (which appends data at the end of the file). Read the [`open` docs](https://docs.python.org/3/library/functions.html#open) for all the details.

```python
f = open()
for i in range(0,100):
    f.write(str(i**2)+"\n")
```

Here, there's something just a little tricky. `i` and `i**2` are  integers, but the file object in this case expects a string. If we try to use `f.write(i**2)` instead, we'll get an error: `TypeError: write() argument must be str, not int`.

To get around this, we can convert from int to string using the built-in `str` class constructor `str()` to create a new string that's the *string representation* of the integer we pass in. So even though the inteher 4 and the string "4" look the same, they're different objects and different ways to represent data.

For the same reason that we can't do `f.write(4)`, we also can't do `"4"+4` (or, for that matter, `4+"4"`). We have to explicitly tell python whether we want it to treat each value as an integer or a string. `"4"+str(4)` produces "44" while `int("4")+4` returns 8.

The second new thing here is the newline character "\n", which is technically called a LF or Line Feed. This inserts a line break between characters in a string.

## Putting it Together

Here's part of Emily and Eleanore's solution to one of last week's assignments. Let's ignore the part where we chop off the front matter and focus on just the word replacement.

```python
jane = 'The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'
jane = jane.replace("man","person").replace("wife","partner")
print(jane)
```

Let's say that we want to "modernize" every classic book on Project Guttenberg. The first step is to write a program to read a single book in, replace the words, and then write it back out to a file.

I've pushed the Guttenberg version of Pride and Prejudice as a text to this repository, under the `Week07/examples` directory and the skeleton of the code needed to convert the text:

```python
filename = "pg42671.txt"

### input code goes here

jane = jane.replace("man","person").replace("wife","partner")

### output code goes here
```

## Classes (again!)

Okay, let's review classes!

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

A class is really useful to encapsulate both data and functions in a single cohesive unit. Remember what we learned about classes two weeks ago (you can always refer back to the Week 5 CodeLab materials).

Let's model a dog class that includes some simple logic to track mood.

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
            print("*nuzzle* *happy bark!*")
        elif self.mood > 1:
            print("*regular bark*")
        else:
            print("*grrrrr!*") 
    
    def stimulate(self, stimulus):
        if stimulus in self.likes and self.mood<5:
            self.mood += 1
        elif stimulus in self.dislikes and self.mood>0:
            self.mood -= 1

hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
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
hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
hazel_clone = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])

print(hazel is hazel_clone)
hazel.likes.append("smells")
print("smells" in hazel_clone.likes)

hazel_clone = hazel
print(hazel is hazel_clone)
print("smells" in hazel_clone.likes)
```

The `is` operator returns True if the object is literally the same (that is, they have the same memory address) and false if they aren't. If we don't do anything special, printing an object will actually print its type and memory address.

One important thing to understand is that we already use classes even when we're not defining them. The Class is the primary way that Python organizes its standard library and the wider ecosystem of external libraries. So when we do `file_input = open("text.txt","r")`, we get back a File Object that is defined in a class in the Python Standard Library. 

We can see why the porperties of classes are so useful there: each File Object contains distinct data (the filename and the mode and all sorts of things under the hood) and methods that operate on that data.

## Imports are Important

We can easily bring classes into other code using the `import` keyword, which does some voodoo to allow us to use classes defined in other files. This is how we can use parts of the Python Standard Library that aren't directly built into the base language ([Random](https://docs.python.org/3/library/random.html) is an example that we've encountered before). It's also how we use modules written by other programmers from the larger Python community. More on that next week!

We can also use `import` to import our own classes. It gets complicated if we have to specify the path, so for now it's easier to open the Python interpreter inside the same directory to import.

We can try it out by going into the examples directory, where we have defined the Dog class inside of the file Dog.py.

```python
import Dog
hazel = Dog.Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
```

`import Dog` finds the Dog.py file and then we can create a new Dog object as above.

Alternatively, we can use the `from` convention to import the class Dog directly from the file Dog:

```python
from Dog import Dog
hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
```

## Homework
[Assignments](homework.md)
