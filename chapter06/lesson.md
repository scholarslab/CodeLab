---
layout: page
title: Codelab / 06 Functions and Methods / Lesson Document
tags: codelab
---

![Hazel in bed](./assets/hazel_bed.jpg)

## Types
We've covered a few different ways to represent and organize data already: booleans, integers, strings, floats, etc. We can describe these as "data structures", a general term for a way for a computer to, ah, structure its data. Programming languages have their own specific kinds of built-in data structures and we'll eventually discuss using custom ones in external libraries and even building our own. For now, we've played around with a few of the ones in Python's standard set.

(There's some distinction between the term "data structure" and "data type" or simply "type", but for our purposes we can mostly use them interchangeably, at least for now.)

### Built-in types

The Python docs have a pretty good entry for [built-in types](https://docs.python.org/3/library/stdtypes.html).

This is a good time to share a useful trick about strings. We've seen that strings in Python are denoted using quotation marks. These can be either single `'` or double '"' quotes, so long as they're matched. One way to define a string that also includes one kind of quotation mark is to use another kind around the string:

```python
print('Edsger Dijkstra, a computer scientist famous for his pioneering work in graph theory, distributed computing, and programing methodology, as well as some really memorable turns of phrase, once said: "The question of whether machines can think is about as relevant as the question of whether submarines can swim."')
```

The most basic data structures contain just a straightforward value: the integer and float numerical data types we've already encountered contain just the single number they represent. More complex, so-called "composite" data types can comprise data across multiple values of different types and the specific relationships between them. A list, for example, is a set of elements with a linear order. A dictionary maps keys (analogous to the word being looked up in a real dictionary) to values (the definition).

We can also chain different data structures together, such as creating a list of lists to form something like a table or matrix.

### Sequences

Speaking of lists: lists are one of the most common and useful types in Python. It is a kind of ordered collection, neaning that it contains other objects and those objects are arranged in a sequence. Lists in Python are defined using square brackets, like so:

```python
people = ["Brandon","Ronda","Jeremy","Shane"]
```

We can refer to an object in a list (an "element") using its position within the list, called its "index". Python list indices, like many other things in computing, are zero-indexed, meaning that we start counting at zero. To retrieve the first element (the element at index 0) in the list we just defined, we can use this code:

```python
print(people[0])
```

Lists can contain any other type of object, including other lists (so you can have lists of lists, which are very useful for things like coordinates). You can play with these examples in the Python interpreter to try out different list actions:

```python
# Defining a list that we assign to the variable `dogs`
dogs = ["Toby","Bofur","Hazel","Rocky","Maple","Henry","Fat Dog","Monty","Keefa","Triscuit", "Cheddar"]
# print the first element in `dogs` (remember: zero-indexing)
print(dogs[0])
# print the last element in `dogs`
print(dogs[-1])
# print the sub-list consisting of the fourth element in `dogs` to the end
print(dogs[3:])
# print the length of the `dogs` list
print(len(dogs))
# sort the dogs list, then print it
dogs.sort()
print(dogs)
# sort the dogs list in reverse, then print it
dogs.sort(reverse=True)
print(dogs)
```

We've introduced a few new functions here. With `len()`, we pass in a list (or other piece of data) and it tells us how long or big it is. And `sort()`, which sorts a list. `sort()` is actually a sort of special function called a method (more on this later).

A list in Python is one of several data structures called sequences. You can look through the documentation for this and other sequence types here: [Python 3 Docs: Built-in Types: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

One thing that you might have noticed there: strings are actually sequence types, just like lists! They're sequences of characters and we can address particular characters just like with individual elements in lists.

```python
gooddog = "Rocky is a good dog"
print("Every dog"+gooddog[5:])
```

### Type conversion

The same symbols can be interpreted as different kinds of data. For example, in Python we can refer to "3" both as a number (integer) and as text (string):

```python
a = 3
b = "3"
```

Sometimes, it doesn't matter. `print` is a good example where Python is capable enough of handling a variety of types.

```
>>> print(3)
3
>>> print("3")
'3'
>>> print(3.0)
3.0
>>> print([3,3,3])
[3,3,3]
```

Python (at least Python 3) is also smart enough to convert between numeric values so we can this without a hitch:

```
>>> 3+3.0
6.0
>>> 7/2
3.5
```

(Note: the results here are floats)

Sometimes we need to explicitly convert between types because there's ambiguity as to what we want. The `+` operator can be used for both numeric values (as addition) and for strings (as concatenation). For each context, only one kind of data makes sense. So, we can't do this:

```
>>> 3+3
6
>>> "3"+"3"
'33'
>>> "3"+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Instead, we have to tell Python what we mean by doing an explicit conversion using the functions `int()` and `str()`, which convert inputs to integer and string respectively:

```
>>> a = 3
>>> b = "3"
>>> str(a)+b
'33'
>>> a+int(b)
6
```

In Python, we use the single equals sign `=` for *assignment* (assign the right side to the left) and the double equals sign `==` for *equality* (does the right side equal the left?).  Comparitors like `==` yield values of boolean type: `True` or `False`. Under the hood, comparitors are defined as functions (more on this later). Sometimes Python can compare different types and sometimes it can't. Generally, numbers (integers and floats) can be compared with other numbers, but comparing strings and numbers will always return `False` because they're fundamentally not comparable and so are inherrently dissimilar.

```
>>> a = 3
>>> b = 3.0
>>> c = "3"
>>> a == b
True
>>> a == c
False
```

## Functions

We've also already used a few functions. A function is a way to organize code by packaging many lines of code together into a single bundle, like how a math function ties together many different operations. If we're writing a cookbook, we might explain how to fry an egg at the beginning and, later, if we have a recipe for a fancy burger or for bibimbap, we can just refer to that explanation without having to repeat ourselves.

There's a lot of good reasons to organize code into functions. At the most basic level:

* Functions allow easy code reuse, so if we see a function being referenced we immediately know that it's the same steps as the last time that function popped up, without having to read each step.
* They make it easier to organize instructions intuitively. It often makes sense to break big instructions into specific chunks, especially if they're being reused.
* If we need to change code, we can change it in one place rather than in many places. If we have code that does the same thing in 10 places and we accidentally only fix a bug in 9 of those, it can be very annoying to debug!
* And they can make it easier to *not* understand what you don't need to understand, so long as you understand what it's doing.

Python has a number of "built-in functions", functions which are fundamental to the operation of the language. We've already used several. As an example, `print()` or `len()` are built-in functions. As is the function `pow(x,y)`, which gives us the value of x to the y power and is functionally the same as the ** operator (i.e.`x**y`).

```
>>> a = pow(2,3)
>>> print(a)
8
>>> pow(2,8)
256
```

When we tell Python to use a function like this, we call that a _function call_. Function calls have the name of the function ("pow") followed by a matched pair of parenthesis. Inside the parenthesis are zero or more _parameters_, which are bits of data that we "pass in" to the function and which are processed by its code. Parameters are conceptually similar to and often used interchangably with the term _arguments_, although they have slightly different connotations.

Like a math function, a Python function will usually yield a result. In the first line of the example above, we can say that the function `pow(2,3)` _returns_ a value. There, that "return value" is then assigned to the variable `a`.

In the case of `pow()`, the function needs parameters to know what numbers we want to use. And here, we see that the order of parameters matters. `pow(2,3)` is not the same as `pow(3,2)`.

Based on what you know about programming, can you write the code to compute the answer to the `pow()` function?

Even if the answer is "no", you can still calculate it by simply calling the function. This illustrates an important reason to use functions: you don't need to know how it works, just what it does. Programmers call this a "encapsulation" or "information hiding". For a power function, the difference between knowing how something works and knowing what it does is pretty small, but there are actually a lot of things in programming that are fairly easy to understand and really, really hard to do (the worst of these are easy to do poorly but hard to *do right*). Generating a random number is a good example of this concept.

If you're really interested in how Python does anything, including `pow()`, you can take a look for yourself! Python is open source, which means that underlying code for Python itself is freely accessible. I wouldn't necessarily recommend it though, since the reference implementation for Python is written in a different programming language, C, for reasons that are probably too complicated to get into here.

Going back to the cookbook metaphor, if we imagine a function to fry an egg, the function call might look something like this: `fry_egg(hardness=2, salt=True)`. Here, we've explicitly labeled the arguments that we're passing in, which is an alternative to implying arguments by their order.

We can nest functions calls by passing the return value of one call as the argument for another. Let's take a look at these lines:

```python
a = pow(2,3)
print(a)
```

If we don't need to reference the result `a` again, we can combine these two lines into:

```python
print(pow(2,3))
```

### Built-in Functions

`pow()` is what is called a built-in function in Python. These are the most fundamental, most basic operations in Python which do not require any `import` statement to use. We've already used a few other built-in functions. `print()` is one we've used a lot. `exit()` and `input()` are others. We've also just used `int()` and `str()` to convert between types, and `type()`, which returns the type of a variable.

```
>>> type(3)
<class 'int'>
>>> type("3")
<class 'str'>
```

If you get confused about what a function does or expects in terms of parameters, you can use the `help()` built-infunction to look up the documentation for any well-documented function (and also for modules, keywords, classes, etc): `help(pow)`. 

You can also take a look directly at Python's [built-in function documentation](https://docs.python.org/3/library/functions.html).

### Defining Functions

Think back to the `fry_egg()` function we hypothesized earlier. We can define that function using something like this:

```python
def fry_egg(hardness, salt):
  # imagine that the egg-frying code goes here
  print(f"I am frying an egg until it is at hardness level {hardness}.")
  print(f"I have also added salt if this is True: {salt}.")
  return
```

`return`, by itself, returns nothing. Functions like `print()` don't return anything, while `pow()` and `len()` do. Since we're using `fry_egg()` as an abstract example, it's hard to say whether this is appropriate.

So, `def` tells Python that we're defining a new function. The "fry_egg" part names the function. Inside of the parentheses, `hardness` and `salt` tells Python that this function takes two parameters.

It's important to understand that this only defines the function. We're laying out a procedure. We don't actually cause it to be performed. If we run the above code, nothing would happen - nothing would be printed. 

After we define the function, we need to call it:

```python
def fry_egg(hardness, salt):
  # imagine that the egg-frying code goes in here
  print(f"I am frying an egg until it is at hardness level {hardness}. I have also added salt if this is True: {salt}.")
  return

shanes_hardness_preference = 2
shanes_salt_preference = True
fry_egg(shanes_hardness_preference, shanes_salt_preference)
```

Something that's __important to note__: the variable names we're passing into the function call are distinct from those in the function definition. They *can* be the same, but they don't have to be. The values that we pass into the function call are actually the arguments and the values that we reference in the definition are actually the parameters. Because this function can be called anywhere, these two sets of values don't have to be called the same thing. 

Something else __really important__: after the first line of the function definition, the rest of the lines have a few spaces at the begining. In Python, unlike almost every other computer language, leading spaces and tabs (called "white space") are meaningful. Here, indenting the code in this way signifies that this is a *code block*. The function definition extends only to the end of the current code block. As soon as we stop indenting, the function definition is over. We can use any number of spaces or tabs, but they have to be consistent. This kind of outline-like organization scheme is used for many other things in Python, most importantly conditions and loops (we'll get to them in a second) and class definitions (way in the future).

Okay, let's try another example. Let's take your simplified pig latin code from last chapter's homework and make it into a function:

```python
def pig_latin(word):
  latin = word[1:]+word[0]+"ay"
  return latin

print(pig_latin("Hazel"))
print(pig_latin("is"))
print(pig_latin("a"))
print(pig_latin("good"))
print(pig_latin("dog"))
```

Here, the `pig_latin()` function has a return value, `latin`, that is the string containing the pig latin version of the input.

Easy, right? Now we don't have to repeat the pig latin code every time we need to use it. We just call it five times here for five words. By defining a new function `pig_latin()` this way, we can reuse it whenever we want *in the same program* (.py file) or in the same interpreter session (it goes away after we `exit()`).

If you run the code above, we can see that there's arguably a small bug: `pig_latin("Hazel")` returns "azelHay". Pesky capitalization!

But since we defined the important bits as a function, we also only need to change one piece of code and not five:

```python
def pig_latin(word):
  latin = word[1:]+word[0].lower()+"ay"
  return latin
```

### Return values

What about that second line? Let's take a look at the return value. Here's that function again:

```python
def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"
  
print(pig_latin("Hazel"))
```

In the same way that we pass an argument into a function, return passes data back from the element to the function call.

So, our `pig_latin()` function receives "Hazel" through the `word` argument and returns the result "azelhay". That result is passed back to `print()` in the function call. If we printed directly from the function, this function would only be good for printing; instead, we have access directly to the data that it returns.

![Dead Line](./assets/deadline.gif)


### Methods

Functions are bits of code that exist independently. If we think of them as verbs, we might say that they're verbs that lack a subject. Nothing does them. Or rather, nothing beyond Python itself. When we tell Python to `print(3)`, the act of printing isn't a function of anything. It's just part of Python. This is kind of a subtle distinction that might better be understood by contrasting functions with methods.

Methods are like functions, but exist as being performed by a particular subject. For example, Strings have methods. Let's take a look at the documentation for [Strings](https://docs.python.org/3/library/stdtypes.html#textseq).

Scroll down to "String Methods" and we can see that there are a lot of built-in ways to manipulate strings.

```
>>> s = "Rocky is a good dog"
>>> s = s.replace("Rocky","Maple")
'Maple is a good dog'
>>> s.upper()
'MAPLE IS A GOOD DOG'
>>> s.split(" ")
['Maple', 'is', 'a', 'good', 'dog']
```

These methods (`replace()`, `upper()`,`split()`) make sense as part of string objects. One way to interpret them is that they're actions that strings can do, whether to other objects or to themselves. They don't have to be methods - we could organize them all as functions that take in strings as parameters, but it makes intuitive sense to group them inside of strings to avoid ambiguity and to keep the set of more fundamental built-in functions tidy.

We've worked with strings and lists and we often think of a string as a list of characters. We can address constituent elements of lists and strings in the same ways, using [square brackets]. But they are different types because they define different methods and implement some shared methods differently. In this example, `s` is a string and `l`, defined by `l = s.split(" ")` is a list of the words in `s`.

```
>>> s = "Rocky is a good dog"
>>> l = s.split(" ")
>>> print(l)
['Rocky', 'is', 'a', 'good', 'dog']
>>> type(s)
<class 'str'>
>>> type(s.split(" "))
<class 'list'>
>>> s.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'sort'
>>> l.sort()
>>> print(l)
['Rocky', 'a', 'dog', 'good', 'is']
```

In this example, we can see that the string method `split()` differs from the list method `sort()` in an important way. `split()` returns a brand new object and leaves the original unchanged. `sort()` changes the list itself and returns nothing (actually, the special `null` object). It's hard for almost all people to remember the specific details of what methods do, so it's useful to use the Python interactive interpreter to experiment with code snipets or to read documentation.

String is a fundamental, built-in Python class, but we can can instead imagine a new `dog` class that we define. Such a class might have methods like `bark`, `sit`, `fetch`:

```python
rocky = dog()
rocky.bark()
rocky.sit()
rocky.fetch()
```