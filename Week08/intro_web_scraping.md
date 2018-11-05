## Intro to Web Scraping
![https://media.giphy.com/media/IwTWTsUzmIicM/giphy.gif](https://media.giphy.com/media/IwTWTsUzmIicM/giphy.gif)

#### What is web scraping?
Web scraping is extracting data from web pages, using the syntax of a web page. It's great for compiling datasets when you don't already have them in a database somewhere. For more information about web scraping, I highly recommend [Intro to Beautiful Soup by Jeri Wieringa's from the Programming Historian](https://programminghistorian.org/en/lessons/intro-to-beautiful-soup)

#### So how do we scrape the web?
In python, there's a few different libraries we could use, but today we're going to focus on Beautiful Soup.

First we need to install the library:
```python
pip3 install beautifulsoup4
``` 

Now let's make sure we have the library. Start up your python interpreter and we'll import the library
```python
import bs4
print(bs4.__version__)
```
Now we see that we have the library installed and it should be version `'4.6.3'`. Any time you download a python library onto your computer, unless you're using a virtual environment, it will accessible in every directory.

Now let's figure out how to use BeautifulSoup by going to the [documentation for the library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Let's go through their quick start example using our interpreters.

[Let's talk about HTML](intro_html.md)

----

Now let's create a new python script called `web_scraper.py` and try scraping the Scholars' Lab blog page. Go to the soon to be released [Scholars' Lab blog page](http://maybe.scholarslab.org/blog/)

*Downloaded page instructions*
Save the page to your workspace as `slab_blog.html`.
![save image](../assets/save_img.png)


First import beautiful soup
```python
from bs4 import BeautifulSoup
```

Next, instantiate a Beautiful Soup instance and pass it our webpage and then print out the results
```python
soup = BeautifulSoup(open('slab_blog.html'))
print(soup.prettify())
```

*In class assignment*

How would we get the title of the web page?

How would we get the text of the web page?

How would we get the links of the web page? 


*Reading urls instructions*
If you don't want to download each web page, we can use a different library to read the urls of our webpages and store the html. This library is called `requests` and you can find [the documentation here](http://docs.python-requests.org/en/master/). 

Again we have to install the library
```python
pip3 install requests
```

Then we import it using `import requests` into our script where we imported BeautifulSoup. Now instead of downloading our webpage we can use requests to get the contents

```python
result = requests.get('http://maybe.scholarslab.org/blog/')
print(result.content)
```
We should now see the entire web page like earlier.

Then we can store the result and pass it to BeautifulSoup
```python
slab_blog = result.content
soup = BeautifulSoup(slab_blog)
```
![https://media.giphy.com/media/14rI7bze8GSShq/giphy.gif](https://media.giphy.com/media/14rI7bze8GSShq/giphy.gif)
