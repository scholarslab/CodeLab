---
layout: page
title: Codelab / Chapter 09
tags: codelab
---
# Algorithms and File Operations

![Hazel header](./assets/eva.jpg)

## Outline
1. Discuss homework assignments
2. Sorting
3. File input/output

[Lesson document](./lesson.md)

## Homework

### Assignment 0

[Download the plain text of Much Ado About Nothing from Project Gutenberg](http://www.gutenberg.org/ebooks/1519)

Write a program to read in this file and count the total lines of dialog and the length (character count) of those lines for the two main characters: Benedick and Beatrice. Write that data out to a second file. We can interpret "line" to be whatever makes sense to you. I think that a line being any discrete dialog block for a character, regardless of length is a fair definition.

Feel free to modify the text file before loading it into Python if it'd be easier, for example, you want to remove the starting and ending Project Gutenberg text, the scenes list, the dramatis personae, etc.

The structure of the play is kind of annoying, so we should start by asking ourselves questions like: "how do we know when the play is using the name of a character to indicate that that character is speaking and when it is a mention of that name within the play's dialogue?" Just try your best.

### Assignment BONUS:

Implement a sorting algorithm for sorting a list of numbers. Don't use any built-in sort. It can be as simple or complicated as you want. Feel free to look at the innumerable other examples on the Internet, but we might ask you to walk us through your code next week.

Think back to what we talked about, to mapping human processes to code. Try your best, but don't bang your head against a wall if you get stuck. I'm happy to chat about any of this material, of course.

```python
def sort_numbers(numbers):
    # your code here
    return sorted_list

numbers = [6,3,7,8,1,3]
print(sort_numbers(numbers))
```
