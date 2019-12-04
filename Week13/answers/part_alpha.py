from bs4 import BeautifulSoup
import requests


url = "https://scholarslab.lib.virginia.edu/blog/"
html = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")

# We're going to use a dictionary to store our counter.
# Dictionaries map keys to values, like how a phone book maps names to numbers.
# The key is unique, so using a dictionary as a counter makes it easy
# to keep track of people by using their names as keys.
# Their post count will be the value.
counter = {}
total = 0
# We can use the nth-child CSS selector to select the
# *second* link for each blog post or we can just get
# the <li> tag for each post and use BS4's DOM traversal
# mechanisms like find_all() to get to that second <a>
# tag
for link in soup.select("ul.page-previous_posts li a:nth-child(2)"):
    # Because of how we constructed our soup.select, the link
    # variable in each for loop cycle is a specific link to a
    # blog post author's profile page and link.get_text() is
    # the author's name.
    author = link.get_text()
    total += 1
    if author in counter:
        # if the author is already in the list of authors,
        # increment the counter 
        counter[author]+=1
    else:
        # if they're not, set the counter to 1 (to reprsent)
        # the blog post we're looking at
        counter[author] = 1

# Here's a bit of extra code to sort the dictionary by number of posts
# You don't have to do this or spend too much time understanding how this works
sorted_counter = {author:count for author, count in sorted(counter.items(), key=lambda x: x[1], reverse=True)}

# Counter and sorted_counter are dictionaries that map the name to number of posts
# We can print each author and their posts using a for loop.
# In a for loop, the iteration cycles through keys (authors, in this case).
print("Total Posts:",total,"\n")
for author in sorted_counter:
    print(author, ":", sorted_counter[author])
