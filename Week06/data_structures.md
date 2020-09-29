# Data Structures Review

### Lists
If you need a refresher, check out the [resources](data_structures_resources.md).

1. How do we create a list?

1. What can we store in a list?

1. How do we get the first item, last item, and first three items to output from a list?

1. How can we arrange a list alphabetically? (**hint: search for python's built-in method for manipulating lists**)

1. How can we check what types of data are in our list? (**hint: search for python's built-in method for checking types**, also read up on data types in the [data types folder](../data_types/))

1. How can we replace a value in our list with another value?

*Lists are great. But what if we wanted to store information not just in a sequence, but in a way that let's us keep certain values together?*

### Dictionaries
We can use a *dictionary*, which is a collection of key/value pairs to store this information. When defining in place, keys and values are separated by a colon.

```python
shane = { 'name': 'Shane Lin', 'DH methods': ['programming', 'dog petting']}
```
To access our values in dictionaries, we don't use indexing. Instead, we use the keys of dictionary. Keys are always the values that come before the colon.
```python
shane['DH method']
```

We write the key inside of brackets and quotations, called *bracket notation*. 

How do we add a new key/value pair to a dictionary?

How do we change the value for an existing key in a dictionary?

In a dictionary, *keys must be unique!*

Just like lists though we can store a dictionary inside of other data structures, like another dictionary or a list.

```python
shane = { 'name': 'Shane Lin', 'DH methods': ['programming', 'dog petting']}
brandon = { 'name': 'Brandon Walsh', 'DH methods': ['programming', 'innovative pedagogy', 'neoliberalism']}
slab_staff = [shane,brandon]
```

How can we loop through each of Brandon's DH methods?

Just like lists there are many ways to manipulate dictionaries: [Python dictionary reference](https://www.w3schools.com/python/python_ref_dictionary.asp)


### For Loops and dictionaries

**For Loops** are one of the most common ways in python to loop over a sequence. We've already used for loops in lists before, like this:
```python
slab = ['Amanda', 'Shane', 'Brandon']

for person in scholars_lab:
    print(person) # This should print out each person's name individually
```

We can also use For Loops on dictionaries. The syntax is slightly different because dictionaries are not one long sequence, but rather a sequence of key/value pairs.
```python
shane = { 'name': 'Shane Lin', 'DH methods': ['programming', 'dog petting']}
brandon = { 'name': 'Brandon Walsh', 'DH methods': ['programming', 'innovative pedagogy', 'neoliberalism']}
amanda = { 'name': 'Amanda Visconti', 'DH methods': ['leadership', 'quiet nobility', 'toilet humor']}

scholars_lab = {"boss":amanda, "programmer": shane, "pedagog":brandon}

for key, value in scholars_lab.items():
    print('key', key)
    print('value', value)
```

This script should print out each of the employee keys and then the dictionaries those keys contain.