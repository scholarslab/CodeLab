# Python Dictionary

## Setup
Make a directory in your workspace, `cd` into it, and create a file called `slab_dict.py`

```
mkdir -p ~/workspace/python/exercises
cd exercises
touch slab_dict.py
```

## References

* [Python dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)
* [Learn Python - Dictionaries](https://www.learnpython.org/en/Dictionaries)
* [Introducing Dictionries](http://www.diveintopython.net/native_data_types/index.html#odbchelper.dict)


## Instructions

In the Scholars' Lab, each employee has a title. We can store that information in a dictionary.

##### Example

```python
slab_staff = { 'Zoe_LeBlanc':'DH_Developer' ,
 'Jeremy_Boggs':'Head_RnD', 'Brandon_Walsh' :'Head_GradPrograms' }
```

We can print out each person's title by using either bracket notation
```python
print(slab_staff['Zoe_LeBlanc'])
```
or dot notation.
```python
print(slab_staff.Zoe_LeBlanc)
```

##### Try this
1. Try creating a dictionary with all your fellow praxis student names and departments. 
2. Then try using bracket or dot notation to print out their department. 