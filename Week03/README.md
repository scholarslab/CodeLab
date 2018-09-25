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
pairs = [["Chris","Emily"],['"Eleanore","Cho"],["Cho", "Catherine"],["Catherine","Matilda"]]
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
