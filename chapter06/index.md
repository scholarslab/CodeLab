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
