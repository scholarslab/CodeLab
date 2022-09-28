## Candidate Obama Speaks at Google (a review of Sorts)


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

### Algorithms

By combining the comparison and loop logic in this way, we've created an algorithm. Algorithms are ways to solve problems using an unambiguous set of instructions. So, "Knight to Queen's Bishop 3" rather than a more vague instruction like "attack the center". 

There are some rather formal definitions for this term, but we can informally and facilely say that all computer programs, including all the ones that you've written, are algorithms.

More usefully, we use the term to describe more generalized ways to solve problems: we can think of the function that we just wrote as an implementation of, let's call it the nested-loop duplication detection algorithm. 

There are [a lot of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms).

### Sorting

Different algorithms can solve the same problem. A very common class of problems is sorting. In Python, we have a few built-in ways to sort things. For example:

```
>>> a = [1,3,2,5]
>>> a.sort()
>>> a
[1, 2, 3, 5]
```

But here, Python is doing the hard work under the table, hiding it through a method so you don't have to know how it works. But behind that method is an algorithm. The sorting algorithm [TimSort](https://en.wikipedia.org/wiki/Timsort) to be exact. It's more complicated than I'd like to get into, so let's take a look at a different one.

How would we sort a list of numbers?

Let's talk it over and then I can assign it as homework.

*Insert insightful class discussion*

Here's a photo of Hazel as a Romantic Hero while we do this.

![Hazel Romantic Hero](./assets/hazel_romantic_hero.jpg)

Good, good. So, for variety, let's look at another way to sort. To introduce it, let's turn to Presidential candidate Barrack Obama, being interviewed at Google Headquarters in late 2007.

[![Obama at Google](https://img.youtube.com/vi/k4RRi_ntQc8/0.jpg)](https://www.youtube.com/watch?v=k4RRi_ntQc8)

I'd say that he's got pretty competent campaign staff.

Bubble sort is, in fact, usually a less efficient way to sort. But it's easy to implement and it's often used for teaching.

[Bubble sort animation](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

Or, let's consider a much worse sorting algorithm: we can just use Python's built-in random shuffle method to scramble the list and then check whether it's sorted. If not, repeat the shuffle.

Obviously, this is much less efficient (time-wise at least) than the other sorts we've looked at. In the same way, there are more efficient ways to sort than Bubble Sort or Insertion Sort. In fact, there's a fairly long [Wikipedia article](https://en.wikipedia.org/wiki/Sorting_algorithm) that just lists different sorting algorithms.

This is all to suggest that there can be different ways to solve the same problem, and that those different ways can have quite different performance properties. "Naive" algorithms that mimic human thinking are a good way to start thinking about problems, but they might not get you very far if you want to optimize performance.

Having given you a taste for all that, I want to say that there's often no... real good reason for us as digital humanists to dive too deeply into algorithms or efficiency. Whether it takes 30 seconds to run our text analysis or 3 seconds isn't as consequential as whether Google returns search results in 30 seconds or 3 seconds. And so much of this, like Python's hidden sort, is just already done for us by things like the Python built-in library and third-party modules (which we'll talk about later).

It's useful to look at the broad contours of these things even if we don't understand them in any depth.

## Files

Let's do one useful new thing this week. User input from the command line is useful sometimes, but sometimes we want to do some heavier lifting.

Let's read in a text file.

In Python, there's a number of ways to do this. One of the easiest is to use the `open` function, which returns a "file object" that represents that file. 

[(Here are the Python docs for this)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

The code for `open` is very simple. To read a file, we can do:

```python
infile = open('file.txt', "r"):
text = infile.read()
infile.close()
```

Text will then be a string that holds the text of the input file.

The call at the end to `close` isn't even strictly necessary. It's good practice to do it for optimal resource management, but Python will do it for you if you forget.

A common idiom to use for Python file handling that you'll often see in examples is to use a with-as block. The last example is:

```python
with open('file.txt', "r") as infile:
    text = infile.read()
```

All this does is structure the code so that you don't forget to close the file.

The file object is also magically iterable, so we can treat it as a list that we can loop through. Another common idiom is to use a for loop to go through it line by line.

```python
infile = open('file.txt', "r"):
for line in infile:
    print(line.upper())
infile.close()
```

The "r" argument that you pass in to `open` tells Python that you want to read the file. To write, we can use "w" mode. This will overwrite the file if it already exists. We can use "a" for append to keep the existing content and just add to the end instead.

```python
outfile = open('file.txt', "w"):
outfile.write("Hazel is a good dog.\n")
outfile.close()
```

The `\n` at the end of that string indicates a new line.

See? Easy!

![Maple Snooze](./assets/maple_snooze.JPG)