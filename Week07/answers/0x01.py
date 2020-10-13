import csv

class Dog:
    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed

    def speak(self):
        print("Bork bork! I'm", self.name)

def dogs_to_csv(dogs, filename):
    with open(filename, mode="w") as outfile:
        # since we don't have a ready-to-go dictionary with the keys defined,
        # we'll just have to manually define our column names (or not if we want to just fly blind) 
        fieldnames = ["name","owner","breed"] 
        writer = csv.writer(outfile) # create the new CSV writer that is attached to our output file object
        writer.writerow(fieldnames) # use the csv writer to write the field names
        for dog in dogs: # for every dog...
            writer.writerow([dog.name,dog.owner,dog.breed]) # write the dog's data to a row

def csv_to_dogs(filename):
    dogs = [] # create a new list that will hold all the Dogs
    with open(filename, mode="r") as infile:
        dogreader = csv.DictReader(infile) # create a new csv DictReader to read the csv
        # We can use the DictReader because we took the time to write the column names
        # without them, we'd have to rely on a normal csv reader and hope that our columns are ordered correctly
        for dog in dogreader: # for each dog that we read (well, for each row of the CSV)...
            dogs.append(Dog(dog["name"],dog["owner"],dog["breed"]))
            # create a new Dog by calling the Dog constructor
            # using the three variables that Dog stores. 
        return dogs # return the list


hazel = Dog("Hazel", "Shane", "Beagle")
maple = Dog("Maple", "Amanda", "Hound")
bofur = Dog("Bofur", "Ronda", "Corgi")
dogs = [hazel, maple, bofur]

dogs_to_csv(dogs, "dogs.csv")
dogs2 = csv_to_dogs("dogs.csv")
for dog in dogs2:
    dog.speak()
