# Week 7: Class is in Session
![bart_class dot gif](assets/bart_class.gif)

## Agenda:
- Review Homework
- [Let's talk about classes!](lesson.md)
- [Importance of Import](lesson.md)
- Next week's homework

## Homework

Sorry about the delay; let's leave this week light.

Classes are useful ways to encapsulate data. In the lesson document, we created a new class named Dog, created a constructor that defined some data fields about dogs, and a method that borks out some dog talk. For this assignment, let's define an DogOwner class that contains some dogs to try out ways that classes can interact with each other.

#### Assignment Part 0:

Let's create the base class code. Create a DogOwner class that contains a name and a constructor to populate that name.

```python
class DogOwner:
  def __init__(self,name):
    #set the name of the DogOwner

shane = DogOwner("Shane")
```

#### Assignment Part 1:

Add a list to keep track of the owner's dogs to the class. You can copy and paste the Dog class definition from the lesson document. In your constructor code, be sure to set all the owners in the list of Dogs to the name of the DogOwner.

```python
class Dog:
  #copy from lesson doc

class DogOwner:
  def __init__(self,name,dogs):
    self.name = name
    # set DogOwner's dogs list
    for dog in dogs:
      #set each of the dogs' owners to the name of the DogOwner

hazel = Dog("Hazel","Beagle","NotShane",["treats","naps","raccoons"],["thunder"])
shane = DogOwner("Shane",[hazel])
print(hazel.owner) #Should be 'Shane'
```

#### Assignment Part 2:

Now, let's make things interesting. Write a function to rate the compatibility of dogs based on their likes and dislikes. For every shared like and dislike, add one point to the compatibility score. For every like that appears in another dog's dislike list, subtract one point.

We can use nested loops to make these comparisons, but we can also just use a single loop and the python keyword `in` (e.g. `if element in list:`).

```python
class Dog:
  #copy from lesson doc

def dog_compatibility(dog1,dog2):
  compatibility = 0
  # your code here
  return compatibility

hazel = Dog("Hazel","Beagle","Shane",["treats","naps","raccoons"],["thunder"])
maple = Dog("Maple","Hound","Amanda",["treats","zooms","ducks"],["thunder"])

print(dog_compatibility(hazel,maple)) #Should be 2, because they both like treats and dislike thunder
```

#### Assignment Part Bonus:

This part is a bonus assignment (yay?), but it isn't anything strictly new. Let's make things *really* interesting. Let's write a function that takes two DogOwners and returns the most and least compatible Dogs.

```python
class Dog:
  #copy from lesson doc

class DogOwner:
  def __init__(self,name,dogs):
    self.name = name
    self.dogs = dogs
    for dog in dogs:
      dog.owner = self.name

def dog_compatibility(owner1,owner2):
  #your code here
```

We can form the basic comparison logic by using two loops to loop through all pairings of dogs for each owner:
```python
  for dog1 in owner1.dogs:
    for dog2 in owner2.dogs:
      #your code here
```

To figure out the most and least compatible pairs, we don't need to actually sort them, we can just keep track of score of the two most and least compatible pairs.
