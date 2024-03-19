# Working with Structured Data

## Data Structures

![Hazel snoozing](assets/hazel_snooze.jpg)

We've been using the various fundamental data types in Python for a few weeks now. These are called "basic" or sometimes "primitive" types in computing. In Python, these include integers (whole numbers), floats (floating point numbers, which represent real numbers--"the ones between integers"), strings (text), and booleans (`True` and `False`). You should have a good sense by now of how each of these work (even though floats are weird).

We've also seen how we can use these basic data types to encode information in some more specific contexts, such as using a string to represent color in RGB hex format: "#FFFFFF" for white, "#000000" for black, "#588eb8" for roughly the shade of my bathroom ("Lovebirds" from Lowes). Going one level above this is the concept of a *data structure*. The word structure here is a useful analogy for this relationship: we can think of basic types as being the bricks (fundamental, atomic components) that can be arranged in a particular pattern to make up a larger structure. Sometimes we refer to these as *complex* or *composite* to distinguish them from the basic types.

Abstractly, structure helps us organize information as data in order to help us efficiently access and manipulate that information. In Python, we've already been using composite structures in the form of lists, which provides structure in the form of linear order (there's a contiguous line of objects, each with a unique place in that line). We'll learn about dictionaries today, which provides a different structure. Both dictionaries and lists can contain any object, including any composite types. We've worked with lists of lists already, but we can also put, as an example, lists into dictionaries. There are a few other composite types which are built into Python, but we can also create our own.

Incidentally, because lists can contain any object, you can do funny things in Python like *append a list to itself*.

```python
a = [1,2,3]
a.append(a)
print(a)
print(a[3])
print(a[3][3])
```

### Dictionaries

A Python Dictionary associates specific pieces of data to other pieces, much like a physical dictionary associates a word to a definition or a phone book associates a name to a phone number (ed. note: phone books are historical artifacts that provided listings of telephone numbers as an intermediate technology between human operators and the popularization of the internet). In programming, we say that a dictionary *maps* a *key* to a *value* and that it contains *key-value pairs*. 

In Python, a dictionary is a collection of one-to-one key-value pairs, so that one key maps to exactly one value. However, multiple keys can map to the same value. Think of a phone book where a phone number can belong to only one person, but one person can have multiple phone numbers. "But," you object, "what about an actual dictionary, where a word can have multiple definitions?" And the answer is: a list with multiple definitions is still a single value. We just have to be explicit about it.

And yes, you can have a dictionary assign itself as a value. But dictionaries as a type are not allowed to be keys. Actually, keys must be hashable objects, which I'm not going to get into right now. For the most part, it means that keys should be basic objects.

Dictionaries are defined using curly braces, but they're addressed like lists. You can even use integers as keys, just like the index to a list. However, there is no provision for index continuity (i.e. list indices don't skip numbers, but dictionary keys can be whatever you want).

```python
d = {} # create an empty dictionary
d[1] = 5 # assign the value 5 to the key 1
d[3] = "b" # assign the value "b" to the key 3
d["a"] = [1,2,3] # assign the value [5] to the key "a"
print(d)
```

As we can see, you can mix and match different types of values like for lists. And we can also mix and match different types of keys.

We can also define a dictionary using curly braces and then listing key-value pairs, separating the two with a colon. This code is equivalent to the above.

```python
d = {1:5, 3:"b","a":[1,2,3]} # create a not-empty dictionary
print(d)
```

As with lists, we can traverse dictionaries using for loops:

```python
dogs = {"Shane":"Rocky", "Amanda":"Maple", "Laura":"Triscuit"}
for owner in dogs:
    print(owner+"'s dog is "+dogs[owner])
```

Here, we see that using for loops through all the keys in a dictionary. We can actually get a hold of the list of keys for this dictionary with `dogs.keys()` and a list of the values for this dictionary with `dogs.values()`. Some people prefer this convention that grabs key and value in a for loop:

```python
dogs = {"Shane":"Rocky", "Amanda":"Maple", "Laura":"Triscuit"}
for owner,dog in dogs.items():
    print(owner+"'s dog is "+dog)
```

Dictionaries are unordered, so while this example (probably) loops through the order in which I constructed the dictionary, that isn't guaranteed.


### More file access

![Maple and Jeremy](assets/maple_jerm.jpg)

We covered some basic file input and output in Python last week. It's pretty easy to work with text data, either all at once or line by line.

To review, we can read some text from a file like so:

```python
infile = open('file.txt', "r")
text = infile.read()
infile.close()
```

or, equivalently, using the with-open-as idiom:
```python
with open('file.txt', "r") as infile:
    text = infile.read()
```

We can write back to files just as easily, opening a file in `"w"` (write) mode and using the `write()` method:
```python
outfile = open('file.txt', "w")
outfile.write("Hello Dog!")
outfile.close()
```

This is fine enough for simple data, but how do we read and write composite data to a file?

Let's step back and take a closer look at reading and writing basic data. Recall that when we use the `read()` method on a file object like we did above, the data that we get back is a string. So, if we had a file named file.text that just contained the number `12345`, we'll get back the string "12345" rather than the integer 12345.

