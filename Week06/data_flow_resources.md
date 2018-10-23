# Data Flow

Computers read code line by line, top to bottom of a script. But what if you want to have code run not in sequential order, or you want your code to do something depending on a value, or you want to reuse your code and run it multiple times?

We can solve all those problems with data flow structures.

#### For Loops
**For Loops** are one of the most common ways in python to loop over a sequence. 

![https://www.oreilly.com/library/view/head-first-python/9781449397524/httpatomoreillycomsourceoreillyimages1368346.png.jpg](https://www.oreilly.com/library/view/head-first-python/9781449397524/httpatomoreillycomsourceoreillyimages1368346.png.jpg)

We've already used for loops in lists before, like this:
```python
slab = ['Zoe', 'Shane', 'Brandon']

for person in scholars_lab:
    print(person) # This should print out each person's name individually
```

We can also use For Loops on dictionaries. The syntax is slightly different because dictionaries are not one long sequence, but rather a sequence of key/value pairs.
```python
scholars_lab = {
    'employee_1': {
        'name':'Zoe',
        'DH_methods': ['gifs', 'data visualization', 'web apps']
    },
    'employee_2': {
        'name':'Shane',
        'DH_methods': ['programming_genius', 'TEI']
    },
}
for key, value in scholars_lab.items():
    print('key', key)
    print('value', value)
```
This script should print out each of the employee keys and then the dictionaries those keys contain.


#### Conditionals
Earlier we learned about *booleans* (`True or False`). In Python, we can test the truth value of code to decide how we want our code to run.

![https://automatetheboringstuff.com/images/000019.jpg](https://automatetheboringstuff.com/images/000019.jpg)

Taking our list again, instead of printing out each name. Let's only print if the name equals Zoe.
```python
slab = ['Zoe', 'Shane', 'Brandon']

for person in scholars_lab:
    if person == 'Zoe':
        print(person)
```


We can also test the equality of two variables in an if statement:
```python
zoe = 'Zoe'
brandon = 'Brandon'
if zoe != brandon:
    print('not the same person')
else:
    print('twins')

```
There's lots of ways to test equality with what we call **logical operators**.

![https://introcs.cs.princeton.edu/python/12types/images/ComparisonOperators.png](https://introcs.cs.princeton.edu/python/12types/images/ComparisonOperators.png)

#### Functions
Essentially functions are a way to wrap your code into blocks so that way you can call your code when you need it to run. You can check out the materials from last week on functions [here](../../Week06/)

![https://swcarpentry.github.io/swc-releases/2016.06/python-novice-inflammation/fig/python-function.svg](https://swcarpentry.github.io/swc-releases/2016.06/python-novice-inflammation/fig/python-function.svg)

To create a function, we define using `def` and a unique name and finally parentheses, followed by colon. Then we can pass *arguments* (also called parameters) in the parentheses, that we can that use *inside* of the functions. Those arguments will be *variables* and so we can do anything you would normally do to a value. Finally we can *return* the result of our manipulation.

Here's an example of just returning a simple function
```python
def get_fundamentals():
    fundamentals = 'Having fun'
    return fundamentals

get_fundamentals()
```
This function will work but doesn't really do anything. Let's figure out how to output `fundamentals`.

```python
def get_fundamentals():
    fundamentals = 'Having fun'
    print('inside function value', fundamentals)
    return fundamentals

fun = get_fundamentals()
print('returned value', fun)
```
Here we're outputting twice the value, once inside and once outside of the function. 

Let's try passing an argument and manipulating it!

```python
def get_fundamentals(fundamentals):
    fundamentals = fundamentals + 'fun'
    print('inside function value', fundamentals)
    return fundamentals

fundamentals = 'Having '
fun = get_fundamentals(fundamentals)
print('returned value', fun)
```
So here we pass an argument, and then add another string to our `fundamentals` variable and re-assign the combined strings back to `fundamentals`.

We can also use for loops in a functions.
```python
slab = ['Zoe', 'Shane', 'Brandon']

def get_person(people):
    for person in people:
        print('person', person)
    return people

get_person(slab)
```
Here we're passing in the list of `slab`. Notice we call the argument we're passing `people`. Arguments can be named anything independent of the variables you pass into the function. Then we loop through the list, print out each person, and return the list unchanged.

Here's a great tutorial on functions if you have time[https://www.datacamp.com/community/tutorials/functions-python-tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial).
