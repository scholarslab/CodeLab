# Week 3
![I'm Invincible](assets/invincible.gif)

## Lesson
Lesson document:
1. Discuss homework assignments
2. Review data structures
3. Conditionals and Loops
4. Functions

---
## Homework for Week 4

### Coding Assignment 1: Pick Pair Programmers

Given a hard-coded set of 6 names, write a program that randomly assigns everyone a partner and returns the data as a list of 3 tuples, each representing a pair of programmers. Must return a different, correct result each time!

Example:
```python
names = ["Catherine","Cho", "Chris", "Eleanore", "Emily", "Matilda"]
# Your code here
print(schedule)
```

Hint:
Remember that we looked at the Python standard library module [Random](https://docs.python.org/3/library/random.html) last week. You can use `len(x)` to find the length of a list/sequence. Alternatively, there is section in the Random module documentation on "Functions for sequences" that may be helpful. 

### Coding Assignment 2: Double check!

Given a hard-coded set of 6 names and a list of 3 tuples (the same output format of assignment 1), check whether the list represents a valid and correct pairing of programmers given the 6 names. What do you consider correct? What error conditions are you checking for?

Example:
```python
names = ["Catherine","Cho", "Chris", "Eleanore", "Emily","Matilda"]
schedule = [("Chris","Emily"),("Eleanore","Cho"),("Cho", "Catherine"),("Catherine","Matilda")]
# Your code here
print("This is a valid pairing: " + is_valid)
```

Hint:
[Tuples are kind of like lists.](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

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
I sure hope we got to talk about nested loops.

### Read:
