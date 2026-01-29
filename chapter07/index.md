---
layout: page
title: Codelab / Chapter 07
tags: codelab
---
# Control Flow

[[Back to Codelab index]](../)

You guys are all doing great!

![racoon_highfive dot gif](assets/racoon_highfive.gif)

## Outline
1. Discuss homework assignments
2. [Conditions and Loops](./lesson.md)

## Terms

* **Library/Module/Package**: External code can be brought into your code using the `import` keyword. These are all terms to refer to different levels of code (a Python package is a collection of related modules, a library is less formally defined).

## What's What With Walsh

> One thing programming offers digital humanists is the ability to work at scale. Many of the activities we do as humanists work on a fairly small scale - we read closely, we analyze, we write. But how would you read ten million texts? Programming can help us address great quantities of data, and looping, the application of a particular set of programming texts to many different elements, is fundamental to large scale work. They can be useful for, say, bulk assigning different metadata labels to particular chunks of work. For example, we used loops when working on Michelle Morgenstern's tumblr data to preprocess a variety of social media posts to make them ready for analysis. Digital text analysis commonly lowers the case of all words in a text to make quantifying them easier and more accurate, so we could have used a loop to say "go over every word in this post and lowercase it." But, as a linguistic anthropologist, Michelle actually cared about capitalization in some cases as it could be a rhetorically interesting. Whether or not we wanted all words to be lower cased depended on the context. So we actually implemented a version of "when looking at raw word counts, lower the case of all words except in a set of predefined instances." Combining conditional statements with loops like this meant that we could flexibility build up a project that reflected her needs as a scholar.
> - Brandon

---
## Homework for Week 07

Consider pair programming with a buddy!

## Assignment 0:

What is the output of this code?

```python
x = 0
if x == 0:
  x = 1
if x == 1:
  x = 2
if x == 2:
  x = 3
print(x)
```

And this?

```python
x = 0
if x == 0:
  x = 1
elif x == 1:
  x = 2
else:
  x = 3
print(x)
```

### Assignment 1: Improved pig latin

Let's go back to our very basic pig latin code again. It probably looks something like this:

```python
word = input("Enter word: ")
print(word[1:]+word[0]+"ay")
```

This time, add a conditional to handle the case where the first letter is a vowel (Wikipedia says: "For words that begin with vowel sounds, generally only a syllable 'yay' is appended to the end, with no modifications to the beginning onset.").

### Assignment 2: Filter evens

Write a function, `filter_evens()` that takes in a list of integers as an argument and returns a list of integers comprising only the even numbers.

```python
def filter_evens(numbers):
   # Your function definition here

nums = [0,-2,3,14]
print(filter_evens(nums))
```

### Assignment 3: FizzBuzz

This is a classic coding puzzle, another rite of passage. Write a program that takes as input a number and then plays the [FizzBuzz game](https://en.wikipedia.org/wiki/Fizz_buzz) until that number is reached. This is a classic puzzle that's been an introductory task for millions of beginner programmers.

Sample code:
```python
# We're not going to worry about invalid input for this...
i = int(input("Enter a number: "))

# Your code here
# Example output: "1 2 fizz 4 buzz fizz 7"
# (all on one line or on multiple lines are both fine)
```

Sample output:
```
Enter a number: 7
1
2
Fizz
4
Buzz
Fizz
7
```

Hint:
There's a number of built-in operators in Python that may be helpful for this excercise which are [covered in the documentation](https://docs.python.org/3/reference/expressions.html). Take a look at the "modulo" operator in particular. You'll probably want to use a loop of some kind, so I would suggest peeking at the Python [Control Flow documentation](https://docs.python.org/3/tutorial/controlflow.html).

Remember to test your code. Try to see if your output matches the sample output above. Does it have the right number of prints? Try it out with other inputs too. What is the correct output if the user enters the value 15?
