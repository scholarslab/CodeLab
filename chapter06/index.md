---
layout: page
title: Codelab / Chapter 06
tags: codelab
---
# Functions and Methods

[[Back to Codelab index]](../)

![I'm Invincible](assets/invincible.gif)

---
## Lesson
[Lesson document](lesson/)
1. Discuss homework assignments
2. Data structures
3. Type conversion
4. Functions and methods

## Terms
* **Argument**: A piece of data that is passed into a function call, which typically modifies the behavior of the function or method. Often used interchangeably with "Parameter".
* **Built-in**: In Python, a fundamental component of the language that does not require an `import` statement, e.g. built-in functions, built-in data types, etc. 
* **Code block**: A formal logical grouping of code, used to define the boundaries of code like a function definition or a conditional block. Can be nested (one block inside of another). In Python, these are demarcated with indentation.
* **Function call**: execute a function, often with arguments that modify its behavior.
* * **Function definition**: The code that names and implements a function, but does not call it. 
* **Method**: A function that belongs to an object, which we can think as enacting the method.
* **Parameter**: Part of a funcrtion definition that indicates the expectated araguments that will be or can be passed in. Provides a name for the data passed in through function call arguments. Often used interchangeably with "Argument". 
* **Return value**: The result of a function call. Can be empty. Enacted with the `return` keyword inside of a function definition block.
* **Sequence**: a linear array of data, e.g. list, string. Typically accessed through index addressing.

---
## Homework

### Coding assignment 1a

Just like in the lesson, convert your own Pig Latin code from last week into a function. Call the function and pass in a string you get from the `input()` function.

### Coding assignment 1b

Define a function, `repeat()`, that takes in a string and an integer and prints out the string repeated as many times as indicated.

So, this function call should have an expected output of "praxis praxis praxis ..." (100 Praxes):

```python
repeat("praxis",100)
```

### Coding assignment 1c

Use your function code in part 1a and use the `split()` method to split the input into a list of words. Then, only print the Pig Latin for the first word. The [Python documentation for a particualr string method](https://docs.python.org/3/library/stdtypes.html#str.split) will be very useful here!

As an example, the expected output for the input "praxis codelab code lab" should be "raxispay".

(You shouldn't have the change the function definition you wrote in part 1a.)

### Coding assignment 1d

Combine the functions you've defined in parts 1a and 1b, along with the function call in 1c and call them in such a way to repeat just the first word in pig latin ten times.

(You shouldn't have the change the function definitions you wrote in part 1a and 1b.)

As an example, the expected output for the input "praxis codelab code lab" should be "raxispay raxispay raxispay raxispay raxispay raxispay raxispay raxispay raxispay raxispay".

Your code should be in this form:

```python
def pig_latin(input):
    # function definition from 1a
    return latin

def repeat(text, repetitions):
    # function definition from 1b
    return

input_string = input("Enter text: ")
# combine pig_latin and repeat function calls here
```
