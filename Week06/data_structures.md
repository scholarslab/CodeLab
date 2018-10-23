# Data Structures

You already know one data structure pretty well, so let's review it together.

### Lists
If you need a refresher, check out the [resources](data_structures_resources.md).

1. How do we create a list?

1. What can we store in a list?

1. How do we get the first item, last item, and first three items to output from a list?

1. How can we arrange a list alphabetically? (**hint: search for python's built-in method for manipulating lists**)

1. How can we check what types of data are in our list? (**hint: search for python's built-in method for checking types**, also read up on data types in the [data types folder](../data_types/))

1. How can we replace a value in our list with another value?

![https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/giphy.gif)

*Lists are great. But what if we wanted to store information not just in a sequence, but in a way that let's us keep certain values together?*

### Dictionaries
We can use a *dictionary*, which is a collection of key/value pairs to store this information. Keys and values are always separated by a colon.

```python
scholars_lab = { 'name': 'Zoe', 'DH_method': 'programming'}
```
To access our values in dictionaries, we don't use indexing. Instead, we use the keys of dictionary. Keys are always the values that come before the colon.
```python
scholars_lab['name']
```
We write the key inside of brackets and quotations, called *bracket notation*. 

What happens if we add another name to the dictionary?
```python
scholars_lab = { 'name': 'Zoe', 'DH_method': 'programming', 'name': 'Shane'}
```

![https://media.giphy.com/media/3oEjHKvjqt5pssL99C/giphy.gif](https://media.giphy.com/media/3oEjHKvjqt5pssL99C/giphy.gif)

Zoe was overwritten in our dictionary because our new value shared the same key. In a dictionary, *keys must be unique!*

Just like lists though we can store a dictionary inside of a dictionary, called *nesting*.
```python
scholars_lab = {
    'employee_1': {
        'name':'Zoe',
        'DH_method': 'gifs'
    },
    'employee_2': {
        'name':'Shane',
        'DH_method': 'programming_genius'
    },
}
```
Now we can get Shane's name if we type `scholars_lab['employee_2']['name']`. What's happening here is that we're using the keys to find our value that's nested inside a dictionary within a dictionary.

We can add Zoe's age by using a similar notation:
```python
scholars_lab['employee_1']['age'] = 132
```
Just like lists there are many ways to manipulate dictionaries
[https://www.w3schools.com/python/python_ref_dictionary.asp](https://www.w3schools.com/python/python_ref_dictionary.asp)



[https://media.giphy.com/media/F6MFG8PHtQ2qs/giphy.gif](https://media.giphy.com/media/F6MFG8PHtQ2qs/giphy.gif)

You can also get even crazier and store lists in dictionaries:
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
```
Notice that the list is a value of a key, in this case `DH_mthods`. You can only insert a list into a dictionary as a value, not as a key.

You can also put dictionaries inside of lists:
```python
slab = [
    {
        'name':'Zoe',
        'DH_methods': ['gifs', 'data visualization', 'web apps']
    },
    {
        'name':'Shane',
        'DH_methods': ['programming_genius', 'TEI']
    },
]
```
Notice that we now don't have keys for our top-most dictionaries. In lists, items don't have keys so each of your dictionaries is without an explicit key.

Python defaults to indexing each dictionary with numbers, just like in our list of strings. So to get the first value, you would type:
```python
slab[0]
```

### For Loops and dictionaries

**For Loops** are one of the most common ways in python to loop over a sequence. We've already used for loops in lists before, like this:
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

If you need a refresher on for loops, conditionals, or functions, check out the [resources in the data flow folder](data_flow_resources.md)


### TIME FOR WHITEBOARD EXERCISE
![https://media.giphy.com/media/F4bBD98zUOFX2/giphy.gif](https://media.giphy.com/media/F4bBD98zUOFX2/giphy.gif)

So far we've been having you code a lot, but sometimes the most helpful part of coding is writing out your logic before writing any code.

Try your best to break down this prompt and think about how you would create a script that might achieve all the goals. Remember there's no right answer in coding, just the answer that works!

[Whiteboard Exercise](whiteboard_exercise.md)

**Remember to check out the resources in the data flow folder if you need help remembering how for loops, functions, and conditionals work**