---
layout: page
title: Codelab / Chapter 08
tags: codelab
---
# Control Flow (loop around)

![Hazel header](./assets/20170126.jpg)

## Outline
1. Discuss homework assignments
2. Loops (ctd)

[Lesson document](./lesson.md)

## Homework

### Assignment 0

Write a Python program to implement our instructions for returning exact change from Week 2. Something that looks like this...

```python
DENOMINATIONS = [100,20,10,5,1,0.25,0.1,0.5,0.01]

def change(cost, payment):
    # your code here
    return list_of_change

# Test cases
print(change(5,2.55))
print(change(2.55,5))
print(change(5,5))
print(change(0,5))
```

### Assignment 1

This one's near to my heart: I wrote out a few solutions to this one in an interview for my first job out of college. You'll only have to find one of them. Given a target integer and a list of integers, find the pairs of numbers in that list that add up to the target.

So, for a `target = 9` and input list `numbers = [0,1,3,6,7,8]`, the expected result would be: `[[1,8],[3,6]]`.

The code could be written in this basic form:

```python
def find_sums(target, numbers):
    pairs = []
    # code goes here
    return pairs

print(find_sums(9,[0,1,3,6,7,8]))
print(find_sums(11,[0,8,3,6,7,4]))
```

What are some ambiguities in the instructions? What are some of the tricky edge cases we should account for?