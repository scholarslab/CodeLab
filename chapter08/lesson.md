---
layout: page
title: Codelab / Chapter 08 / Lesson Document
tags: codelab
---
## Control Flow (loop around)

#### Redirecting flow

Sometimes, it can be hard to construct a `while` loop conditional ahead of time. Sometimes, the flow isn't dependent on sequences. We might have complex logic that needs to break out of a loop in the middle of our loop code block. Or we might want to write out each distinct condition for reasons of legibility. Other times, we need to skip past the rest of the code block, to continue on with the loop rather than break out of it entirely.

To illustrate how we might want to accomplish these things, let's play the children's game [Duck Duck Goose](https://en.wikipedia.org/wiki/Duck,_duck,_goose). Every cycle, we ask the user to type in "Duck" or "Goose". If the input is "Duck", we continue the loop from the top. If it's "Goose", we break out of it. We could write this in a number of different ways, but this will help illustrate our new keywords.

```python
while 1:
    word = input("What do you say? ")
    if word.upper() == "DUCK":
        continue
    elif word.upper() == "GOOSE":
        break
    print("Maybe I should explain the rules again...")
```

At the top, `while 1` tells Python to loop forever because 1 (and every other non-zero integer) evaluates as `True` and so it's just equivalent to `while True`. We can do this a lot of other ways because many things evaluate to `True`: `while "Hazel"`, etc. But `while 1` or `while True` are the most common in Python and the most intelligible across different programming languages.

If the input word is "Duck", the `continue` tells Python to continue looping, back from the top, *without* going through the rest of the code. If we `continue`, we never reach the `print()` on line 7.

If the input word is "Goose", we hit the `break` and Python breaks out of the entire loop. If we are using an infinite loop like `while 1`, we definitely want to hit a `break` at some point. The keywords `continue` and `break` can be used in any `for` or `while` loop to modify the control flow.

Now, a `while 1` loop is a little scary. In this example, our exit conditions are pretty direct and the user input prompt keeps memory use from growing uncontrollably, so it's arguably a sound choice.  And its use is really a faithful reproduction of the rules of the game, illustrating the inherent tension at the intersection of childhood and the infinite. 

Now, we could have written this loop in other ways. Here's one example that is logically equivalent:

```python
word = "DUCK"
while word != "GOOSE":
    word = input("What do you say? ")
    if word.upper() != "DUCK" and word.upper() != "GOOSE":
        print("Maybe I should explain the rules again...")
```

Here, we are priming `word` to be "DUCK". This is another common while loop technique, where we set up an initial state so that the loop runs at least once. So while it's a little odd to imagine a version of this game where someone calls out "DUCK" to kick things off, it does make the exit condition a bit more logically straightforward.

Which version makes more logical sense to you?

### Nested Loops: Loops, But More.

![nesting](assets/nesting.gif)

If we want to really master loops, we have to learn how to nest them. Nesting means that we can have one loop inside of another. One reason we might want to do this is if we need to compare different elements in a list with each other.

How might we write a function to check whether a list contains duplicate numbers? With a single layer of looping, it's not so easy. But with two, it's simple. Well. Simple once you get the hang of it.

One good strategy for solving problems like this is to ask: how would we do this as a person? What discrete steps can we break this into? 

So, as a person, how would we check this list for duplicates? `[3,5,7,9,5]`

To start, we need to look at each number in the list individually, to have something to compare all the other numbers to. Let's start with the first number there: 3.

What next? We're at that first number. We should see if there are any other 3s in the list. There aren't.

So we move on to the next number, 5, and repeat. There is another 5, so we can say: "yes, there is a duplicate."

Good, now how do we abstract this in code? Our basic strategy involves two levels of looping: in the first level, we want to take a look at each number; in the other, we want to compare that number against all the other numbers. In Python, this is easier to construct using a `while` loop (`for` loops abstract away some of the index data we want to use).

This is a simple case where we're doing basically the same thing on both levels: just iterating through some numbers. This kind of loop should look familiar:

```python
i = 0 # we're going to use i as a counter to keep track of the index
while i < len(numbers):
    #do some stuff
    i+=1 #increment the index counter
```

So, if we stack one inside of the other, we get something like this:

```python
def got_dupes(numbers):
    i = 0 # i is the first counter, for the outer loop
    while i < len(numbers)-1: #we don't need to loop at the very last number on the outside loop because there's nothing to compare it to
        j = 0 # j is the second counter, for the inner loop
        while j < len(numbers):
            if numbers[i] == numbers[j]:
                return True #duplicate found! Returning True.
            j+=1
        i+=1
    return False #if we complete all the looping without returning, there must not have been any duplicates
```

What's wrong with this code?

We want to loop through all the numbers on the outer loop, but do we want to loop through them all on the inner one too?

Here's the correct code:

```python
def got_dupes(numbers):
    i = 0
    while i < len(numbers)-1: 
        j = i+1 # j starts at the next number after i on every loop
        while j < len(numbers):
            if numbers[i] == numbers[j]:
                return True
            j+=1
        i+=1
    return False
```

We're using nested while loops here, because we care about the order of the numbers. That is, the inner loop has to start with next index from the current index of the outer loop. There is a way to write this with a for loop, even a little more cleanly than here, but the logic is cleaner and more obvious with a while loop, especially for a novice programmer.