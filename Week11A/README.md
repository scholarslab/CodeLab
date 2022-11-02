# Week 10: APIs

![maple](assets/toby.jpg)

## Agenda
- [Application Programming Interfaces](lesson.md)

## Assignments

Okay! Let's take an easy-to-use API for a spin. Take a look at [SWAPI, the Star Wars API](https://swapi.dev/documentation). This is a nice and simple API with some nice conveniences and a pretty basic dataset. Best of all, there's no registration or API key (the rate limit is 10k queries a day, gated by IP address).

Read the documentation closely, paying attention to the example URLs listed. The IDs for each category are, conveniently, sequential integers. So there are 6 films (apparently this dataset hasn't been updated in a while) with IDs ranging from 1 to 6 and accessible through, for example, [https://swapi.dev/api/films/1/](https://swapi.dev/api/films/1/). Results for each call are in JSON by default.

There is a specific helper library in Python, but you should use Requests (or another http library if you're feeling fancy) to access the API directly.

Write a bit of code to report on the average height of every character listed for each film.

For reference, here is the code I showed in class for the Online Movie Database (if you want to run it, you'll need to sign up for an API key and fill it in):

```python
import requests
import json

API_KEY =  'KEY'

p = {'apikey': API_KEY, 's': 'Dune'}
r = requests.get('http://www.omdbapi.com/',params=p)
if r.status_code != 200:
    print("Bad response code!")
    exit()
for movie in json.loads(r.text)["Search"]:
    print(movie["Title"]+" ("+movie["Year"]+")")
    p_movie = {'apikey': API_KEY, 'i': movie["imdbID"]}
    r_movie = requests.get('http://www.omdbapi.com/',params=p_movie)
    print("\t"+json.loads(r_movie.text)["Plot"])
```

![fatdog](assets/fatdog.jpg)