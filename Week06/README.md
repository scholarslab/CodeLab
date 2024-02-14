# Week 6: Functions and Methods
![I'm Invincible](assets/invincible.gif)

---
## Lesson
[Lesson document](lesson.md)
1. Discuss homework assignments
2. Types
3. Functions and methods

---
## Homework for Week 6

### Coding assignment 1a

Just like in the lesson, convert your own Pig Latin code from last week into a function in this form:

```python
# Your function definition here

print(pig_latin(input("Enter input: ")))
```

### Coding assignment 1b

Add the function we defined in the lesson to repeate words (`repeat()`)to your code and call it to print the output from part 1a one hundred times.

The expected output for the input "praxis" should be "praxis praxis praxis ..." (100 Praxes).


### Coding assignment 1c

Modify your code in part 1a to `split()` the input into a list of multiple words. If there is only one word, it'll just be a list with one element. Then, only print the Pig Latin for the first word. The [Python documentation for a particualr string method](https://docs.python.org/3/library/stdtypes.html#str.split) will be very useful here!

As an example, the expected output for the input "praxis codelab code lab" should be "raxispay".

### Coding assignment 1d

Modify your code in part 1c to repeat just the first word in pig latin one hundred times, but also print the rest of the words after that.

As an example, the expected output for the input "praxis codelab code lab" should be "raxispay codelab code lab".