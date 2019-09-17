# Week 4
![Git merge dot gif](assets/gitmerge.gif)

## Outline
1. Discuss homework assignments
2. Review conditionals and loops
3. Let's talk about Data: text files and binary files
4. Full steam ahead: [Git for Humanists](https://shane-et-al.github.io/git_slab/)

---
## Homework for Week 4

Try pair programming with a different buddy this time. Or else try to pair program rather than not doing it.

### Assignment 1: FizzBuzz

This is a classic coding puzzle. Write a program that takes as input a number and then plays the [FizzBuzz game](https://en.wikipedia.org/wiki/Fizz_buzz) until that number is reached. This is a classic programming puzzle and, very helpfully, Wikipedia actually has a list of solutions, including one in Python. But if you use it, be prepared to explain how it works in front of the Fellowship in the next Codelab. It's not the simplest answer (and, in fact, it's Python 2 code), but it might be useful to reverse-engineer!

Sample code:
```python
# We're not going to worry about invalid input for this...
i = int(input("Enter a number: "))

# Your code here
# Example output: "1 2 fizz 4 buzz fizz 7"
# (all on one line or on multiple lines are both fine)
```

Hint:
There's a number of built-in operators in Python that may be helpful for this excercise which are [covered in the documentation](https://docs.python.org/3/reference/expressions.html). You'll probably want to use a loop of some kind, so I would suggest reviewing the Python [Control Flow documentation](https://docs.python.org/3/tutorial/controlflow.html).

### Assignment 2: Git Practice

I've created a git repository on the Scholars' Lab account that has a markdown text file for your Praxis cohort at [https://github.com/scholarslab/gitpractice](https://github.com/scholarslab/gitpractice). Hopefully, you should have access to this repository by now. Clone this file to your computer, answer the two original seed questions, then add a new question of your own for your fellows to answer. Check back later in the week for new questions and answer them so that, hopefully, by the time we meet again, we'll have a fully-filled-out and, let's say, quixotically personal questionaire for the entire cohort.


### Assignment 3: Put it together

Take your answer to assignment 1 and push it to a new repository on Github under your account. It's probably easier to create a new repo on Github (the website), clone it to your computer, and copy in the file you've already produced, but you can also try doing an in-place `git init` if you're feeling adventurous.


### Read:
Raymond, Eric S. [The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/index.html): Introduction through "How Many Eyeballs Tame Complexity"

Review as needed: Lin, Shane. [Git for Humanists](https://shane-et-al.github.io/git_slab/).
