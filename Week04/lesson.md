## Week 4: Program Flow (ctd)

![hazel_sleeping](assets/hazel_sleeping.jpg)

### Looping

Functions are neat in part because they let you write a bit of code once and then refer back to that code over and over again in the future. Loops do that too, but let you repeat code dynamically, with the program flow varying depending on inputs. Let's take a look at what sort of problems these structures help with.

Say we want to write a piece of code to sum up all the numbers in a list of integers, like totaling up a column in a spreadsheet. Without Python's loop features, we could add up a set number of elements:

```python
def sum(number_list):
    return number_list[0]+number_list[1]+number_list[2]
```

That's no good. It works, but only for inputs with exactly 3 numbers. It'd fail if we passed in a list with 5 numbers or with 2. We want a way to let Python decide when to repeat and when to stop repeating, based on conditions that we give it.

![looper](assets/looper.gif)

We need a way to loop through code, round and round.

#### while loops

Conveniently, Python's `while` loops let you repeat a code block so long as a condition you specify holds true. Let's take a look at how we could implement the summation code from before with `while`:

```python
def sum(number_list):
    x = 0
    sum = 0
    while x<len(number_list):
        sum = sum + number_list[x]
        x = x+1
    return sum

nums = [0,1,2,3,4,5,6000]
print(sum(nums))
```

Here, the line `while x<len(number_list):` tells Python to loop through the following block so long as the condition `x<len(number_list)` holds true (recall that `len` is a built-in function that tells you the length of a sequence).

The variable `x` acts as a counter. Every loop, we add 1 to x (`x = x +1`). So, the first cycle x is 0, the next cycle x is 1, and so on until x gets to the length of number_list. 

The other line in the while block, `sum = sum + number_list[x]` adds the number at the `x` index of number_list to a running total, `sum`. Because we run one cycle for every value of `x` from 0 to the length of `number_list`, we run this addition for every value in `number_list`.

Once `x` gets higher than the length of `number_list`, the while loop ends. We're left with a `sum` value for the entire list.

The loop condition (the logic that goes after `while`) is a boolean value (`True` or `False`), so we can chain together many different parts using `and` and `or` and `not`. 

### for loops

We've had some experience now with sequences such as lists and strings. We can easily move through theses sequences using the `for` loop. In the last example, we had to keep track of our own counter `x`. But if we just want to do something for each value in a sequence, we really need to do that ourselves.

Let's say we want to write a function to tell every dog in a list of dogs that they're good dogs. Here's what that code might look like:

```python
def good_dog(dog_list):
    for dog in dog_list:
        print(dog + " is a good dog!")

dogs = ["Hazel", "Maple", "Bofur", "Fat Dog"]
good_dog(dogs)
```

A `for` loop moves through a list or string (or any iterable object, but we don't want to talk about that yet) and runs a code block for every part of that list or every character of the string.

In this example, we don't have to use the variable name `dog` to match the list name `dog_list`; we can use any variable name, but using variable names like `dog_list` and `dog` helps us keep track of what's going on.

The code block within the `for` loop is run every cycle and each cycle the `dog` is different. In the first cycle, `dog` is "Hazel" because "Hazel" is the first value in the input list. In the second cycle, `dog` is "Maple".

Here's Maple in the middle of a loop.

![maple_loop](assets/maple_loop.jpg)

#### Redirecting flow

Sometimes, it can be hard to construct a `while` loop conditional ahead of time. Sometimes, the flow isn't dependent on sequences. Let's say we want to play the children's game Duck Duck Goose. Every cycle, we ask the user to type in "Duck" or "Goose". If the input is "Duck", we continue the loop from the top. If it's "Goose", we break out of it.

```python
while 1:
    word = input("What do you say? ")
    if word == "Duck":
        continue
    elif word == "Goose":
        break
    print("Maybe I should explain the rules again...")
```

At the top, `while 1` tells Python to loop forever because 1 evaluates as `True` and so it's just equivalent to `while True`. We can do this a lot of other ways because many things evaluate to `True`: `while "Hazel"`, etc. But `while 1` or `while True` are common and traditional.

If the input word is "Duck", the `continue` tells Python to continue looping, back from the top, *without* going through the rest of the code. If we `continue`, we never reach the `print()` on line 7.

If the input word is "Goose", we hit the `break` and Python breaks out of the entire loop. If we have an infinite loop like `while 1`, we probably want to hit a `break` at some point.

`continue` and `break` can be used in any `for` or `while` loop. But be careful about overusing them, because they can make code hard to read.

### Version Control

[Git for Humanists](https://shane-et-al.github.io/git_slab/)
