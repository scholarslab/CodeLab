# Week 10: Working with Structured Data
![Tacoma Narrows GIF](assets/structure.gif)

## Agenda
- Review homework (if it exists)
- [Hands on with structured data ](lesson.md)

## Assignment

### Part 0
Now that you have a handle on composite data structures like lists and dictionaries, we can put them to practical use. Create a representation of your Praxis cohort in Python. You can include whatever data you want: basic data like name, year, department, but maybe consider the icebreaker questions from the [git practice](https://github.com/scholarslab/gitpractice). Then use the Python json module to dump it into a json formatted text file.

### Part 1
Okay! The meat of this week's homework. It's another kinda amorphous, experimental one. Working alone or in groups (or a single super-group), find an interesting dataset, read it into Python, and use Python to extract some interesting facts from it.

Happily, there are a lot of interesting datasets out floating out there, often in CSV-like formats. FiveThirtyEight, for example, has a ton of csv-formatted data on their [Github](https://github.com/fivethirtyeight/data). Buzzfeed has a similar [Github repo](https://github.com/BuzzFeedNews). IMDB has big, big datasets in tab-separated-values format (CSV, but with tabs) [on their site](https://www.imdb.com/interfaces/). The Government has an enormous clearinghouse of public data on the appropriately-named [data.gov](https://catalog.data.gov/dataset) website, in a variety of formats. The sky's the limit!

Even though the CSV module makes reading the data into Python pretty easy, this is potentially a really tricky assignment because keeping different related data fields together can be challenging (e.g. sorting a column and also sorting the other fields for each row together). Google is definitely your friend here ("sorting dictionary by key python"). Literally millions of people have had to do the same thing you're trying to do. If you're having some trouble, ping me on Slack any time. It might be useful to read the CSV data into another data structure to make this easier.

Plan for 0-5 minute shows-and-tell next week!
