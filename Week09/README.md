# Week 9
![assets/netscape.gif](assets/netscape.gif)

## Agenda:
- Review Homework
- Libraries, Packages, and Modules
- JSON
- HTML/CSS Part 2
- Next week's homework

## Python Libraries
![assets/dogs.gif](assets/dogs.gif)

One of the strengths of Python is its large standard library that comes with every installation of Python. However, even the most extensive standard library doesn't cover all the bases and sometimes the way that the standard library does certain things is more complicated than is necessary for most cases. Python provides a robust mechanism to find, download, and use external libraries by the global community of Python developers.

Last week, when we installed Beautiful Soup, we ran the command:

```
pip3 install --user beautifulsoup4
```

[Pip](https://pip.pypa.io/en/stable/) is the recommended tool for installing packages. The command above is mostly what you'll be using to do this. It grabs a package from the [Python Package Index (PyPi)](https://pypi.org/) and installs it in your Python user install directory. PyPI is a vast and sprawling collection of code: if you have a sense that you need to do something complicated that maybe someone else has had to do in the past, there's a good chance that there's a package for that already.

First, let's properly go over some terminology that we've touched on in the past:

* Library: There's a lot of different definitions for this term. Unless really unexpected things have happened, we are currently sitting in one right now. But in the CodeLab context, this is a collection of software that's directly used by other software. Most often, this will be a generalizable piece of logic that is useful to bundle separately so that other, unrelated pieces of software can use it. Because it's an informal term in Python and not a specific, technical one, it's more useful to think about libraries in terms of how code is organized. Used in this way, the concept of "software libraries" spans many different programing languages and development contexts: we have Python libraries, C++ libraries, Javascript libraries, operating system libraries, etc.

 Let's consider libraries that we've used before. The [Python Standard Library](https://docs.python.org/3/library/) is the most obvious example which encompasses many different purposes and packages (more on that later), but is unified in that it is included in all Python installations so that Python code that's written using the Standard Library will run on any compatible Python environment of the expected version. Parts of the Standard Library that we've used before include packages like [random](https://docs.python.org/3/library/random.html) and ones that we'll be using shortly, like [json](https://docs.python.org/3/library/json.html).

 Third-party libraries found on PyPI are less expansive than the Standard Library. Last week, we used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), which is analogous in scope to packages like random or json. In fact, third party packages are often organized into a single package. A library like Beautiful Soup can best be thought of in terms of purpose: you want to accomplish the a particular, common task (navigating )
 Third-party libraries found on PyPI are less expansive than the Standard Library. Last week, we used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), which is analogous in scope to packages like random or json. In fact, third party packages are often organized into a single package. A library like Beautiful Soup can best be thought of in terms of purpose: you want to accomplish the a particular, common task (scraping a website) and Beautiful Soup helps accomplish it. 

* Package: A package is a formal Python term. It's a specific organization of code which all lives in a single directory. Libraries sometimes (often) consist of a single package (e.g. Random or BS4), so the term is sometimes (often) used interchangeably. Packages are the basic unit by which we install and use libraries. PyPI is the Python *Package* Index, so when we type `pip3 install --user beautifulsoup4` into the terminal, we're installing the beautifulsoup4 package.

 Here, confusingly, the name of the package on PyPI (beautifysoup4) doesn't match the actual Python code package (bs4). Always [read the docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)! 
 
 Knowing this, we use Beautiful Soup in our Python code with:
 
 ```python
 from bs4 import BeautifulSoup
 # 'bs4' is the package, 'BeautifulSoup' is a class defined inside the package definition
 soup = BeautifulSoup(html_doc, 'html.parser')
 ```
 
 or:

 ```python
 import bs4
 soup = bs4.BeautifulSoup(html_doc, 'html.parser')
 # this code is equivalent
 ```

 we can also do:

 ```python
 from bs4 import *
 soup = BeautifulSoup(html_doc, 'html.parser')
 # imports * imports all modules in a package
 ```
 
