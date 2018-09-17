# Python interpreter as calculator
```python
1+1
2**3
```

# Hello World
### Concepts: strings, functions, parameters
```python
print("Hello Cruel World!")
```

# Variables
### Concepts: variables, operator functions (concatenation)
```python
madlibs="Scholars' Lab"
print("I, for one, 'welcome' our new "+madlibs+" overlords!")
```

### Concepts: integers, floats
```python
a = 7
b = 3
a+b
a/b
```


### Concepts: binary representation of numbers
```python
0.1+0.2
```
!["There are 10 kinds of people in the world..."](assets/10kinds.jpeg)

Binary (base 2) comprises only 1s and 0s. Integers are easy enough to represent: 0, 1, 10, 11, 100, 101, 111, ...
Floats are trickier and require a special system to represent. Just as it's impossible to represent exactly 1/3 in finite decimal notation, similarly impossible to represent simple decimal numbers in a binary notation.

[Float to Binary Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)
[IEEE 754 Standard](https://en.wikipedia.org/wiki/IEEE_754-1985)


# Comments and Documentation
### Inline Commenting
```python
# Life is suffering
1+2+3
```

Comments are especially useful--necessary!--for collaboration. Python is open source and its community of millions of coders often share in its permissive approach to intellectual property. Python as a whole is a giant collaborative project of which you are now members.

### Documentation

Python, as with virtually all other languages and complex codes, contains extensive documentation that covers all aspects of its use.

[Python 3 Documentation](https://docs.python.org/3/)

Let's take a look at the specific documentation for strings:

[Python 3 Docs: Built-in Types: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)


# Interlude: The Zen of Python
### Why Python? 
[PEP 20: The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
[Brief Analysis of 'The Zen of Python'](https://medium.com/@Pythonidaer/a-brief-analysis-of-the-zen-of-python-2bfd3b76edbf)


# Sequences

### Lists

```python
dogs = ["Bofur","Hazel","Henry","Fat Dog","Maple", "Monty","Toby"]
print(dogs[0])
print(dogs[-1])
print(dogs[3:])
print(len(dogs))
dogs.sort(reverse=True)
print(dogs[0])
```

![Bad Pun Hazel](assets/badpunhazel.jpeg)

Lists are one type of sequence, which are ordered collections of variables (including sequences, so you can have lists of lists).
[Python 3 Docs: Built-in Types: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

Strings are actually sequence types, just like lists!

```python
gooddog = "Hazel is a good dog"
print("Every dog"+gooddog[5:])
```

# Modules
### Python Standard Library
```python
import random
print(random.randint(0,10))
```

[Python 3 Docs: Standard Library: Numeric and Mathematical: Random](https://docs.python.org/3/library/random.html#module-random)

Of course, you don't always want to write your own code. Programmers are ~~lazy~~ efficient. Python has a famously robust built-in Standard Library so you can reuse the work of thousands of programmers who have contributed to it. This Standard Library is part of the language itself and is included in every Python installation.

For more specialized tasks, it's also easy to use the work of third party developers. But we'll leave that to another week.

# Bring it all together
### Work together
Pair programming is a common practice. We want you to always do pair programming. Let's write some code to assign each of you a partner for this week's homework using what we've just learned!
