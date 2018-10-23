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
witch = 'Hermione'
if wizard != witch:
    print('well done')
else:
    print('nice try')
```

In this example, we're getting a bit more tricky.
Let's break it down with a simpler example.
```python
test1 = True
test2 = False
print(test1 == test2)
print(test1 != test2)
three = 3
four = 4
print(three < four)
print(four > three)
```

#### Functions
 Essentially functions are a way to wrap your code into blocks so that way you can call your code when you need it to run.

```python
def get_fundamentals():
    fundamentals = 'Having fun'
    print(fundamentals)
    return fundamentals

get_fundamentals()
```
![https://swcarpentry.github.io/swc-releases/2016.06/python-novice-inflammation/fig/python-function.svg](https://swcarpentry.github.io/swc-releases/2016.06/python-novice-inflammation/fig/python-function.svg)

Some more advanced examples:
```python
def new_costume(halloween_costumes):
    costumes = halloween_costumes + 'Black Panther'
    return costumes

updated_costumes = new_costume(halloween_costumes)
```

Combining everything together:
```python
def check_costumes(costumes):
    for costume in costumes:
        if costume == 'Black Panther':
            print("That's your costume " + costume)
        else:
            print("Back to the drawing board")
check_costumes(updated_costumes)
```

We don't have time to go into depth about functions, but here's a great tutorial [https://www.datacamp.com/community/tutorials/functions-python-tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial).
