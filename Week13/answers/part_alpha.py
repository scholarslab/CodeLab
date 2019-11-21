from bs4 import BeautifulSoup
import requests

url = "https://scholarslab.lib.virginia.edu/blog/"
html = requests.get(url).text
soup = BeautifulSoup(html)

counter = {}

# We can use the nth-child CSS selector to select the
# *second* link for each blog post or we can just get
# the <li> tag for each post and use BS4's DOM traversal
# mecahnisms like find_all() to get to that second <a>
# tag
for link in soup.select("ul.page-previous_posts li a:nth-child(2)"):
    # Because of how we constructed our soup.select, the link
    # variable in each for loop cycle is a specific link to a
    # blog post author's profile page and link.get_text() is
    # the author's name.
    author = link.get_text()
    if author in counter:
        # if the author is already in the list of authors,
        # increment the counter 
        counter[author]+=1
    else:
        # if they're not, set the counter to 1 (to reprsent)
        # the blog post we're looking at
        counter[author] = 1

sorted_counter = {author:count for author, count in sorted(counter.items(), key=lambda x: x[1])}
print(sorted_counter)
