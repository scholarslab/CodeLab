
# A Little Help From Our Friends (at Python)

![hazel](assets/hazel_pet.jpg)

## Coding is hard

Okay, so we've been coding for a while now. You have the basic tools to take on almost anything!

So, let's flex those muscles a bit. Write me the code to return all the permutations for two items out of a list. This might be useful to pick out all the possible pairings out of a list of Scholars' Lab pets. So we want to go from `pets = ["Bofur","Catsby","Hazel","Maple","Pepper"]` to:

```python
[('Bofur', 'Catsby'), ('Bofur', 'Hazel'), ('Bofur', 'Maple'), ('Bofur', 'Pepper'), ('Catsby', 'Bofur'), ('Catsby', 'Hazel'), ('Catsby', 'Maple'), ('Catsby', 'Pepper'), ('Hazel', 'Bofur'), ('Hazel', 'Catsby'), ('Hazel', 'Maple'), ('Hazel', 'Pepper'), ('Maple', 'Bofur'), ('Maple', 'Catsby'), ('Maple', 'Hazel'), ('Maple', 'Pepper'), ('Pepper', 'Bofur'), ('Pepper', 'Catsby'), ('Pepper', 'Hazel'), ('Pepper', 'Maple')]
```

So, where would we start?

Let's go with one loop on the outside and one on the inside, but we want to make sure that the pet in the outside isn't the same as the one on the outside...

```python
def permutations(pets):
    perms = []
    for pet1 in pets:
        for pet2 in pets:
            if pet1==pet2:
                continue
            perms.append((pet1,pet2))
    return perms

pets = ["Bofur","Catsby","Hazel","Maple","Pepper"]
print(permutations(pets))
```

Easy enough... so far. What if we want to do groups of three instead of two?

```python
def permutations(pets):
    perms = []
    for pet1 in pets:
        for pet2 in pets:
            if pet1==pet2:
                continue
            for pet3 in pets:
                p = (pet1,pet2)
                if pet3 not in p:
                    p = p+(pet3,)
                    perms.append(p)
    return perms

pets = ["Bofur","Catsby","Hazel","Maple","Pepper"]
print(permutations(pets))
```

Whew! This is getting a bit rough.

Okay, so what about permutations of 4 pets? Or a generalizable algorithm that calculates different sizes of permutation sets based on a parameter? Hmmm. I think we're going to have to talk about recursion...

But, wait. Remember when I said (a long time ago) that really novel problems are rare and that it's almost certain that other people have had the same problems as you in the past?

What if we could let some hardworking Python developers do the hard work for us?

## Imports

```python
from itertools import permutations
pets = ["Bofur","Catsby","Hazel","Maple","Pepper"]
print(list(permutations(pets,3)))
```

Easy!

We can see in that first line, `from itertools import permutations`, that we're importing a function, `permutations` from the *module* `itertools`, a set of code that provides tools for iterative computation. [Here's the doc.](https://docs.python.org/3/library/itertools.html) 

Modules are broad collections of code. It can contain functions directly (as we see here), but it can also contain classes. Using `from ... import`, we can import any of these components inside of the module.

Itertools is one of many modules that come as part of the Python Standard Library. When Python was released, it was known for this robust library that provided many common and fundamental tools.

Let's take a look at another example.

How do we write a function to return a random number? Beats the hell out of me. This is... actually a really hard problem that has important ramifications for, among a lot of tother things, security if not done right. So we can just use the Python implementation like we did before. (The Python random function is actually also probably not good enough for high-level infosec uses, but it's sufficient for most things we're liable to do.)

![python security warning](assets/security.png)

By nature, randomness is complicated and random number generators are too. There's a lot of stuff in the [Python random module](https://docs.python.org/3/library/random.html), but there's also a few easy functions for us to easily get what we want if we don't care about the nuts and bolts.

We can get a random integer (or a random index for a list):

```python
import random
praxis = ["Bofur","Catsby","Hazel","Maple","Pepper"]
print(praxis[random.randint(0,len(praxis)-1)])
```

(I ran this code to test it and I got 4 Bofurs out of 5 tries.)

![Bofur!](assets/bofur.jpg)

If we read the doc, we can see that randint is inclusive (so, randint(0,5) would sometimes return 5), so we want to do len(praxis)-1 because the valid indices for Praxis are `[0,1,2,3,4]`.

In this example, we can see that instead of importing a single class or function, we just imported the entire module using `import random`. This allows us to access all of its member functions and classes through that name. We could have done this before with `itertools` too:

```python
import itertools
print(itertools.permutations([1,2,3,4,5],2))
```

It just depends on whether or not we just need to use a single function or class from a module or if we want to use more.

If we important random, we can use its other functions (e.g. `random.shuffle()` or `random.sample` to shuffle the list or to pick out a random sampling from that list) without re-importing.

```python
import random
praxis = ["Bofur","Catsby","Hazel","Maple","Pepper"]
print(praxis)
random.shuffle(praxis)
print(praxis)
print(random.sample(praxis,2))
```

We can find the full, glorious index to the Python Standard Library [here](https://docs.python.org/3/library/).

## Importing your own classes

Modules in the Standard Library and from other sources (more on this in a moment) are packaged in a particular way, but we can use imports to bring in our own code too. Let's take the Dog class we worked with last week.

```python
class Dog:
    def __init__(self, name, owner, breed, likes, dislikes):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.likes = likes
        self.dislikes = dislikes
    
    def speak(self):
        print("Bork bork! I'm",self.name)
```

Let's say that we have a few different files that need to refer to Dogs. We don't want to just duplicate this code in all of those, not just because it's messy and a bit of work, but because if we change some part of that Dog code, we want those changes to be the same everywhere so all our code will interoperate with each other. If we added a new data field to our Dog class and constructor, age for example, that new Dog class wouldn't necessarily play well with code that used the old version.

Imports are the solution to this problem. If we save this class to its own file, let's say `dog.py`, we can import this in any other python file in the same directory:

```python
from dog import Dog
hazel = Dog("Hazel","Shane","Beagle",["treats","naps","raccoons"],["thunder"])
hazel.speak()
```

In that first line, `dog` is the name of the file (dog.py) and Dog is the class within that file.
