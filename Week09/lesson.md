# Structuring Data

![Maple and Jeremy](assets/maple_jerm.jpg)

We covered some basic file input and output in Python a few weeks ago. It's pretty easy to work with text data, either all at once or line by line.

To review, we can read some text from a file like so:

```python
infile = open('file.txt', "r"):
text = infile.read()
infile.close()
```

or, equivalently, using the with-open-as idiom:
```python
with open('file.txt', "r") as infile:
    text = infile.read()
```

and we can write back to files just as easily:
```python
outfile = open('file.txt', "w"):
outfile.write("Hello Dog!")
outfile.close()
```

(If you need a refresher, we learned all of this back in [Week 5](../Week05/lesson.md))

But while we've worked with simple text and numerical data like strings and ints plenty, we've also used lists and dictionaries and more structured data too. How do we read and write those more complicated kinds of data?

Let's revisit the way that we read in numbers. Recall that when we use the `read()` method on a file object like we did above, the data that we get back is a string. So, if we had a file named file.text that just contained the number `12345`, we'll get back the string "12345" rather than the integer 12345.

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

## Let's talk about Data Formats

So, strings and even numbers are simple enough. How do we represent, say, a list of things in a file?

A really simple way to do this is to just write them out as a list, separated by some delimiter. Following English convention, let's use commas. An easy way to do this in Python is to use the string method `join()`, which is kind of like a reverse split. It lets you join together a list of strings with a delimiter (you can also just mush together the list of strings if you call it on an empty string).

```python
dogs1 = ["Hazel", "Maple", "Bofur"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dogs))
with open('file.txt', "r") as infile:
    text = infile.read()
dogs2 = text.split(",")
print(dogs1 == dogs2)
```

So, we can see that (hopefully) the two dogs lists are the same. This is easy enough for simple data, but we can probably see that there are some complications here...

```python
dogs1 = ["Hazel, who is definitely Shane's dog", "Maple, the Stilt-Legged", "Bofur, Boss of the Lab"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dogs))
with open('file.txt', "r") as infile:
    text = infile.read()
dogs2 = text.split(",")
print(dogs1 == dogs2)
```

So, there's one basic problem with using text to store structured text. Whatever delimiters or special characters we use to indicate the structure of the data can also exist in the data itself. ASCII, the archaic way of encoding text, solved this by setting aside special non-text characters. There were characters for things like "Start of Heading", "End of Transmission", "Acknowledgement", and even "Bell" to get a computer operator's attention. These days, that method is hopelessly outmoded, not just because we want to be have more flexibility in the ways that we define our structures.

So how do we get by this? We can wrap individual elements in quotes and that works well enough if we don't also use quotes. We can also use escape characters to tell Python when we do and don't mean business. An escape character is just a character that means "interpret the next thing as text, without any special meaning." Although sometimes it means "interpret the next thing as a special thing and not just as regular text." Commonly, many systems use the backslash (`\`) as an escape character. This works when we define a string in Python, for example:

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
hazel = ["Hazel","Shane","Beagle"]
maple = ["Maple", "Amanda", "Hound"]
bofur = ["Bofur", "Ronda", "Corgi"]
dogs = [hazel,maple,bofur]

with open('dogs.csv', "w") as outfile:
    outfile.write(",".join(["Dog","Owner","Breed"]))
    for dog in dogs:
        outfile.write("\n"+",".join(dog))
```

If you want, you can import that into your preferred spreadsheet application to to see what comes out.

But this still leaves us with the problem of how to handle tricky data. Since CSV is so widely used, there is actually a [built-in Python module](https://docs.python.org/3/library/csv.html) to handle it. Let's try it out.

```python
import csv

hazel = ["Hazel, Shane's Dog","Shane","Beagle"]
maple = ["Maple, the Swift", "Amanda", "Hound"]
bofur = ["Bofur, the Brave", "Ronda", "Corgi"]
dogs = [hazel,maple,bofur]

with open('dogs.csv', 'w', newline='') as csvfile:
    dogwriter = csv.writer(csvfile, delimiter=',')
    dogwriter.writerow(["Dog","Owner","Breed"])
    for dog in dogs:
        dogwriter.writerow(dog)
```

Easy!