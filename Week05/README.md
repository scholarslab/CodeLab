# Week 5
You guys are all doing great!

![racoon_highfive dot gif](assets/racoon_highfive.gif)

## Outline
1. Discuss homework assignments
2. [Conditions and Loops](./lesson.md)

---
## Homework for Week 5

Try pair programming with a buddy!

### Assignment 0: Improved pig latin

Let's go back to our pig latin code again. This time, add a conditional to handle the case where the first letter is a vowel (Wikipedia says: "For words that begin with vowel sounds, generally only a syllable 'yay' is appended to the end, with no modifications to the beginning onset.").

### Assignment 1: Filter evens

Write a function, `filter_evens()` that takes in a list of integers as an argument and returns a list of integers comprising only the even numbers.

```python
def filter_evens(numbers):
   # Your function definition here

nums = [0,-2,3,14]
print(filter_evens(nums))
```

### Assignment 2: FizzBuzz

This is a classic coding puzzle, another rite of passage. Write a program that takes as input a number and then plays the [FizzBuzz game](https://en.wikipedia.org/wiki/Fizz_buzz) until that number is reached. This is a classic programming puzzle and, very helpfully, Wikipedia actually has a list of solutions, including one in Python. But if you use it, be prepared to explain how it works in front of the Fellowship in the next Codelab. It's not the simplest answer (and, in fact, it's Python 2 code), but it might be useful to reverse-engineer!

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