* Modules: Since a Package is a directory, we can probably intuit that Modules are individual Python files contained within a directory. In fact, every .py file can be a module if we import them into another bit of Python code. Often, this is most useful for separating variables from code and for breaking classes out into their own file. So, we can do this (we can tell git to ignore config.py and freely commit code.py):

 config.py:
 ```python
 PASSWORD = "passw0rd"
 ```
 
 code.py:
 ```python
 import config
 if input("Enter password:") != config.PASSWORD:
    print("WRONG PASSWORD")
    exit()
 ```

 And we can do something like this:

 doglib.py:
 ```python
 class Dog:
    def __init__(self, name):
        self.name = name
        print("Bark! My name is "+name)
 ```

 code.py:
 ```python
 import doglib
 # dog is the module, 
 hazel = doglib.Dog("Hazel")
 ```

## JSON
![assets/jason.gif](assets/jason.gif)
(XML [left] and JSON [right])

We've covered some HTML and the related, more general XML standard a bit (more on this later). You know what it looks like at least:

```xml
<scene id = "30" type = "INT" location = "PlanetExpress" episode="S01E3">
    <dialog role="Leela">
        Please, Bender! Have some malt liquor! If not for yourself, then for the people who love you.
    </dialog>
    <dialog role="Bender">
        I hate the people who love me and they hate me!
    </dialog>
</scene>
```

XML is really verbose and you have to be really careful about closing tags correctly. But it's quite powerful, with entire secondary languages to define its schema, to translate it from one XML format to another, and to traverse the data that it contains. That complexity makes it a bit clunky to use, even with a 
But XML isn't the only data format in town. There's quite a few others, the most popular of which is probably JSON, which was originally created out of Javascript ("JavaScript Object Notation"). Like XML, it's text-based and fairly legible. Unlike XML, it's much more compact and able to express arrays/lists of things.

It's often mispronounced "Jay Song", but you can be real snooty by making a point to say "Jason", like the Argonaut. Here's an example of a JSON representation of a Famous Canadian:

```json
{
  "firstName": "Justin",
  "lastName": "Trudeau",
  "frenchName":"Pierre",
  "occupation": "Character actor on the 2007 CBC docu-drama 'The Great War'",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "123 Canadian White House (Un Deux Trois Maison-Blanche d'Canada)",
    "city": "Ottawa",
    "state": "Quebec"
  },
  "phoneNumbers": [
    {
      "type": "Home (Maison)",
      "number": "212 555-1234"
    },
    {
      "type": "Cell (Téléphone Portable)",
      "number": "646 555-4567"
    },
    {
      "type": "Hot Line (Ligne Diplomatique)",
      "number": "123 456-7890"
    }
  ]
}
```

It's useful to understand that there are many ways to represent data, of which HTML/XML and JSON are two that are better or worse at expressing different kinds of information and more or less suitable for different contexts. JSON in particular is a popular format to use for handling simple data on the Internet.

It's also handy because it's so simple that there are simple ways for many different programming languages to read and write it. In Python, we can use the [`json` package](https://docs.python.org/3/library/json.html) in the Standard Library to read and write JSON.

Let's take our totally factual Trudeau JSON string and load it into Python:

```python
import json
json_string = '''{"firstName":"Justin","lastName":"Trudeau","frenchName":"Pierre","occupation":"Character actor on the 2007 CBC docu-drama 'The Great War'","isAlive":true,"age":27,"address":{"streetAddress":"123 Canadian White House (Un Deux Trois Maison-Blanche d'Canada)","city":"Ottawa","state":"Quebec"},"phoneNumbers":[{"type":"Home (Maison)","number":"212 555-1234"},{"type":"Cell (Téléphone Portable)","number":"646 555-4567"},{"type":"Hot Line (Ligne Diplomatique)","number":"123 456-7890"}]}'''
jt = json.loads(json_string)
print(jt["firstName"],jt["lastName"])
for number in jt["phoneNumbers"]:
    print(number["number"])
```

What sorcery! Our JSON data has magically become Python data! The general act of writing and reading a specific data format (broadly defined) is called encoding and decoding. The specific case of writing and reading to and from an object in a programming language is called serialization and deserialization.

The opposite (well, reflection) of json.loads (load string) is dumps (dump string), which produces a JSON string from simple Python objects. You should be able to dump back any object you loaded from a JSON string. This is particularly useful when you want to easily save your data to file and read it back again. 

