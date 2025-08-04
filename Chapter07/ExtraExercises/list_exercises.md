# Python Lists

## Setup
Make a directory in your workspace, `cd` into it, and create a file called `slab_list.py`

```
mkdir -p ~/workspace/python/exercises
cd exercises
touch slab_list.py
```

## Reference

* [Python Lists](https://docs.python.org/3.6/tutorial/datastructures.html)
* [Learn Python - Lists](http://www.learnpython.org/en/Lists)


## Instructions

In the Scholars' Lab, we offer instruction in many sub-fields of DH. We can store our offerings in a list

##### Example

```python
slab_specialties = ['mapping', 'makerspace', 'text_analysis', '3D_printing', 'VR_AR', 'computer_vision', 'machine_learning', 'programming' ]
```

We can print out each type of specialty by using the index of the list
```python
print(slab_specialties[0])
```
We can get the final value of the list by using the index `-1`
```python
print(slab_specialties[-1])
```
We can get a range of items in the list by using `:` to specify the range. In this example we should get the first two items.
```python
print(slab_specialties[0:2])
```
Finally we can figure out how long are list is by using the built in function `len()`, which should be 7.
```python
print(len(slab_specialties))
```

*REMEBER: when indexing a list, the first index is always zero!!! *

##### Try this
1. Try printing out the above examples and changing the index number. (** hint: if you get an index out of range error, you might have used a number greater than the number of items in the list **)
2. Then try creating your own list of your research interests, and then try using indexes to print out each one. 