```python
with open('file.txt', "r") as infile:
    text = infile.read()
    text += 43210 #this line results in "TypeError: must be str, not int"
```

The "12345" in the text file is, after all, text. Underneath it all, it's being represented by a text encoding, which means that if you look under the hood, "12345" isn't actually 12345. These days, this kind of text is usually UTF-8/ASCII encoded numbers, which means "12345" is actually 049 050 051 052 053. To turn the text "12345" into the number 12345 in Python, we have to explicity tell Python to make this conversion.

```python
with open('file.txt', "r") as infile:
    text = infile.read()
    number = int(text)
    number += 43210 #this works just fine now
```

Here, we're calling the integer constructor method that takes in a string argument and builds us a new integer object based on that string.

I bring this up to suggest that there's difference between the static text representation of an object and the "live" Python objects that live in computer memory and can be manipulated. Python objects are useful because we can easily manipulate them, but they don't persist beyond the lifespan of a program. Static files persist data, but have to be read and interpreted explicitly in the way that we want them to be. 

## Let's review data formats

So, strings and even numbers are simple enough. How do we represent, say, a list of things in a file?

We talked about this way back, so let's just review it again. A really simple way to do this is to just write them out as a sequence, separated by some delimiter. Following English convention, let's use commas. An easy way to do this in Python is to use the string method `join()`, which is kind of like a reverse split. It lets you join together a list of strings with a delimiter (you can also just mush together the list of strings if you call it on an empty string).

```python
dogs1 = ["Rocky", "Maple", "Bofur"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dogs1))
with open('file.txt', "r") as infile:
    text = infile.read()
dogs2 = text.split(",")
print(dogs1 == dogs2)
```

So, we can see that (hopefully) the two dogs lists are the same. This is easy enough for simple data, but we can probably see that there are some complications here...

```python
dogs1 = ["Rocky, the wary", "Maple Stilt-Legs", "Bofur, Boss of the Lab"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dogs1))
with open('file.txt', "r") as infile:
    text = infile.read()
dogs2 = text.split(",")
print(dogs1 == dogs2)
```

So, there's one basic problem with using text to store structured text. Whatever delimiters or special characters we use to indicate the structure of the data can also exist in the data itself. ASCII, the archaic way of encoding text, solved this by setting aside special non-text characters. There were characters for things like "Start of Heading", "End of Transmission", "Acknowledgement", and even "Bell" to get a computer operator's attention. These days, that method is hopelessly outmoded, not just because we want to be have more flexibility in the ways that we define our structures.

