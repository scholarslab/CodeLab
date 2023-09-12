# Lesson Plan: Week 04
![Hazel in bed](./assets/hazel_bed.jpg)

## Discuss homework assignments

## Types
We've covered a few different ways Python handles data already. We can describe them as "data structures", a general term for a way for a computer to, ah, structure its data. Programming languages have their own specific kinds of built-in data structures and we'll eventually discuss using custom ones in external libraries and even building our own. For now, we've played around with a few of the ones in Python's standard set.

(There's some distinction between the term "data structure" and "data type" or simply "type", but for our purposes we can mostly use them interchangeably, at least for now.)

### Built-in types

The Python docs have a pretty good entry for [built-in types](https://docs.python.org/3/library/stdtypes.html).

This is a good time to share a useful trick about strings. We've seen that strings in Python are denoted using quotation marks. These can be either single `'` or double '"' quotes, so long as they're matched. One way to define a string that also includes one kind of quotation mark is to use another kind around the string:

```python
print('Edsger Dijkstra, a computer scientist famous for his pioneering work in graph theory, distributed computing, and programing methodology, as well as some really memorable turns of phrase, once said: "The question of whether machines can think is about as relevant as the question of whether submarines can swim."')
```

The most basic data structures contain just a straightforward value: the integer and float numerical data types we've already encountered contain just the single number they represent. More complex composite data types can comprise data across multiple values of different types and the specific relationships between them. A list, for example, is a set of elements with a linear order. A dictionary maps keys (analogous to the word being looked up in a real dictionary) to values (the definition).

We can also chain different data structures together, such as creating a list of lists to form something like a matrix.


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

Instead, we have to tell Python what we mean by doing an explicit conversion using the conversion functions `int()` and `str()`:

```
>>> a = 3
>>> b = "3"
>>> str(a)+b
'33'
>>> a+int(b)
6
```

In Python, we use the single equals sign `=` for *assignment* (assign the right side to the left) and the double equals sign `==` for *equality* (does the right side equal the left?).  Comparitors like `==` yield values of boolean type: `True` or `False`. Under the hood, comparitors are defined as functions (more on this later), so sometimes Python can compare different types and sometimes it can't. Generally, numbers (integers and floats) can be compared as numbers, but comparing strings and numbers will always return `False` because they're fundamentally not comparable and so are inherrently dissimilar.

```
>>> a = 3
>>> b = 3.0
>>> c = "3"
>>> a == b
True
>>> a == c
False
```

## Functions and methods

We've also already used a few functions and methods. A function is a way to organize code by packaging many lines of code together into a single bundle, like how a math function ties together many different operations. In a cookbook, we might explain how to fry an egg at the beginning and refer back to that explanation in later recipes without having to repeat ourselves.

There's a lot of good reasons to organize code into functions. At the most basic level, this makes it easy to reuse code, often easier to read and to organize logic, easier to change code in one place rather than in many places, and easier to *not* understand what you don't need to understand.

Python has a number of "built-in functions", some of which we've already used. As an example, the function `pow(x,y)` returns the value of x to the y power.

```
>>> pow(2,4)
8
>>> pow(2,8)
256
```

When we tell Python to run a function like this, we call that a "function call". Function calls have the name of the function ("pow") followed by a matched pair of parenthesis. Inside the parenthesis are zero or more "arguments", which are bits of data that we "pass in" to the function and which are processed by the code of the function.

In the case of `pow()`, the function needs to know what numbers we want to use. You might not know quite enough Python yet to code this yourself (although you will hopefully by the end of this lesson!), but it's easy enough to just type in `pow(2,8)`.

That's actually an important reason to use functions: you don't need to know how it works, just what it does. Programmers call this a "encapsulation" or "information hiding". For a power function, the difference between how something works and what it does is pretty small, but there are actually a lot of things in programming that are easy to understand and hard to do (the worst of these are easy to do but hard to *do right*). The random functions we've used already are a good example.

If you're really interested in how Python does it, you can take a look for yourself! Python is open source, which means that underlying code for Python itself is freely accessible. I wouldn't necessarily recommend it though, since the reference implementation for Python is written in a different programming language, C, for reasons that are probably too complicated to get into here.

Going back to the cookbook metaphor, a function to fry an egg might look like this: `fry_egg(style="over easy", salt=True)`. You can choose whether to explicitly name the arguments in a function call or just imply them through their order (like with `pow()`).

### Built-in Functions

We've already used a few other built-in functions. `print()` is one we've used a lot. `exit()` and `input()` are others. We've also just used `int()` and `str()` to convert between types. Built-in functions are useful because they perform some of the very basic operations in Python.

One other useful one is `type()`, which will return the type of a variable.

```
>>> type(3)
<class 'int'>
>>> type("3")
<class 'str'>
```

If you get confused about what a function does or expects in terms of arguments, you can use the `help()` built-infunction to look up the documentation for any well-documented function (and also for modules, keywords, classes, etc): `help(pow)`. 

You can also take a look directly at Python's [built-in function documentation](https://docs.python.org/3/library/functions.html).

### Methods

Functions are bits of code that exist independently. When we use `print()` or `exit()`, there's no context that those operations have to be associated with. We can pass in data, but functions aren't parts of that data. When we tell Python to `print(3)`, the act of printing isn't a function of 3. It's just part of Python. This is kind of a subtle distinction that might better be understood by contrasting functions with methods.

Methods are like functions, but a part of an "object". Or it might be easier to think about objects as data structures that also contain special functions that define their behaviors.

For example, Strings have methods. Let's take a look at the documentation for [Strings](https://docs.python.org/3/library/stdtypes.html#textseq).

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

These methods (`replace()`, `upper()`,`split()`) make sense as part of string objects. One way to interpret them is that they're actions that strings can do, whether to other objects or to themselves. They don't have to be methods - we could organize them all as functions that take in strings as arguments, but it makes intuitive sense to group them inside of strings to avoid ambiguity and to keep the set of more fundamental built-in functions tidy.

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

A __really important__ thing to note about that code: the second line of the function definition has a few spaces at the begining. In Python, unlike almost every other computer language, leading spaces and tabs (called "white space") are meaningful. 

In this case, they indicate to Python that everything that's indented (using spaces or tabs) is part of the function definition. As soon as we stop indenting, the function definition is over. We can use any number of spaces or tabs, but they have to be consistent. This tier of code (and technically the tiers it contains) is called a "code block." This kind of outline-like organization scheme is used for many other things in Python, most importantly conditions and loops (we'll get to them in a second) and class definitions (way in the future).

### Arguments/Parameters

Let's break down the pig_latin function definition above a bit further. Here it is again:

```python
def pig_latin(word):
  return word[1:]+word[0].lower()+"ay"
```

`def` tells Python that we're defining a function.

`pig_latin` is the name of the function we're defining.

`(word)` indicates the arguments that we're expecting to be passed in. Here, it's a single one named "word". Arguments and parameters mean essentially the same thing, with slightly different connotations.

`word` can then be used within the function definition like a normal variable. We can tell Python that we're expecting multiple arguments by separating them with comas:

```python
def repeat(word, number):
  return (word+" ")*number
```

One really important idea to understand about arguments is that the name of the variable you're passing in doesn't have to match the name of the parameter in the function definition and that we don't even have to use variables at all - we can use the raw form of the data (i.e. `"Brandon"` or `3`). So, we can call the above `repeat` function using `repeat(name, 3)`. In that case, the variable `name` in the function call is automatically mapped to the parameter name `word` inside of the function block and the raw integer `3` is mapped to the variable `number`. This separates the logic of the code that calls the function from the code of the function itself.

In this way, functions are isolated from the code that calls it. In the same way that if you can call the `fried_egg()` function, you don't need to know how it works, the function itself doesn't have to (and can't) know any more about what kind of code is calling than the arguments provided to it.

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
