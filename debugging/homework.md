# Assignment 1:

I think Brandon said that he was going to cover dictionaries... right? Dictionaries are really useful, so let's do a bit of practice with them.

If Brandon didn't talk about them, you can read the [Python docs about them](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). The example code they have there with the phone book is a good way to think about them.

Let's break this up assignment into smaller steps.

### Assignment 1A
For the first part, make a dictionary that maps the name of Praxis fellows in a cohort (that's you all) to their departments. So, if it were my cohort, it would be something like:

```python
praxis2012 = {}
#your code here
print(praxis2012["Shane"]) # should print "History"
print(praxis2012["Brandon"]) # "English"
```

### Assignment 1B
Now that we have that dictionary, let's programatically print out the list of all the fellows and their majors.

Here's a hint. We've been looping through all the items in a `list` like this:

```python
dogs = ["Hazel", "Maple", "Bofur", "Fat Dog"]
for dog in dogs:
   print(dog)
```

This just loops through each of the dogs and prints their name. What happens if we try this same looping code with a dictionary instead of a list?

### Assignment 1C

Good, good. Dictionaries are designed to be used to look up a value given a key. They're not really supposed to be used to go the other way. But sometimes we can't anticipate what we need our data to do. Let's flip it around.

We already have a dictionary of the fellows and their departments. Now, write a function that takes in that dictionary and a department and prints out all the fellows from that department.

So, something like this:

```python
def fellows_in_department(cohort, department):
   #your code here

praxis2012 = {"Brandon":"English", "Shane":"History", "Cecilia":"History", "Gwen": "Philosophy", "Chris":"Music", "Claire":"Sociology"}

fellows_in_department(praxis2012,"History") #should print "Shane" and then "Cecilia"
```

### Assignment 1D

Okay, last part! Let's put everything together now. Write a function that takes in a dictionary and then reverses it.

There's a problem right off the bat here - keys are unique. Keys map to a single value, though that value can contain many different pieces of data, like a list. Multiple keys can map to equivalent values. 

So, in the example of Praxis 2012, we only have room for one key that's Brandon. If there were two fellows named Brandon, we'd have to figure out a different way to organize the two of them (by naming one as "Brandon 1" and the other as "Brandon 2", for example). Otherwise, one Brandon would override the other. Just like in the wild.

Meanwhile, both Shane and Cecilia are in the history department and that's okay because "History" is a value and that's totally fine.

So, if we want to write a function to reverse the dictionary, we'll have to deal with this. I'm going to leave it up to you guys to figure out how!

```python
def reverse_dict(cohort):
   #your code here
   return reversed

praxis2012 = {"Brandon":"English", "Shane":"History", "Cecilia":"History", "Gwen": "Philosophy", "Chris":"Music", "Claire":"Sociology"}

sixarp2012 = reverse_dict(praxis2012)
print(sixarp2012["English"]) # Should print "Brandon"
print(sixarp2012["History"]) # Should print ???
```

