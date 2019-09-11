# Lesson Plan: Week 03
![Hazel in bed](./assets/hazel_bed.jpg)

## Discuss homework assignments

## Types
We've covered a few different types of Python's types and data structures. A data structure is a general term for a way for a computer to structure its data. Programming languages have their own specific kinds of built-in data structures and we'll eventually discuss using custom ones in external libraries and even building our own. For now, we've played around with a few of the ones in Python's standard set.

(There's some distinction between the term "data structure" and "data type" or simply "type", but for our purposes we can mostly use them interchangeably, at least for now.)

### Built-in types

The Python docs have a pretty good entry for [built-in types](https://docs.python.org/3/library/stdtypes.html).

The most basic data structures contain just a straightforward value: the integer and float numerical data types we've already encountered contain just the single number they represent. More complex composite data types can comprise data across multiple values and different basic types and specific relationships between that data. In dictionary, for example, a single key maps to a single value.

We can chain different data structures together, such as creating a list of lists to form something like a matrix.

We've seen that strings in Python are denoted using quotation marks. These can be either single `'` or double '"' quotes, so long as they're matched. One way to define a string that also includes one kind of quotation mark is to use another kind around the string:

```python
print('Edsger Dijkstra, a computer scientist famous for his pioneering work in graph theory, distributed computing, and programing methodology, as well as some really memorable turns of phrase, once said: "The question of whether machines can think is about as relevant as the question of whether submarines can swim."')
```

### Type conversion

The same symbols can be interpreted as different kinds of data. For example, in Python we can refer to "3" both as a number (integer) and as text (string):

```python
a = 3
b = "3"
```

Sometimes, it doesn't matter. `print` is a good example where the way that Python is designed means that it just works for a variety of types.

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

(Also note: That second example wouldn't work like this in Python 2, where the division operation returned values in accordance with the input types. So the integer 7 divided by the integer 2 would return the integer 3. But that's weird and confusing so Python 3 is smarter.)

Sometimes we need to explicitly convert between types because there's ambiguity as to what we want. The `+` operator can be used for both numeric values (as addition) and for strings (as concatenation). For each context, only one kind of data makes sense. So, we can't do this:

```
>>> a = 3
>>> b = "3"
>>> a+b
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Instead, we have to tell Python what we mean by doing an explicit conversion using the conversion functions `int()` and `str()`:

```
>>> a = 3
>>> b = "3"
>>> str(a)+b
'33'
>>> a+int(b)
6
```

## Functions and methods

We've also already used a few functions and methods. A function is a way to organize code by packaging many lines of code together into a single bundle, like how a math function ties together many different operations. At the most basic level, this makes it easy to reuse code: it's easier to write out and read a single line rather than many lines and easier to change code in one place rather than in many places.

Functions that are provided by Python (built-in functions) or by an external library also help to abstract away their implementation details. We often don't care about how something works, only what it does. For example, the built-in function `pow(x,y)` returns the value of x to the y power.

```
>>> pow(2,4)
8
>>> pow(2,8)
256
```

You might not know quite enough Python yet to code this yourself (although you will hopefully by the end of this lesson!), but it's easy enough to just type in `pow(2,8)`.

If you're interested in how Python does it, you can take a look for yourself. Python is open source, which means that underlying code for Python itself is freely accessible. I wouldn't necessarily recommend it though, since the reference implementation for Python is written in a different programming language, C, for reasons that are probably too complicated to get into here.

Python's [built-in function documentation](https://docs.python.org/3/library/functions.html) is also a good thing to know about.

### Built-in Functions

We've already used a few other built-in functions. `print()` is one we've used a lot. `exit()` and `input()` are others. We've also just used `int()` and `str()` to convert between types. Built-in functions are useful because they perform some of the very basic operations in Python.

One other useful one is `type()`, which will return the type of a variable.

```
>>> type(3)
<class 'int'>
>>> type("3")
<class 'str'>
```

### Methods

Functions are bits of code that exist independently. When we use `print()` or `exit()`, there's no context that those operations have to be associated with. We can pass in data, but functions aren't parts of that data. When we tell Python to `print(3)`, the act of printing isn't a function of 3. It's just part of Python. This is kind of a subtle distinction that might better be understood by contrasting functions with methods.

Methods are like functions, but a part of an object. So, let's take a look at the documentation for [Strings](https://docs.python.org/3/library/stdtypes.html#textseq).

Scroll down to "String Methods" and we can see that there are a lot of built-in ways to manipulate strings.

```
>>> s = "Hazel is a good dog"
>>> s.replace("Hazel","Maple")
'Maple is a good dog'
>>> s.upper()
'HAZEL IS A GOOD DOG'
>>> s.split(" ")
['Hazel', 'is', 'a', 'good', 'dog']    
```

These methods (`replace()`, `upper()`,`split()`) make sense as part of string objects. One way to interpret them is that they're actions that strings can do. They don't have to be methods - we could organize them all as functions that take in strings as arguments.

We can imagine, instead of string, a dog type that might have methods `bark`, `sit`, `fetch`:

```python
hazel = dog()
hazel.bark()
hazel.sit()
hazel.fetch()
```

Don't worry to much about methods so much right now other than to know that they exist and that you can look up a list of methods for any built-in type or class in the standard library (more on this maybe next week?) in the Python docs.

### Defining Functions

Let's look at how we can define our own function and turn last week's Pig Latin code into a function.

```python
def pig_latin(word):
  return word[1:]+word[0]+"ay"

print(pig_latin("Hazel"))
print(pig_latin("is"))
print(pig_latin("a")) #how does pig latin work for single-letter words?
print(pig_latin("good"))
print(pig_latin("dog"))
```

Easy, right? Now we don't have to type out the complicated pig latin logic every time we need to use it. By defining a new function `pig_latin()` this way, we can reuse it whenever we want *in the same program* (.py file) or in the same interpreter session (it goes away after we `exit()`). Those five times we used our `pig_latin()` function are called "function calls".

If you run the code above, we can see that there's kind of an error: `pig_latin("Hazel")` returns "azelHay". Pesky capitalization!

But since we defined the important bits as a function, we also only need to change one piece of code and not five!

```python
def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"
```

A __really important__ thing to note about that code: the second line of the function definition has two spaces at the begining. In Python, unlike almost every other computer language, leading spaces and tabs (called "white space") are meaningful. 

In this case, they indicate to Python that everything that's indented (using spaces or tabs) is part of the function definition. As soon as we stop indenting, the function definition is over. We can use any number of spaces or tabs, but they have to be consistent.

Whitespace is used to demarcate other things as well, most importantly conditions and loops (we'll get to them in a second) and class definitions (way in the future).

### Arguments

Let's break down the pig_latin function definition above a bit further. Here it is again:

```python
def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"
```

`def` tells Python that we're defining a function.

`pig_latin` is the name of the function we're defining.

`(word)` indicates the arguments that we're expecting to be passed in. Here, it's a single one named "word".

`word` can then be used within the function definition like a normal variable. We can tell Python that we're expecting multiple arguments by separating them with comas:

```python
def repeat(word, number):
  return (word+" ")*3
```

### Return values

What about that second line? Let's take a look at the return value. Here's that function again:

```python
def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"
  
print(pig_latin("Hazel"))
```

In the same way that we pass an argument into a function, return passes data back from the element to the function call.

So, our `pig_latin()` function receives "Hazel" through the `word` argument and returns the result "azelHay". That result is passed back to `print()` in the function call.


## Control flow

So far, the code that we've written has flowed forward, line by line. Even the function definition: the contents of the `def` block are read in order by the interpreter. This is boring, though. If computation is about choices, this sort of linear flow is boring code.

The order of instructions through which a computer program runs is known as "control flow". We can affect the flow with conditionals and loops which allow us more interesting modes.

### Conditionals

A conditional is a way for a computer program to make a choice. The basic syntax of the conditional in many programming languages is the `if` statement. In Python, it looks like this:

```python
x = 5
if x>0:
  print("Positive")
elif x<0:
  print("Negative")
else:
  print("Zero")
```

We can see the three conditional keywords: `if`, `elif` (else if), and `else`. They're what they sound like. Each of the conditional blocks (the three `print()` statements) are only run if the associated conditional statement is `True` (in the boolean logic sense). We can have multiple `elif` blocks if we want. We can also omit `elif` and `else` blocks altogether.

Note the colon after each conditional line.

For numbers, we can use `>`, `>=`, `==`, `<`, and `<=` to make numeric comparisons. If we want to modify or chain together boolean statements, we can use `and`, `or`, and `not`:

```python
if not(x>0 and x<0):
  print("ZERO")
```

For strings, we can use use `==` for comparison and some special operators like `in` to see if one string exists inside of another.

```python
if "I" in "TEAM":
  s = "at least one"
else:
  s = "no"
print("There is "+s+" I in TEAM")
```

If a variable is the special `None` object, an empty string (""), or the numeric value zero, it evaluates as boolean `False`. Otherwise, it is `True`.

```python
dog = ""
if dog:
  print("Yay!")
else:
  print("Nooo...")
```

### Loops

#### for loops

We've had some experience now with sequences such as lists and strings. We can easily move through theses sequences using the `for` loop. Here's what that looks like:

```python
dogs = ["Hazel", "Maple", "Bofur", "Fat Dog"]
for dog in dogs:
  print(dog + " is a good dog")
```

A `for` loop moves through a list or string (or any iterable object, but we don't want to talk about that yet) and runs a code block for every part of that list or every character of the string. In this example, we don't have to use the variable name `dog` to match the list name `dogs`; we can use any variable name, but a name like `dog` helps us keep track of what's going on.

The code block within the `for` loop acts basically like a function.

#### while loops

No time!

#### Redirecting flow

Nooope.

#### Nested loops

Wooooahh there.

We'll kick the can down the road and cover these and other exciting topics next week.

![Dead Line](./assets/deadline.gif)
