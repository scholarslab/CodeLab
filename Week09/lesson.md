# External Depedencies

![fatdog](assets/fatdog.jpg)


## Outside help

The Python Standard Library provides a pretty wide set of tools. It comes with every Python install and that's one of its main strengths - you don't have to worry about whether someone has `itertools` or `random` installed.

But sometimes, the thing we need is a little bit more obscure or specific. We couldn't include all these things with every Python install, because otherwise that install would be enormous. Instead, there's something like an app store for Python code (except that it's all free, because Python is all free) called the [Python Package Index, or PyPI](https://pypi.org/). Not to be confused with PyPy (groan), which is something else.

It's pretty big. Anyone can submit projects to it and so there are more than a quarter-million individual ones.

We can install any one of these packages through [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/), which all of you should already have since we did the environment setup at the beginning of the year.

Pipenv coordinates the function of two important tools, Pip and Virtualenv. Pip is Python's package manager, which means that it downloads and installs Python packages. But it downloads them either to the whole system or to a single user's space. This means that when we grab a package, we could override packages that are being used by other projects. This is potentially really bad, because we're not the only ones on our computers that use Python. We could break applications or even our operating system.

To solve this, Virtualenv walls off "virtual" environments for particular programs. These virtualenvs are like independent Python installations that don't affect other things that use Python.

Pipenv combines these functions together into one tool. It works at the directory level. We can create a new pipenv environment inside of a directory so long as it doesn't live in another another directory with a pipenv environment. You can choose to have, for example, all your Codelab assignments live inside a single directory like `~/projects/Codelab` or you can choose to have each week have its own environment like `~/projects/Codelab/Week10`. It doesn't matter too much since you probably won't have dependency conflicts between different weeks. But you can't have both an environment in both because one is inside of the other.

To create a pipenv environment, we can just run `pipenv install X` to install a package from PyPI and it will automatically create a virtualenv for that directory and install package "X" in that virtualenv. After we do that, we can then use `pipenv shell` to spawn a subshell to use Python in that directory. To quit out of the subshell, we can just use the `exit` command.

It's a bit clunky, but it works really well for most DH work.

You can browse through PyPI and see if there's anything interesting. Of course, the first thing I did was find this: [getname](https://pypi.org/project/getname/).

So, let's take that for a spin.

## Using Pipenv

First, let's go into whatever directory where we're going to set up our pipenv environment. For me, that's going to be...

```
cd ~/projects/sandbox
```

Now, let's set up our pipenv environment and install that package.

```
pipenv install getname
```

That'll take a little bit to run. After it finishes, we have our environment set up. We can see that there are two new files inside our directory: Pipfile and Pipfile.lock.

Looking inside Pipfile, we can see something like:

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
getname = "*"

[requires]
python_version = "3.7"
```

We can see that there's some basic information about the package we specified. In this case, the line `getname = "*"` indicates that we want to grab some version of the `getname` package (* is often used as a wildcard character, standing in for "any").

The Pipfile.lock file has similar information, but with the specific version of the packages that we grabbed.

Don't worry about the particular formats for these files. It's only really important to understand that by distributing them (for example, by committing them to git), we can tell other people that grab our code what external dependencies they need (and potentially what versions of those dependencies).

Everything is set up now.

We can run the `which python` command to show us what the default system Python is. We'll get back something like `/usr/local/bin/python`.

Now, we can activate the shell using:

```
pipenv shell
```

If we try the `which python` command again, it'll be something different. Something like: `/Users/shane/.local/share/virtualenvs/sandbox-2UjlHtLl/bin/python`

That tells us that we're actually using a totally different Python from before. A Python that has access to the package that we just told pipenv to grab.

Which allows us to do...

```python
from getname import random_name

dogs = []
while len(dogs)<6:
    dogs.append(random_name('dog'))
print(dogs)
```

Without all the pipenv steps, we wouldn't have access to our new package and that first import line would fail.

## Example: NLTK

Still with us? Great!

![Hazel says hello!](assets/hazel_hi.jpg)

Okay, so let's do another, real example using the very useful and powerful NLTK package.

I've included the dialog frm Much Ado About Nothing in [a nicely formatted JSON file](MAAN_dialog.json). Let's make use of that now.

We can start by using pipenv to install nltk and activating the pipenv shell.

```
pipenv install nltk
pipenv shell
```

Just for NLTK, we need to prime the module by downloading a few key bits of data. So we should jump into the Python interactive interpreter and just run these lines:

```python
import nltk
nltk.download('stopwords')
```

This is specific to nltk and actually kind of an unusual way of working in Python. We only need to do this once for our environment.

Now we can work on our actual Python code. Let's read in our json file.

```python
import json

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())
```

This imports and json-loads our text file as a list of dictionaries. Because we've put the work into formatting our data, we can easily manipulate it to our purposes. Let's say we have a scholarly interest in, specifically, how the dialog of Beatrice and Benedick differ.

Let's collate their lines now.

```python
import json

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]
```

This gives us two variables, `bea` and `ben`, that contain all of those characters' lines.

How might nltk give us insight into these lines? Let's do something simple and see out how the words that Shakespeare put into their mouths differ by looking at frequency distribution.

First, we need to tokenize the dialog (i.e. break up the dialog into words). We can use one of nltk's built-in tokenizers for this. And then let's remove *stopwords*, which are common English words like articles that don't provide much insight in this sort of analysis.

Stopwords are one of the wordlists provided by nltk. You can see all the English stopwords and read up on the other wordlists in the [NLTK book](https://www.nltk.org/book/ch02.html#wordlist-corpora). The little bit of code we ran in the interactive interpreter downloaded the stopword wordlist.

Here's what the code to tokenize the dialog and strip out the stopwords looks like:

```python
import nltk
import json

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]

