---
layout: page
title: Codelab / 05 Introduction to Python
tags: codelab
---

![https://media.giphy.com/media/9xaryfkdWqqiK6QHKf/giphy.gif](https://media.giphy.com/media/9xaryfkdWqqiK6QHKf/giphy.gif)

## Lesson
[Lesson document](intro_python.md)
0. A brief note about learning with AI 
1. Let's get coding
2. Python interactive interpreter
3. Data structures
4. Documentation
5. Dogs

## Resources
[Python data types cheatsheet](types_cheatsheet.md)

## Terms
* **Binary**: Base-2 numeral system, consisting only of 0 and 1. Counting up from 0, the binary numbers are: 0, 1, 10, 11, 100, 101, 110, 111, 1000...
* **Boolean**: A data type that has two possible values: True and False. These are often used with and associated with the binary values 1 and 0. Boolean values in Python are often used in conditionals and loops (which we'll talk about in the future)
* **Comment**: Parts of the code that are ignored by the computer and are intended as explanatory text for humans.
* **Documentation**: Writing about code. Often, these are formal desciptions of all of the different functions, modules, classes, and methods in a piece of code, such as the [documentation for Python itself](https://docs.python.org/3/). Sometimes, it's less formal instructions and tutorials.
* **Floating Point Number (Float)**: A number with a decimal point (e.g. `3.0` rather than `3`). Because computers use binary numbers internally, we often run into very small and unexpected rounding errors when using floats.
* **Function**: A piece of code that does a specific task. Larger functions can be broken down into smaller ones. Familiar built-in Python functions include `print` and `len`. Functions are defined using the `def` keyword and then can be "called" (executed) by other code at will later on using the `function_name(parameter)` format.
* **Index**: The position of a value inside of a list or other sequence, typically referenced using square brackets. Python is "zero-indexed", which means that the first index of a list is 0. `numbers[0]` references the *first* value of the list `numbers` whereas `numbers[3]` is the *4th* value. So if `numbers = [1,2,3,4,5]`, then `numbers[0]` is `1` and `numbers[3]` is 4.
* **Integer**: A whole number (e.g. `3` rather than `3.0`).
* **List**: A useful built-in Python data structure that represents a linear and ordered collection of data (i.e. data arranged in a row, in a certain order). We define lists using square brackets (e.g. `numbers = [1,2,3]` or `numbers=[]` to create an empty list). We can access an individual item inside of a list using square brackets and its list index (e.g. `numbers[2]`) or a range of indices (e.g. `numbers[2:5]` or `numbers[3:]`).
* **Method**: A function that belongs to a class. Don't worry about that part for now; if you see it mentioned, just treat it as meaning the same as a function.
* **Parameter/Argument**: We can use these terms interchangeably. Parameters are data that's passed into a function or a method (i.e. the `text` part of `print(text)`). We define what parameters a function should expect in the function definition and then we have to pass in the right number and kind of data in the function call.
* **String**: Text data. We can think of it as a list of this as a list of characters. For example, `"Hazel"[2]` is `'z'`.
* **Variable**: A container for data. Variables let us squirrel away a piece of data using a variable name and the assignment operator (`a = 5`) and then refer back to it later (`a + 10`). Any piece of data that we want to keep track of, we have to store away as a variable.

---
## Homework

### Coding Assignment 0: Simplified Pig Latin
Produce a simple program to accept a single word as text input and then print out the [pig latin](https://en.wikipedia.org/wiki/Pig_Latin) translation.

When I first assigned this homework, I didn't actually know that Pig Latin is a more complicated and potentially more ambiguous algorithm than I thought! Because of this, we can implement the simplest case for the word provided: just shift the first letter to the end and add "ay" to it.

Taking into consideration words starting with consonant clusters or vowels requires some conditional logic, which we haven't gone over yet, but feel free to jump ahead if you really want to show off.

Your code should be structured something like this:

```python
word = input("Enter word: ")
# Pig latin code goes here
print(pig_latin)
```

### Natural Language Coding
Once again, let's write, in plain English, precise and detailed step-by-step instructions for a task: given a list of students, pair off each student with a partner, making sure to not double-book anyone and to not assign anyone to be their own partner. What kinds of "edge cases" (unexpected conditions) do we have to watch out for? What's missing from these instructions?

## Read:
Posner, Miriam (2015),  [Humanities Data, a Necessary Contradiction ](http://miriamposner.com/blog/humanities-data-a-necessary-contradiction/)
