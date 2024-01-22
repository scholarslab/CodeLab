# Introduction to Python
!["Monty Python"](assets/montypython.jpg)

## Before we get started...
Computer programs are algorithms. These two things are so connected in the lay imagination that they are sometimes used as synonyms for each other. The media talks about "The Algorithm" when it describes Google's search and ad services, Netflix's recommendations, or TikTok's infinite video scroll, but an algorithm isn't some sort of magic tech thing. It's just a sequence of unambiguous procedures, like a particularly rigorous recipe. A computer program is an algorithm that's formatted in a language that a computer can understand.

But knowing the language is only part of writing code. We have to know *what* to tell a computer as well as *how*.

One of the best ways to figure out the *what* is to think about how we might solve the same problem as humans. It's useful to break up things we intuitively conglomerate in our heads into discrete steps. We don't usually examine what we're actually doing when we make exact change or sort of deck of playing cards, so it's useful to make the effort to describe each step, algorithmically. After that, it's just a matter of translating our algorithm into computer language.

This kind of process often helps us define the problem more concretely (what do we mean when we say "sort" a deck of cards?), identify ambiguity in our procedure, and discover unexpected "edge cases" that fall outside of our normal use.

## Python interpreter as calculator
Let's get started with Python.

Python comes with an interactive interpreter that executes your instructions as you enter them line by line. For beginners, it's an excellent way to sandbox your ideas or check your syntax. Start the interactive interpret using the `python` (or `python3`) command.

One of the simplest things we can do is basic arithmetic:

```python
1+1
2**3
```

You can exit using `exit()`. The interactive interpreter is useful to test out an idea or to double check syntax or whether the output of a function matches expectation. But what we type into the interactive interpreter isn't saved and we have to feed it line by line, so it's not a good way to actually write a computer program. For that, we can use VS Code.

## Saving and running Python files

To write and save a Python program, the typical convention is to use the `.py` extension. When we save a file as a .py file in VS Code, it also tells VS Code that it contains Python code and will automatically activate code highlighting and syntax checking.

To run a Python program that you've saved, we can use the `python` command through the terminal with the name of the file that contains your program (if running `python --version` in the terminal shows a 2.x version or "command not found", you will need to use `python3` instead):

```
python code.py
```