So how do we get by this? We can wrap individual elements in quotes and that works well enough if we don't also use quotes. We can also use escape characters to tell Python when we do and don't mean business. An escape character is just a character that means "interpret the next thing as text, without any special meaning." Although, annoyingly, sometimes it means "interpret the next thing as a special thing and not just as regular text." Commonly, many systems use the backslash (`\`) as an escape character. This works when we define a string in Python, for example:

```python
 text = "here are some quotation marks inside of a string: \"\'\'\""
 print(text)
```

But all these rules are starting to add up. It's getting kind of complicated. We don't want to spend our time writing out the special logic to distinguish between real quotations marks and commas and fake ones. And what if we didn't think of some nonobvious, uncommon edge case? Happily, this whole exercise is a pretty common problem and there are a few standard ways to do it.

We can impart supertextual meaning to text data (like the structure of a list) using data formats, which are standard ways to write out and read data, that typically have standard software tools to accomplish those tasks.

## CSV

One of the simplest data formats is CSV, which stands for, simply enough, Comma Separated Values. This is what we've actually just talked through. Strangely enough, it doesn't actually have to be commas that do the separating. Typically, we can choose our own delimiter. CSVs are used for tabular data and is a commonly used to exchange data between different spreadsheet applications or to produce data that is easily ingested by those applications. In a CSV, each column entry is separated by the delimiter and each new line contains a new row.

Let's try out a simple example with some familiar data.

![Hazel again](assets/hazel3.jpg)

```python
rocky = ["Rocky","Shane","Texas Heeler"]
maple = ["Maple", "Amanda", "Hound"]
bofur = ["Bofur", "Ronda", "Corgi"]
dogs = [rocky,maple,bofur]

with open('dogs.csv', "w") as outfile:
    outfile.write(",".join(["Dog","Owner","Breed"]))
    for dog in dogs:
        outfile.write("\n"+",".join(dog))
```

If you want, you can import that into your preferred spreadsheet application to to see what comes out.

But this still leaves us with the problem of how to handle tricky data. Since CSV is so widely used, there is actually a [built-in Python module](https://docs.python.org/3/library/csv.html) to handle it. If we haven't talked in depth about imports yet because I moved the weeks around, recall that we've used Python's built-in `random` module before to generate random numbers. Modules are just bits of extra code that we can bring in ("import") to use in our own.

We just create a file object with `open()` like before, but we pass that file object into a special CSV writer.

Let's try it out.

```python
import csv

rocky = ["Rocky, the Wary","Shane","Beagle/Heeler"]
maple = ["Maple, the Swift", "Amanda", "Hound"]
bofur = ["Bofur, the Brave", "Ronda", "Corgi"]
dogs = [rocky,maple,bofur]

with open('dogs.csv', 'w', newline='') as csvfile:
    dogwriter = csv.writer(csvfile, delimiter=',')
    dogwriter.writerow(["Dog","Owner","Breed"])
    for dog in dogs:
        dogwriter.writerow(dog)
```

Which produces the output csv file...

```csv
Dog,Owner,Breed
"Rocky, the Wary",Shane,Beagle/Heeler
"Maple, the Swift",Amanda,Hound
"Bofur, the Brave",Ronda,Corgi
```

Easy!

Actually, this is still a little too much work. We have to manually define headers and make sure that everything is in the right order. What if we didn't even have to do that?

If start with a dictionary instead of a list, we have a way to associate values with keys rather than just depending on their indices. We can use the `DictWriter` class inside of the csv module to automatically take care of things for us.

```python
import csv

rocky = {"name":"Rocky","owner":"Shane","breed":"Texas Heeler"}
maple = {"name": "Maple", "owner":"Amanda", "breed": "Hound"}
bofur = {"name": "Bofur", "owner":"Ronda", "breed": "Corgi"}

with open('dogs.csv', 'w', newline='') as csvfile:
    fieldnames = rocky.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(rocky)
    writer.writerow(maple)
    writer.writerow(bofur)
```

This produces the same kind of CSV file. Note that the field names are consistent, so I just used the keys for Rocky. We'd have to do this a bit differently if the data wasn't structured homogenously.

To read CSV files, we can use analogous Reader and DictReader objects in the csv module:

```python
import csv

with open('dogs.csv', newline='') as csvfile:
    dogreader = csv.DictReader(csvfile)
    for dog in dogreader:
        print(dog["name"],"and",dog["owner"])
```

### JSON

CSV is good for tabular data, but not great to encapsulate data with more complex relationships. Each of our Dogs has lists of things they like and dislike, for example. CSVs don't really support variable-length lists of things inside of rows. We can store our own format to store lists within a single CSV element, but that just puts us back at step one. And, I cannot emphasize this enough, storing different arbitrary text data formats inside of each other is a *real bad idea*. Don't do it. Oh my god, no, just don't do it.

One popular, good way to do this is JSON. Sometimes it's pronounced "Jay Song", but it's really "Jason". Like the Argonaut or the deli or [Robards](https://www.imdb.com/name/nm0001673/). JSON stands for "Javascript Object Notation" and was originally designed to allow websites to pass data back and forth between the browser and the server. But it's become a really popular generic format for all sorts of things and all sorts of languages.

For example, a lot of GIS data is available as GeoJSON, a JSON format with geographic-specific fields.

We don't have to go too much into the particular details of how JSON is structured. It's enough to just glance at what it looks like. Here's an example:

```json
[
  {
    "name": "Rocky",
    "owner": "Shane",
    "breed": "Texas Heeler",
    "likes": [
      "vocalizing",
      "eating disgusting garbage",
      "cats"
    ]
  },
  {
    "name": "Maple",
    "owner": "Amanda",
    "breed": "Hound",
    "likes": [
      "zoomies",
      "looking",
      "carrots"
    ]
  },
  {
    "name": "Bofur",
    "owner": "Ronda",
    "breed": "Corgi",
    "likes": [
      "the ladies"
    ]
  }
]
```

Happily, there is also an easy to use [JSON module for Python](https://docs.python.org/3/library/json.html).

One of the most useful mechanisms it provides is the ability to "dump" and "load" arbitrary built-in Python data structures into and out of JSON. It makes it super easy to throw a complex python object into a file and get it back out again.

There are `dump` and `load` methods, which write and read directly to files, but also `dumps` and `loads` methods which write and read to a string object. I like using the latter because it makes it easier to check them during debugging.

```python
import json

rocky = {"name": "Rocky", "owner": "Shane", "breed": "Texas Heeler",
         "likes": ["vocalizing", "eating disgusting garbage", "cats"]}
maple = {"name": "Maple", "owner":"Amanda", "breed": "Hound","likes":["zoomies","looking"]}
bofur = {"name": "Bofur", "owner":"Ronda", "breed": "Corgi","likes":["ladies"]}
dogs = [rocky,maple,bofur]

with open('dogs.json', mode="w") as jsonfile:
    jsonfile.write(json.dumps(dogs))

with open('dogs.json', mode="r") as jsonfile:
    dogs_load = json.loads(jsonfile.read())
    for dog in dogs_load:
        print(dog["name"],"and",dog["owner"])
```

## Other Data Formats

There are a ton of other text data formats. The other big one is SGML/XML/HTML, which are structurally similar and related. HTML is, of course, the language that websites are written in. We'll revisit that in the future when we talk about Web scraping and about building websites.

These are all different from binary data formats like the jpg and gif images that are peppered (Peppered? We should have more Pepper media) throughout these docs. That's a whole different kettle of fish.
