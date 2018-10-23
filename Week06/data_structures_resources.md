### Data Structures
Some of this information is overview from week 2, so check out that folder as well.

#### Lists

A list is an unordered, comma-separated collection of any values. So we can store any combination of values in our list.
```python
names = ['Hermione', 'Harry', 'Ron', 42]
```
We can also store a list inside of another list.
```python
names = ['Hermione', 'Harry', 'Ron', 42, ['UVA', 'W&L']]
```
What if you want to just print out 'Hermione' from the list? We can do that by *indexing* the list. 
```python3
names[0]
```
Each list in Python is a sequence, and we can access the position of an item in that sequence through indexing. **In Python, indexes always start at zero!**

We can use indexing in all sorts of ways.
1. We can take the final item by using negative one, which tells python to get the last item from the list
```python3
names[-1]
```
1. We can take a range of items by using a colon to specify when we want to start and stop
```python3
names[1:3]
```
1. If we try to index longer than the list, we'll get an error that tells us we're out of range of the list
```python3
names[8]
```

Now what if we wanted to add a Hogwarts classes to our list? We could create a new list that contained the classes and then use concatenation to join them.
```python3
classes = ['Defense Against The Dark Arts', 'Potions']
names + classes
```
We can see that we now have a list containing both lists, but what happens if you type names again?
![https://media.giphy.com/media/80TEu4wOBdPLG/giphy.gif](https://media.giphy.com/media/80TEu4wOBdPLG/giphy.gif)

Remember to store values, we need to *assign* them to variables.
```python3
classes = ['Defense Against The Dark Arts', 'Potions']
new_list =names + classes
```

We can also add items and remove them from the list. Let's take a look at some of these methods [https://www.w3schools.com/python/python_ref_list.asp](https://www.w3schools.com/python/python_ref_list.asp). You can read more about them in the python documentation [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

Lists are great. But what if we wanted to store information not just in a sequence, but in a way that let's us keep certain values together?

#### Dictionaries
We can use a *dictionary*, which is a collection of key/value pairs to store this information. Keys and values are always separated by a colon.

```python3
witch = { 'name': 'Hermione', 'age': 18}
```
To access our values in dictionaries, we don't use indexing. Instead, we use the keys of dictionary. Keys are always the values that come before the colon.
```python3
witch['name']
```
We write the key inside of brackets and quotations, called *bracket notation*. 

What happens if we add another name to the dictionary?
```python
witch = { 'name': 'Hermione', 'age': 18, 'name': 'Harry'}
```
Where's hermione??

![https://media.giphy.com/media/OUwzqE4ZOk5Bm/giphy.gif](https://media.giphy.com/media/OUwzqE4ZOk5Bm/giphy.gif)

Hermione was overwritten in our dictionary because our new value shared the same key. In a dictionary, keys must be unique!

Just like lists though we can store a dictionary inside of a dictionary
```python
hogwarts = {
    'student_1': {
        'name':'Hermione'
    },
    'student_2': {
        'name':'Harry',
        'age':19
    },
}
```
Now we can get Hermione's name if we type `hogwarts['student_1']['name']`. What's happening here is that we're using the keys to find our value that's nested inside a dictionary within a dictionary.

We can add Hermione's age by using a similar notation:
```python3
hogwarts['student_1']['age'] = 18
```
Just like lists there are many ways to manipulate dictionaries
[https://www.w3schools.com/python/python_ref_dictionary.asp](https://www.w3schools.com/python/python_ref_dictionary.asp)


[https://media.giphy.com/media/F6MFG8PHtQ2qs/giphy.gif](https://media.giphy.com/media/F6MFG8PHtQ2qs/giphy.gif)

You can also get even crazier and store lists in dictionaries:
```python
hogwarts = {
    'student_1': {
        'name':'Hermione',
        'classes':['Defense Against The Dark Arts', 'Potions']
    },
    'student_2': {
        'name':'Harry',
        'age':19
    },
}
```
Notice that the list is a value of a key, in this case `classes`. You can only insert a list into a dictionary as a value.

You can also put dictionaries inside of lists:
```python
students_hogwarts = [
    {
        'name':'Hermione',
        'classes':['Defense Against The Dark Arts', 'Potions']
    },{
        'name':'Harry',
        'age':19
    }
]
```
Notice that we now don't have keys for our top-most dictionaries. In lists, items don't have keys so each of your dictionaries is without an explicit key.

Python defaults to indexing each dictionary with numbers, just like in our list of strings. So to get the first value, you would type:
```python
students_hogwarts[0]
```