## A quick note about Python 2 and Python 3
The Python programming language was first conceived in the late 1980s, but became popular after the release of Python 2.0 in 2000 (not to be confused with [Pythons 2](https://www.imdb.com/title/tt0330795/?ref_=nv_sr_3)) when the language switched to a more public code repository and a more open, community-driven development model.

Python 3 is the current major version. It was released in 2008 as a major reformation of the language that made it more consistent and unified redundant mechanisms. Python 3 is not backwards compatible with Python 2; it is, in effect, a new language. You should definitely use Python 3 because Python 2 finally went away (as coders say, became "deprecated") after more than a decade of parallel adoption.

Many computers come with Python already installed by default. Depending on how yours is set up, running `python` may run the Python 2 or Python 3 interpreter. To determine which one, run the command `python --version`. Pipenv should have this all sorted out, but more on this later.

## Hello World
### Variables, Functions, amd Parameters
Let's take a look at the traditional program used as an introduction to countless programming students before you, Hello World:

```python
print("Hello World!")
```

Try saving this code as a program and running it.

"Print" is a function, which is like a command. Functions are called by writing the function name followed by parenthesis. Inside the parenthesis are zero or more parameters, which are extra bits of information that you attach to the function. The "print" function simply writes out the data that's passed to it.

If you're looking for help on the internet and ever see something like `print "foobar"` instead of `print("foobar")` (without the parenthesis), that's a sign that it's Python 2 code instead of Python 3!

## Variables

!["Monty Python"](assets/overlords.jpg)

### String functions (concatenation)


One of the most fundamental parts of coding is to remember things, which is say: to name them so we can keep track of them. When we describe, in our algorithm exercises, writing the results of a math function down, tallying a count, or even pointing with our finger to a particular item in a list, this is what we're doing. In programming, the label that that put on a piece of data is called a **variable**. When we assign a variable to a piece of information, that's variable assignment and we do it like this:

```python
noun = "Scholars' Lab"
```

Note the direction here. In this example, the variable name "noun" is assigned the string (a type of object that  contains text data) "Scholars' Lab".

Variable names have to start with a letter or an underscore and can only contain letters, numbers, and the underscore character. No spaces. They're also case-sensitive, so `SLAB` `slab` and `SLab` are different.


```python
madlibs="Scholars' Lab"
print("I, for one, 'welcome' our new "+madlibs+" overlords!")
```

In the second line, we use the + operator to concatenate three strings together and pass the result to print.

You can also "multiply" strings.

```python
print("Scholars' L"+"a"*10+"b")
```

### Numbers
```python
a = 7
b = 3
a+b
a/b
```
Integers are whole numbers. Floats (floating point numbers) are prepresentations of real numbers. Integers are simple and easy to use. Floats are mostly easy, but sometimes really weird!

### Weird Numbers

What does this return?

```python
0.1+0.2
```

Huh, weird.

!["There are 10 kinds of people in the world..."](assets/10kinds.jpeg)

(No one really understands binary)

All data in a computer is represented as binary (base 2) numbers, comprising only 1s and 0s. The text you're reading now is represented by individual characters that, under the hood, are stored as binary numbers. The method of translating these information between different forms and contexts (such as between binary numbers and text or numbers) is called encoding.

Integers are easy enough to represent in binary: 0 is 0, 1 is 1, 2 is 10, 3 is 11, 4 is 100, and so on.

But floats are trickier and require a special system to represent. Don't worry about it for now, but consider for a moment that it's impossible to represent exactly 1/3 in finite decimal notation (0.3333...). It's similarly impossible to represent some simple decimal numbers in a binary notation. Which is why you get the weird results above.

[Float to Binary Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

[IEEE 754 Standard](https://en.wikipedia.org/wiki/IEEE_754-1985) if you really want to learn more. You probably do not want to read this.

### Booleans
```python
print(True)
print(False)
print(True or False)
print(True and False)
print(not True)
```
True in Python is interchangeable with the number 1 and False with 0.

## Comments and Documentation
### Inline Commenting
```python
# Help I'm stuck in a Python interpreter
1+2+3
```

Comments are especially useful--necessary!--for collaboration. Python is open source and its community of millions of coders often share in its permissive approach to intellectual property. Python as a whole is a giant collaborative project of which you are now members.

When you write particularly complicated logic or whenever you write new classes or functions (more on this later!), you should write a comment to explain yourself. I will be using comments extensively in the lesson documents to explain what's going on in code.

### Documentation

Python, as with virtually all other languages and complex codes, contains extensive documentation that covers all aspects of its use. This documentation is [easily accessible via the Internet](assets/MissionImpossible.m4v?raw=true).

[Python 3 Documentation](https://docs.python.org/3/)

Let's take a look at the specific documentation for strings:

[Python 3 Docs: Built-in Types: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

Learning to read documentation is a critical skill for succeeding as a programmer. Happily, most of you, as graduate students, should already be literate.

## Interlude: The Zen of Python
### What's the deal with Python? 
Type this into Python:
```python
import this
```

Here's [one interpretation of Z of P](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/).

Also, a DH answer: lots of DH projects are written in Python because of its simplicity and robust community and its popularity in areas like text analysis and machine learning.

## Saving and running code
The Python interactive interpreter is very useful for experimentation, but if you want to write something less ephemereal, you'll want to save it as a file so that it can be run over again without going through it line by line. The code is exactly the same, just save it as a text file to your disk with the usual Python file format extension, .py.

Now, you can run the resulting file using the command `python code.py` (or `python3 code.py`).

There are some important differences in behavior between running code through the interactive interpreter and as a saved .py file. The way that we've been using the interpreter so far has relied on how it returning values that we reference.

If we run these two lines in the interactive interpreter, we see that the second statement prints 2 because Python assumes that we want to know more about it:

```
>>> a = 1+1
>>> a
2
```

If we ran these lines from a .py file, nothing will print at all because the statement `a` on the second line doesn't actually tell Python to do anything. In a .py file, we have to explicitly tell Python to print using the print() function.

```python
a = 1+1
a
```

## Input
Code that always does the same thing is a little boring. Let's spice up the earlier example a bit with user input.
```python
madlibs=input("What manner of overlords do you, for one, welcome? ")
print("I, for one, welcome our new "+madlibs+" overlords!")
```

We can see here that `input` is a function, just like `print`. `input` asks the user to type something and then it "returns" that something back to Python. We'll be writing our own functions soon enough. For now, it's important mainly to understand that functions can hand back bits of data and, like mathematical functions, we can treat the function and the result interchangably in our code. So, if we were to run the example above and the user types in "Hazel", the string "Hazel" would be saved into the variable `madlibs` just as if we'd coded `madlibs="Hazel"`.

## Sequences
### Lists

![Bad Pun Hazel](assets/sleeping_hazel.jpeg)

Lists are one of the most common and useful types in Python. It is a kind of ordered collection, neaning that it contains other objects and those objects are arranged in a sequence. Lists in Python are defined using square brakets, like so:

```python
l = ["Brandon","Ronda","Jeremy","Shane"]`
```

We can refer to an object in a list (an "element") using its position within the list, called its "index". Python list indices, like many other things in computing, are zero-indexed, meaning that we start counting at zero. To retrieve the first element (the element at index 0) in the list we just defined, we can use this code:

```python
print(l[0])
```

Lists can contain any other type of object, including other lists (so you can have lists of lists, which are very useful for things like coordinates). You can play with these examples in the Python interpreter to try out different list actions:

```python
# Defining a list that we assign to the variable `dogs`
dogs = ["Toby","Bofur","Hazel","Rocky","Maple","Henry","Fat Dog","Monty","Keefa","Triscuit"]
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

[Python 3 Docs: Built-in Types: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Strings are actually sequence types, just like lists! They're sequences of characters and we can address particular characters just like with lists.

```python
gooddog = "Rocky is a good dog"
print("Every dog"+gooddog[5:])
```

## Modules
### Python Standard Library
```python
import random
print(random.randint(0,10))
```

[Python 3 Docs: Standard Library: Numeric and Mathematical: Random](https://docs.python.org/3/library/random.html#module-random)

Of course, you don't always want to write your own code. Programmers are ~~lazy~~ efficient. Python has a famously robust built-in Standard Library so you can reuse the work of thousands of programmers who have contributed to it. This Standard Library is part of the language itself and is included in every Python installation.

For more specialized tasks, it's also easy to use the work of third party developers. But we'll leave that to another week.

