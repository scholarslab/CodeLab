# Week 3
![I'm Invincible](assets/invincible.gif)

---
## Lesson

### Discuss homework assignments

### Data Structures
We've covered a few different types of Python's data structures. A data structure is a general term for a way for a computer to structure its data. Programming languages have their own specific kinds of built-in data structures and we'll eventually discuss using custom ones in external libraries and even building our own. For now, we've played around with a few of the ones in Python's standard set.

The Python docs have a pretty good entry for [built-in types](https://docs.python.org/3/library/stdtypes.html).

The most basic data structures contain just a straightforward value: the integer and float numerical data types we've already encountered contain just the single number they represent. More complex composite data types can comprise data across multiple values and different basic types and specific relationships between that data. In dictionary, for example, a single key maps to a single value.

We can chain different data structures together, such as creating a list of lists to form something like a matrix.


### Functions and methods

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

Python's [built-in function documentation](https://docs.python.org/3/library/functions.html) is also a good thing to have on hand.

### Built-in Functions 

### Methods

### Defining Functions
Arguments
Return values

### Putting it all together

## Control flow
### Conditionals
#### Boolean logic
### Loops
#### for
#### while
#### Redirecting flow

---
## Homework for Week 4

Pair program these with a buddy! Pair programming is fun and productive unless you do it wrong. According to formal logic, this does not necessarily mean that doing it wrong cannot also be fun and productive, but it does mean that if it isn't fun and productive, you aren't doing it right.

### Coding Assignment 1: Pick Pair Programmers

Given a hard-coded set of 6 names, write a program that *randomly* assigns everyone a partner and prints out 3 pairs of programmers. Must return a different, correct result each time!

Example:
```python
names = ["Catherine","Cho", "Chris", "Eleanore", "Emily", "Matilda"]
# Your code here
print(pairs)
# E.g. "Catherine and Cho, Chris and Eleanore, Emily and Matilda"
```

Hint:
Remember that we looked at the Python standard library module [Random](https://docs.python.org/3/library/random.html) last week. You can use `len(x)` to find the length of a list/sequence. Alternatively, there is section in the Random module documentation on "Functions for sequences" that may be helpful.

### Coding Assignment 2: Double check!

Given a list of 6 names (`names`) and a list of lists (`pairs`), check whether `pairs` represents a valid and correct pairing of programmers. What do you consider correct? What kind of error conditions are you checking for?

Example:
```python
names = ["Catherine","Cho", "Chris", "Eleanore", "Emily","Matilda"]
pairs = [["Chris","Emily"],["Eleanore","Cho"],["Cho", "Catherine"],["Catherine","Matilda"]]
# Your code here
if is_valid:
   print("This is a valid set of pairings.")
else:
   print("Nope!")
```

Hint:
A list of lists is kind of like a table - it's essentially 2 dimensions, although this doesn't ensure that every row has the same number of columns. Just as you would access a list using list[x], you can access a list of lists using list[x][y].

### Coding Assignment 3: List of Sums

Given a list of integers and a target integer, find the integer pairs in the list that add up to the target.

Example:
```python
input = [1,5,7,9,11,15,19,27]
target = 12
# Your code here
# For the above example, should return (5,7) and (1,11)
```

Hint:
I sure hope we got to talk about nested loops. A nested loop is two loops nested one inside of another. This is a simple way to deal with multi-dimensional lists.

### Read:
The Coder's Apprentice, ch 6-7: [http://www.spronck.net/pythonbook/](http://www.spronck.net/pythonbook/)
