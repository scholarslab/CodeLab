# Week 5
![function dot gif](assets/function.gif)
![racoon_highfive dot gif](assets/racoon_highfive.gif)

## Outline
1. Discuss homework assignments
2. Review Git
3. Functions
4. Classes
5. Let's put it all together

## Functions

We've already used many of Python's [built-in functions](https://docs.python.org/3/library/functions.html) and some others in Python's standard library, such as in String and Random. A fundamental part of most programming languages is the ability to define your own functions so we can reuse code that we (or others) have already written.

Let's take a look:

```python
def overlords(name):
  print("I, for one, hail our new " + name + " overlords.")
# These two lines just defined the function. Nothing happens yet.

for person in ["Catherine","Cho","Chris","Eleanore","Emily","Matilda"]:
    #This is a "function call" - now the code in overlords() is executed.
    overlords(person)
    
```

In this `overlords` function, `name` is a parameter, a variable that we "pass in" to the function that alters its behavior. Note that the definition (`def overlords(name)`) goes first. Think about how the interactive interpreter works - if you open it up and just type in `overlords()`, it wouldn't have any idea what you mean. Just like a variable, you have to define it first.

Functions can, in turn, also "return" values back to whatever called it. Let's change last week's fizzbuzz assignment to use a function (or multiple functions).

```python
# something something fizzbuzz()

for i in range(1,100):
  print(fizzbuzz(i))
```


## Classes

Even better, we can group data and functions together in convenient arrangements called classes. Here's a simple, *bad* example:

```python
class Staff:
    name = "Brandon"
    house = "Hufflepuff"

    def speak(self):
        print("It is I, "+self.name+" of House "+self.house+"!")

a = Staff()
a.speak()
```

This is a bad example because there's really no reason  A *class* is a particular type of objects. We can create ("instantiate") an object of a class and store it as a variable. A variable therefore contains (technically, contains a reference to) an *instance* of a class.

Let's look closer at this class. The function `speak` is attached to the class, so it's actually a method, which is pretty much the same as a function. But we can see that, as a method, it has a special parameter, `self`. This parameter doesn't appear in the method call later, but it allows the method to access the internal data stored inside of the class.

Let's keep that bad class definition for now, but let's play with it a bit.

```python
a = Staff()
b = Staff()
b.name = "Shane"
b.house = "Clearly Ravenclaw, Even Though For Some Reason Everyone Thinks I'm A Slytherin"
a.speak()
b.speak()
```

So, we can see that `a` and `b` both have their own sets of internal data, just like if they were any built-in type. But this is still not a very good class. For one thing, Brandon is some kind of prototypical Slab staffe and that's just poor software design. For another thing, we have to know how it works internally to know how to actually change its behavior. This gets really complicated the more complicated the code is.

Let's consider this: the built-in classes we've used are the same kind of classes as these, built in the same way (here is the internal python code for the familiar [Random class](https://github.com/python/cpython/blob/3.7/Lib/random.py)). We don't want to have people know all about text encoding works or how pseudorandom number generation works for them to use the string and random classes.

Ideally, we should make things easy to understand only using the public methods for a class. One important method is a "constructor". This is called whenever a class is instantiated. Let's revise our class using a constructor:

```python
class Staff:
    name = "Brandon"
    house = "Hufflepuff"

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def speak(self):
        print("It is I, "+self.name+" of House "+self.house+"!")
    
    def housemates_with(self, fellow):
        if self.house == fellow.house:
            return True
        else:
            return False

a = Staff("Brandon", "Hufflepuff")
b = Staff("Shane", "Slitherclaw")
a.speak()
b.speak()
print("Are these two in the same house?", a.housemates_with(b))
```

The method `__init__` (with two underscores on either side) is the constructor. It lets us fill in the details for a `Staff` right off the bat. We can add more methods to interact with this class as needed, such as the `housemates_with` method.

Designing classes in this way allows us to achieve a concept called *encapsulation*, which amounts to being able to use a class without knowing how it works. We don't need to know what variable `Staff` stores the house in or what format it's in or how to compare it. We just need to know that there is a method named `housemates_with` and what it does (presumably because we also have nicely documented this class because we're responsible coders). It also makes it easier for a larger project to be broken up into small blocks of code.


## Advanced Topics That We're So Obviously Not Going To Have Time to Talk About

[Don't read this. Seriously, it talks about a lot of things that we've glossed over. And, like, other programming languages that we've never, ever mentioned.](https://ericlippert.com/2014/01/02/what-is-duck-typing/comment-page-1/) (But it's actually really good.)

---
## Homework for Week 5

For the homework, let's put all of this together. In Git.

### Assignment 1: Fellowship Program

We're going to have all of you create code to keep track of a fellowship program. You're going to work in teams of three, but the trick to this assignment is that both teams are going to be working on the same file in the same repository. We'll start with the bare bones (which will run, but won't do what we want it to do) and then assign each team to a different class in the code.

Let's start with the basic skeleton, which I'll throw onto the Scholars' Lab Github:

```python

class Fellow:
    # Constructor. Name (in "firstname  lastname" format) and department are self-explanatory. Start_year is the year that the student started grad school.
    def __init__(self, name, department, start_year):
        pass
    # Get the student's name
    def get_name(self):
        return("Brandon Walsh")
    def get_department(self):
        return("English")
    # Returns how many years the fellow has spent in their program (1 = "first year", etc) using the current, actual date. If the fellow has graduated, return how many years it took to graduate.
    def get_year(self):
        return(6)
    # Get the current status of the fellow. Fellows all start as "student", but can eventually become a "graduate". Let's not mention the third possibility.
    def get_status(self):
        return("student")
    # Sets the status of the student to "graduate" and caps get_year at a certain value
    def set_graduate(self, year):
        pass
    # Invent a secret algorithm to based on some combination of the fellow's data (number of vowels in name, heiarchy of departments, etc) to generate a secret rating from 0-10 for a fellow. Be creative.
    def get_rating(self):
        return(10)
    # Return a string representing all the data for a student in as a single row of a CSV file.
    def printout(self):
        return("Brandon Walsh, English, etc, etc, etc")
    # Compare two fellows. If they have all the same data, return true.
    def equals(self,f):
        return(False)
    
    
class Fellowship:
    # Name is the name of the fellowship
    def __init__(self, name):
        pass
    # Audit the program to check that there's been a cohort of 6 students every year and that no person appears multiple times in each cohort. Return True if the fellowship passes, False if it fails.
    def audit(self):
        return(True)
    #Add fellow f to the fellowship in the cohort for year year. 
    def add_fellow(self, f, year):
        pass
    # Return all the fellows for a particular year's cohort in a list. Figure out what to return if the cohort doesn't exist.
    def get_cohort(self, year):
        return([])
    # Return the total rating for a cohort (add up all the students' individual ratings)
    def get_cohort_rating(self,year):
        return(9)
    # Return the best cohort or cohorts
    def get_best_cohort(self):
        return([2012])
    # Return the cohort or cohorts with fellows from the most number of departments
    def get_most_diverse(self):
        return([2012])
    # Return the cohort or cohorts with fellows from the least number of departments
    def get_most_diverse(self):
        return([2011])
    # Return the department whose students are most frequently chosen
    def get_top_department(self):
        return("Music")
    # Write the data for all the students to a CSV file using the filename parameter
    def write_to_file(self,filename):
        pass

praxis = Fellowship("Praxis")
praxis.add_fellow(Fellow("Brandon Walsh","English",2011), 2012)
print(praxis.get_cohort(2012))
print(praxis.get_cohort_rating(2012))
print(praxis.audit())
```

One team, let's call it Team One, will fill in the methods and data in the Fellow class. The other team, Team Alpha, will fill in the methods and data for the Fellowship class. At the end of the day, we should be able to fill it in with real historical from the Praxis Program and figure out which cohort is the most diverse and also which cohort was the best.

### Assignment 2: Manual Addition Edition

Same teams, but this time it's separate code.

Fill in the methods in this class to perform addition with two classes constructed using a list of single-digit numbers that represent potentially large numbers.

```python
class BigNumber:
    # "big" is a list of integers representing a single-digit number. So, [9,5,1] represents the number 951. This can be a very big number.
    def __init__(self, big):
        pass
    # Add self to another BigNumber and return a new BigNumber representing the sum. 
    def add(self,bn):
        return(BigNumber([0]))
    
    # Prints the BigNumber's value
    def print_value(self):
        print("x")

a = BigNumber([1,1,1])
b = BigNumber([2,3,4])
c = a.add(b)
# In this example, should print out "345"
c.print_value()
```

Manually add each integer in the list - don't try to convert the list to a regular number.