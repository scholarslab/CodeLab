# Week 7: Class is in Session
![bart_class dot gif](assets/bart_class.gif)

## Agenda:
- Review Homework
- File input and output in Python 
- Let's talk about classes again!
- Importance of Import
- Next week's homework


## File Input

File IO is easy in Python using the [`open` built-in function](https://docs.python.org/3/library/functions.html#open).

To open a file for reading (input), we just do:

```python
input_file = open("text.txt","r")
text = input_file.read()
print(text)
input_file.close()
```

Here, we use the `open` function to open a file in mode "r" (read). `open` returns a [File Object](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) that provides methods for reading and writing. In this case, the `read` method reads in data from the `input_file` file object and stores it as a string in `text`.

At the end, we can close the file to save some memory, but even if we don't do it explicitly, Python will eventually catch on to the fact that it isn't being used anymore and do it for us. This isn't a huge concern unless you're opening thousands of files or the files you're opening are very, very large.

One convenient way to read files is to combine the file object with a for loop to read text files line by line.

```python
input_file = open("text.txt","r")
for line in input_file:
    print(line.upper())
input_file.close(
```
This will loop through the file, line by line, until it's closed.

Often, you'll see file handling used with the `with` keyword:

```python
with open("text.txt","r") as input_file:
    for line in input_file:
        print(line.upper())
```

This is functionally the same as our last example. The only difference is that the file is automatically closed at the end of the block. You can use whichever convention you like, but keep both in mind because they're both pretty common in the wild.

## File Output

File output is very similar. We just use mode 'w', which overwrites the file specified. We can also use 'x' (which only works for new files) or 'a' (which appends data at the end of the file). Read the [`open` docs](https://docs.python.org/3/library/functions.html#open) for all the details.

```python
f = open()
for i in range(0,100):
    f.write(str(i**2)+"\n")
```

Here, there's something just a little tricky. `i` and `i**2` are  integers, but the file object in this case expects a string. If we try to use `f.write(i**2)` instead, we'll get an error: `TypeError: write() argument must be str, not int`.

To get around this, we can convert from int to string using the built-in `str` class constructor `str()` to create a new string that's the *string representation* of the integer we pass in. So even though the inteher 4 and the string "4" look the same, they're different objects and different ways to represent data.

For the same reason that we can't do `f.write(4)`, we also can't do `"4"+4` (or, for that matter, `4+"4"`). We have to explicitly tell python whether we want it to treat each value as an integer or a string. `"4"+str(4)` produces "44" while `int("4")+4` returns 8.

The second new thing here is the newline character "\n", which is technically called a LF or Line Feed. This inserts a line break between characters in a string.

## Putting it Together

Here's part of Emily and Eleanore's solution to one of last week's assignments. Let's ignore the part where we chop off the front matter and focus on just the word replacement.

```python
jane = 'The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'
jane = jane.replace("man","person").replace("wife","partner")
print(jane)
```

Let's say that we want to "modernize" every classic book on Project Guttenberg. The first step is to write a program to read a single book in, replace the words, and then write it back out to a file.

I've pushed the Guttenberg version of Pride and Prejudice as a text to this repository, under the `Week07/examples` directory and the skeleton of the code needed to convert the text:

```python
filename = "pg42671.txt"

### input code goes here

jane = jane.replace("man","person").replace("wife","partner")

### output code goes here
```

## Classes (again!)

Let's review classes! One important thing to understand is that we already use classes all the time.