bea_tokens = []
ben_tokens = []

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
for token in tokenizer.tokenize(bea):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        bea_tokens.append(token.lower())
for token in tokenizer.tokenize(ben):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        ben_tokens.append(token.lower())

print(bea_tokens)
print(ben_tokens)
```

`bea_tokens` and `ben_tokens` are now lists of words with stopwords stripped out. 

We can pass these lists back to NLTK's frequency distribution function to see how often distinct words appear.

```python
import nltk
import json

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]

bea_tokens = []
ben_tokens = []

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
for token in tokenizer.tokenize(bea):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        bea_tokens.append(token.lower())
for token in tokenizer.tokenize(ben):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        ben_tokens.append(token.lower())

bea_freq = nltk.FreqDist(bea_tokens)
print("Beatrice word frequencies:")
for key, val in bea_freq.most_common(10):
    print(str(key) + ':' + str(val))

ben_freq = nltk.FreqDist(ben_tokens)
print("\n\n Benedick word frequencies:")
for key, val in ben_freq.most_common(10):
    print(str(key) + ':' + str(val))
```

And since a big list of words is maybe less useful, let's install a plotting library that nltk uses through pipenv:

```
pipenv install matplotlib
```

Which will allow us to get some pretty graphs:

```python
import nltk
import json

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]

bea_tokens = []
ben_tokens = []

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
for token in tokenizer.tokenize(bea):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        bea_tokens.append(token.lower())
for token in tokenizer.tokenize(ben):
    if token.lower() not in nltk.corpus.stopwords.words('english'):
        ben_tokens.append(token.lower())

bea_freq = nltk.FreqDist(bea_tokens)
ben_freq = nltk.FreqDist(ben_tokens)

bea_freq.plot(20, cumulative=False)
ben_freq.plot(20, cumulative=False)
```

NLTK is a big and complicated piece of software designed to do (kind of) complicated analysis. This is still a unit on external dependencies and not on natural language processing or text analysis. Don't fret too much about how NLTK works or how to use it - the important part is that you now have the knowledge and the means and the wherewithall to exploit a vast universe of external python tools.
