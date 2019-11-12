# Week 12: Web Scraping
![assets/netscape.gif](assets/netscape.gif)

## Agenda:
- Review Homework
- Python Libraries, revisited
- Introduction to XML: the Extensible, Monstrous Language
- Beautiful Soup

![assets/dogs.gif](assets/dogs.gif)

## Jeremy talks about HTML

![assets/zoidberg.gif](assets/zoidberg.gif)

## Homework

### Assignment 1: Book Report

Individually, find a Python library and give a 3-5 minute presentation about it in class next time we meet. Bring in a code demo if you can. Choose something not too crazy. Coodinate among yourselves to pick different libraries.

You can [manually search in PyPI](https://pypi.org/search/) to find something that aligns with your interests. Alternatively, a not-bad way to find one is to google "best python libraries" or "top python packages".

Don't pick Requests, even though that's one of the most popular ones. We'll go into it in depth next time.

### Assignment 2: Serializing People

Take [your solution to the Week 07 assignment](https://github.com/scholarslab/praxis-code-lab-2018-2019/blob/master/week7/supergrouphmwk.py) and add two methods to that class to do JSON serialization and deserialization. That is, add one method that takes a filename as a parameter and writes a JSON representation of the data to that file and one method that takes a filename as a parameter and reads that file for a JSON string and then sets the instance's data to match the JSON.

For example:

```python

class historical_figures:
    # existing logic goes here
    def __init__(self, first_name, last_name):
        # ...
    def get_full_name(self):
        # ...
    def set_century(self, century):
        # ...
    def add_expertises(self, expertises):
        # ...
    def get_info(self):
        # ...
    
    # new methods:
    def serialize(self,filename):
        # write the JSON representation of the data to the file here
    
    def deserialize(self,filename):
        # read the file and decode the contents as a JSON string, then overwrite the data in the instance with the decoded JSON data.

jane = historical_figures('Jane','Austen')
jane.set_century('even longer 18th century')
jane.add_expertises(['writing','gender','sarcasm'])
jane.serialize("jane_austin.json")

jane = historical_figures('Jane','Austin')
jane.set_century('long 19th century')
jane.add_expertises(['Brownist Puritanism','American history','New Englandry'])

jane.get_full_name()
jane.deserialize("jane_austin.json")
jane.get_full_name()
```

### Assignment 3: Github Pages

Create a simple HTML file that contains your CV and push it to your personal Github account and host it using Github Pages. Follow this simple guide: [https://pages.github.com/](https://pages.github.com/)

Just put up an HTML CV for now - don't worry about anything that mentions Jekyll. We'll cover that another day.