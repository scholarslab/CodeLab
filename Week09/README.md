# Week 09
![Tacoma Narrows GIF](assets/structure.gif)

## Agenda
- Review homework (for real this time)
- [Structuring Data](lesson.md) 

## Assignment

### Part 0x00
Okay, so maybe the Week 5 homework was too hard. I added [the answers to the repo just now for parts 2 and Bonus](https://github.com/scholarslab/CodeLab/tree/master/Week05/answers) to help set this assignment up. I think the answer to the bonus assignment will be useful as a foundation to this part. 

Read in the [same project Gutenberg text file of Much Ado About Nothing we used in Week 05](http://www.gutenberg.org/ebooks/1519) in Python. Separate all the lines of dialog and turn each into a dictionary with "role" and "dialog" as the keys. For example, we want to isolate a line of dialog such as:

```
BEATRICE.
I wonder that you will still be talking, Signior Benedick:
nobody marks you.
```

And then turn it into a Python dictionary like this:

```python
{"role":"BEATRICE","dialog":"I wonder that you will still be talking, Signior Benedick:nobody marks you."}
```

Collect every line of dialog in the play into a list of dictionaries and use the Python json module to dump it into a json file.


### Part 0x01
Let's write a bit of code to turn a list of Dog objects into a CSV file and then create a new list of Dog objects by reading the file back.

So, we start with our basic Dog class:

```python
class Dog:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed
    
    def speak(self):
        print("Bork bork! I'm",self.name)
```

Now, let's write two functions, one to dump a list of dogs into a csv file and one to load that file back into a list of dog.

```python
import csv
class Dog:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed
    
    def speak(self):
        print("Bork bork! I'm",self.name)

def dogs_to_csv(dogs,filename):
    with open(filename,mode="w") as outfile:
        # your code here

def csv_to_dogs(filename):
    dogs = []
    with open(filename,mode="r") as infile:
        #your code here
        return dogs

hazel = Dog("Hazel","Shane","Beagle")
maple = Dog("Maple","Amanda","Hound")
bofur = Dog("Bofur","Ronda","Corgi")
dogs = [hazel,maple,bofur]

dogs_to_csv(dogs,"dogs.csv")
dogs2 = csv_to_dogs("dogs.csv")
for dog in dogs2:
    print(dog.speak())
```