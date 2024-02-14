## Week 07: Control Flow

![hazel_sleeping](assets/hazel_sleeping.jpg)

The order of instructions which a computer program executes is known as "control flow" and we can think it as like a river with a strangely winding, branching, looping course. Functions are our first step in working with code that doesn't simply run linearly, one line after the next. After we define them, we can call back on functions again and again, from anywhere. With functions, just because a line of code appears before a later one doesn't mean that it isn't executed later. 

But functions are still... functionally linear: we're basically copying out a block of code and pasting it back in elsewhere and so we know every time that a particular function will be called. The river always winds one way, the same way, every time.

But sometimes we want to change things up, to make decisions based on what input we provide or what time of day we run our code or even just randomly. Sometimes we want the river to fork. Sometimes we want to take a different path this time than the next and the last. To accomplish this, we must use conditionals and loops.

This is where we start to get to the fun stuff!

### Conditionals

A conditional is a simple way for a computer program to make a choice about flow. The basic syntax of the conditional in many programming languages is the `if` statement. In Python, it looks like this:

```python
x = 5
if x>0:
  print("Positive")
elif x<0:
  print("Negative")
else:
  print("Zero")
```

Let's take a look at the actual *conditions*: `x>0` and `x<0`. These are valid Python statements. If you define a variable `x` and then execute `x>0` in the Python interactive interpreter, we can see that they return Boolean values, `True` or `False`:

```python
>>> x = 5
>>> x > 0
True
>>> x = -5
>>> x > 0
False
```

Around the conditions are the conditional keywords: `if`, `elif` (else if), and `else`. They're what they sound like. Each of the conditional blocks (the three `print()` statements) are only run if the associated conditional statement is `True` (in the boolean logic sense). We can have multiple `elif` blocks if we want. We can also omit `elif` and `else` blocks altogether.

In each of these examples, note the colon at the end of each conditional line. Here, as with function definitions, a colon is a signal that we're going to start a new code block (indicated by the indentation). The different code blocks (the "Positive", "Negative", and "Zero" print statements here) delineate the conditional flow.

For numbers, we can use `>`, `>=`, `==`, `<`, and `<=` to make numeric comparisons. 

In our first example, because we assign `x=5`, the first condition (`if x>0:`) is met and we print out "positive." Because the other statements are `elif` and `else` and we have already met a condition, we do not even evaluate those statements.

### More complex conditions

If we want to modify or chain together boolean statements, we can use `and`, `or`, and `not`:

```python
if not(x>0 and x<0):
  print("ZERO")
```

For strings, we can use use `==` for comparison and some special operators like `in` to see if one string exists inside of another.

```python
if "I" in "TEAM":
  s = "at least one"
else:
  s = "no"
print("There is "+s+" I in TEAM")
```

If a variable is the special `None` object, an empty string (""), or the numeric value zero, it evaluates as boolean `False`. Otherwise, it is `True`.

```python
dog = ""
if dog:
  print("Yay!")
else:
  print("Nooo...")
```

### Constructing Conditionals

Let's take another look at our example:

```python
x = 5
if x>0:
  print("Positive")
elif x<0:
  print("Negative")
else:
  print("Zero")
```

Why is this structured the way that it is? Is it functionally the same as this version?

```python
x = 5
if x>0:
  print("Positive")
if x<0:
  print("Negative")
if x==0:
  print("Zero")
```

Because numbers in Python cannot simultaneously be positive, negative, or zero (and ignoring concurrency for now), these two bits of code are actually equivalent. Only one of `x>0`, `x<0`, and `x==0` can be true at one time.

But this is a simple scenario where we are not only covering all our bases and can be confident that we have thought of all scenarios, but also one in which there are no complicated overlaps between the conditions. Additionally, using `elif` explicitly excludes conflicting code blocks and `else` is often a way to catch unexpected conditions. These are strategies that are useful for writing more legible and robust code.

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