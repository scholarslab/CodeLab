# Week 13: Web Scraping

## Python Libraries, revisited

A few weeks ago, we've played around with using Python code that people who are not Python (and who are often not you) wrote. Let's take a closer look at these libraries.

First, let's properly go over some ideas that we might have casually brushed past before:

* Library: There's a lot of different definitions for this term. Unless really unexpected things have happened, we are currently sitting in one right now. But in the CodeLab context, this is a collection of software that's directly used by other software. Most often, this will be a generalizable piece of logic that is useful to bundle separately so that other, unrelated pieces of software can use it. Because it's an informal term in Python and not a specific, technical one, it's more useful to think about libraries in terms of how code is organized. Used in this way, the concept of "software libraries" spans many different programing languages and development contexts: we have Python libraries, C++ libraries, Javascript libraries, operating system libraries, etc.

 Let's consider libraries that we've used. The [Python Standard Library](https://docs.python.org/3/library/) is the most obvious example which encompasses many different purposes and packages (more on that later), but is unified in that it is included in all Python installations so that Python code that's written using the Standard Library will run on any compatible Python environment of the expected version. Parts of the Standard Library that we've used before include packages like [random](https://docs.python.org/3/library/random.html) and ones that we'll be using shortly, like [json](https://docs.python.org/3/library/json.html).

 Third-party libraries found on PyPI are less expansive than the Standard Library. This week, we'll take a look at [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), which is analogous in scope to packages like random or json. In fact, third party libraries are often organized into a single package. A library like Beautiful Soup can best be thought of in terms of purpose: you want to accomplish the a particular, common task like scraping a website and Beautiful Soup helps accomplish it. 

* Package: A package is a formal term in the Python context. It's a specific organization of code which all lives in a single directory. Libraries sometimes (often) consist of a single package (e.g. Random or BS4), so the term is sometimes (often) used interchangeably. Packages are the basic unit by which we install and use libraries. PyPI is the Python *Package* Index, so when we type `pipenv install beautifulsoup4` into the terminal, we're installing the beautifulsoup4 package.

 Here, confusingly, the name of the package on PyPI (beautifulsoup4) doesn't match the actual Python code package (bs4). Always [read the docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)! 
 
 We use Beautiful Soup in our Python code with code that looks like this:
 
 ```python
 import bs4
 soup = bs4.BeautifulSoup(html_doc, 'html.parser')
 # 'bs4' is the package, 'BeautifulSoup' is a class defined inside the package definition
 ```

 or

 ```python
 from bs4 import BeautifulSoup
 soup = BeautifulSoup(html_doc, 'html.parser')
 # this code is equivalent
 ```

 We can also use the star symbol, which often means "all" or "any", to import all the modules in the package:

 ```python
 from bs4 import *
 soup = BeautifulSoup(html_doc, 'html.parser')
 # imports * imports all modules in a package
 ```

 In these examples, we can either the `bs4` *package* directly or, using the `from` keyword, import *modules* from with that package.

 Incidentally, it's almost always considered poor practice to use the `from x import *` form. We see in the example immediately above that, for people just reading through our code, there's no obvious connection between the bs4 package and the BeautifulSoup class. It would take some deeper understanding of BeautifulSoup or at least chasing down some its documentation. This confusion is made worse by the fact that we can import multiple packages this way and, actually, do something like this:

 ```python
 def randint(i,j):
    return i
 from random import *
 print(randint(0,10))
 ```

 Which randint would this run? The best and clearest way to import a package is using the `import x` format, since the contents of each module must then be explicitly addressed using the `x.y` format. For small and simple associations, `from x import y` is acceptable.
 
 Since directories can be nested, packages can be also. However, it is somewhat unusual to see this done in practice for third-party libraries. Typically, they will be organized more simply or split into different libraries altogether.
 
* Modules: Since a Package is a directory, we can probably intuit that Modules are individual Python files contained within a directory. In fact, every .py file can be a module if we import them into another bit of Python code. Often, this is most useful for separating variables from code and for breaking classes out into their own file. So, we can do this (we can tell git to ignore config.py and freely commit code.py):

 config.py:
 ```python
 PASSWORD = "yourefired"
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

 There is a special module in each package that makes them a package that must be named `__init__.py`. This file can be blank, but its presence is what lets Python know that you intend a directory to be a package. Note that `__init__` is also how we define class constructor. Here, the contents of `__init__.py` are run whenever we import a package. This allows us to, effectively, treat the package itself like a module.

 For how this all works practically, we can take a look at the code for the familiar [json package in the Standard Library](https://github.com/python/cpython/tree/3.9/Lib/json) (all the Standard Library packages will have links at the top of the docs to the code itself). We see here that the JSON package actually contains a variety of modules, broadly organized by function (decoder, encoder, etc). However, we haven't really used these in our examples because we've accessed the functions defined inside of its [__init__.py](https://github.com/python/cpython/blob/3.9/Lib/json/__init__.py). There, we can find the definitions for our old favorites like [json.dumps](https://github.com/python/cpython/blob/3.9/Lib/json/__init__.py#L183).

 This json package is organized this way because if for some reason we didn't like the way that Python handled functions like loads and dumps (for example, if we wanted a prettified version of dumps), we can override the default `json.encoder.JSONEncoder` class (where `json` is a package and `encoder` is the module) ourselves.

 One last thing: inside of the `__init__.py` for json, we see that there's [a few lines](https://github.com/python/cpython/blob/3.9/Lib/json/__init__.py#L106) where it imports classes like JSONDecoder and JSONEncoder. This means that whenever we import the json package in our code, we also perform these imports too. This means that when we do `import json`, we can address the same JSONEncoder class as either `json.encoder.JSONEncoder` or `json.JSONEncoder`. This is often done to simplify the internal organization of packages to users.

## XML
![xml vs jason](assets/jason.gif)

(XML [left] and JSON [right])

We've covered some JSON already. Let's talk about its older, more monstery cousin. They're not exactly the same kind of thing. JSON is intended, as we've seen and used, to encapsulate object states. XML stands for "Extensible Markup Language" and the Markup Language part means that it's a way to "mark up" text in ways that convey information beyond the very narrow boundaries of the text, like an editor might mark up a document.

That is, markup languages provide ways to express anything that isn't directly expressible as text characters: *emphasis*, _italics_, [links](https://github.com/scholarslab/CodeLab/blob/master/Week05/assets/hazel_romantic_hero.jpg), spacing and layout, typeface, and so on. Images too.

![hazel snoozing](assets/hazel_snooze.jpeg)

When you all blog, you're writing in another markup language, the whimsically-named Markdown.

But despite the differences of intention, both XML and JSON (and also CSV and markdown) are text formats designed to contain and structure data.

Let's take a quick peek at what XML looks like. Let's shift gears from our usual Much Ado About Nothing examples and move on to the 31st century.

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

![bender](assets/bender.gif)

This is an arbitrarily constructed example. XML is built around tags that represent discrete elements. In the example above, `scene` and `dialog` are tags. Tags can contain attributes, such as the `role` attribute for `dialog` or the `location` attribute in `scene`. Tags can wrap around text and we can understand that the tag contains the text, like the label for a link or the text of a line of dialog.

XML is really verbose and you have to be really careful about closing tags correctly. But it's quite powerful, with entire secondary languages to define its schema, to translate it from one XML format to another, and to traverse the data that it contains. That complexity makes it a bit clunky to use.

The "Extensible" part of the XML name means that we can use this basic structure to build other languages. Just like my constructed Futurama script example can form a standard format to represent dialog, XML can be extended (really, constrained) to represent the structures of other specific kinds of data. One example is TEI, the Text Encoding Initiative, which uses XML to represent text documents. Another is the modern form of HTML that the web runs on.

## Web Scraping
![https://media.giphy.com/media/IwTWTsUzmIicM/giphy.gif](https://media.giphy.com/media/IwTWTsUzmIicM/giphy.gif)

Okay, let's put these ideas together. Let's scrape some websites.

Web scraping is extracting data from web pages, using the syntax of a web page. It's great for compiling datasets when you don't already have them in a database somewhere. A good supplemental resource for web scraping is [Intro to Beautiful Soup by Jeri Wieringa](https://programminghistorian.org/en/lessons/intro-to-beautiful-soup) at The Programming Historian.

### So how do we scrape the web?
In Python, there's more than a few different libraries we could use, but let's continue to focus on Beautiful Soup.

We've already installed the library into our pipenv using:

```python
pipenv install beautifulsoup4
```

We can make sure this was done correctly by importing the library into a Python file in our virtual environment and printing its version number (remember to activate the appropriate pipenv shell if you haven't yet).

```python
import bs4
print(bs4.__version__)
```

Now let's figure out how to use BeautifulSoup by going to the [documentation for the library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Let's take a quick look at that now.

Okay, let's do this. Let's try scraping the [Scholars' Lab blog page](https://scholarslab.lib.virginia.edu/blog/)

First, we should have pipenv install another library to help us grab websites. There are some good built-in ways to download things from the web, but one of the easiest to use and most popular is the third party library Requests (coincidentally by Kenneth Reitz, the same guy who wrote Pipenv), the same library we used to access APIs.

We can use it to download our website using this simple code:

```python
import requests

url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
print(html)
```

Now that we've got the raw HTML of the site, we can then use Beautiful Soup to parse it.

So, let's first import beautiful soup...

```python
import bs4
```

Next, we'll instantiate a Beautiful Soup instance and pass it our html. One easy thing we can do is have BS prettify our html so it's a bit more expansive and readable.

```python
import bs4
import requests

url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
print(soup.prettify())
```

We can see here that `soup` is an instance of a [bs4.BeautifulSoup class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautifulsoup). This is an object that represents the whole of the document. The other important class we will use is the [Tag class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag), which represents an html tag. These two classes actually share many of the same methods: we can use `get_text()` on either a BeautifulSoup or a Tag to extract just the text that they contain.

We can also use the `find_all()` method that they share to search with either the whole document or within the tag. Remember that tags can be nested within each other.

Let's take a look at the basic structure of the html file. We can do this easily using the development console built into most popular browsers. In Chrome or Firefox, right clicking (or control-clicking) and choosing "Inspect" or "Inspect Element".

We can see that, for example, the authors for each blog post live in something called a `div` tag that looks like this:

```
<div class="blog-meta__author">
    <a href="/people/brandon-walsh/">Brandon Walsh</a>
</div>
```

Let's ignore most of the nitty gritty of what this means right now, but we can see that the outer tag is a `div` tag, which contains an `a` tag within. These are some of the basic building blocks of HTML: `div` tags are "divisions", containers that are used to organize text and other tags together. `a` tags are anchors, which are used for links. So this html block is a container (`<div class="blog-meta__author">`) that contains a link (`<a href="/people/brandon-walsh/">`) that points to the author of a blog post.

We can see that the outer div tag has an attribute, `class="blog-meta__author"`, which we can pass to BeautifulSoup to find all the author divs. To do this, we tell `soup` to `find_all` the `div` tags that are of class `"blog-meta__author"`:

```python
...
print(soup.find_all("div",class="blog-meta__author"))
```

This bit of code results in a Python list containing 4 Tag objects representing the authors of the 4 most recent blog posts. We can drill down into each of these Tags to get at their contents. For example, we can get the name for each author by getting the text of the `a` tags. The `find()` method is like `find_all()`, but just returns the first result (so it's equivalent to `find_all()[0]`).

```python
...
author_divs = soup.find_all("div",class_="blog-meta__author")
for author_div in author_divs:
    print(author_div.find("a").get_text())
```

To get the URL for each author, we can ask soup for the "href" attribute for the `a` tag by passing it the name of the attribute like the key of a dictionary.

```python
...
author_divs = soup.find_all("div",class_="blog-meta__author")
for author_div in author_divs:
    print(author_div.find("a")["href"])
```

Knowing how to grab links means that we can follow them by asking Requests to grab the website at that URL. This way, we can write a "spider" to crawl through entire websites. This is a very powerful way to map out online datasets that aren't designed to be very accessible.

So, for example, we can craw through and save *every* blog post on the Scholars' Lab blog into one file for the purposes of text analysis.

```python
import bs4
import requests

post_text = ""
url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
soup = bs4.BeautifulSoup(html, features="html.parser")
old_posts = soup.find("section",id="previous_posts")
for i in old_posts.find_all("li"):
    # the post links are relative links, so we need to append the domain to make it an absolute link
    post_url = "https://scholarslab.lib.virginia.edu"+i.contents[0]["href"]
    post  = requests.get(post_url).text
    soup = bs4.BeautifulSoup(post, features="html.parser")
    post_text+=soup.find("div", class_="post__content").get_text()
    # Let's write out all the posts every time so we can interrupt it at any point
    f = open("posts.txt", "w")
    f.write(post_text)
    f.close()
```

In a real-world example, we might want to introduce a delay to not hammer someone's web server or to trigger some kind of denial-of-service protection.
