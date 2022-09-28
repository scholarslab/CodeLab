# Week 5

## Outline
1. Discuss homework assignments
2. Loops (ctd) + Algorithms
3. File input/output

[Lesson document](./lesson.md)

## Homework

Pair program these with a buddy! Pair programming is fun and productive unless you do it wrong. According to formal logic, this does not necessarily mean that doing it wrong cannot also be fun and productive, but it does mean that if it isn't fun and productive, you aren't doing it right.

### Assignment 0:

Implement a sorting algorithm for sorting a list of numbers. Don't use any built-in sort. It can be as simple or complicated as you want. Feel free to look at the innumerable other examples on the Internet, but be prepared to explain your code!

Think back to what we talked about, to mapping human processes to code. Try your best, but don't bang your head against a wall if you get stuck. I'm happy to chat about any of this material, of course.

```python
def sort_numbers(numbers):
    # your code here
    return sorted_list

numbers = [6,3,7,8,1,3]
print(sort_numbers(numbers))
```

### Assignment 1

[Download the plain text of Much Ado About Nothing from Project Gutenberg](http://www.gutenberg.org/ebooks/1519)

Write a program to read in this file and count the total lines of dialog and the length (character count) of those lines for the two main characters: Benedick and Beatrice. Write that data out to a second file.

### Assignment 2

* In preparation for next week's Brandon Code Lab Special Episode, read through the piece [here](https://humanitiesprogramming.github.io/exercises/python-debugging/) on "common code errors and how to find them" (don't worry about working through the exercises).
* Send Brandon (by slack, email, or github) a working program that answers some homework exercise from CodeLab so far. 
* Send a partner two copies of the same code - one that works, and one that has a bunch of errors you introduced to it. They should be small! An example might be:

my_sentence = "hello' <br>
print my sentence

And a debugger would look at this and say "Ok. I need to make sure the double quotation marks match when assigning the variable. I need parentheses around the print statement. And I also need an underscore between my and sentence.

* Solve the broken code your partner gave you! You'll use the working code they shared if you get stuck.
