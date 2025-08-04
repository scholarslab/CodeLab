# Week 11

## Show and Tell!
![Show and Tell](assets/showtell.gif)

## Assignments (Review)

### Part I
![maple](assets/maple.jpg)

Let's do some straightforward  algorithm practice. I'll give you a list of numbers and a target number and you return a list of all the pairs of numbers in the list that add up to the target. 

So:

```python
def adds_up(nums,target):
    # your code here
    return pairs

print(adds_up([1,7,5,3,4,2],7)) #Should return [[5,2],[3,4]]
```

### Part II
![toby](assets/toby.jpg)

Let's use the [Much Ado About Nothing json file](answers/MAAN_dialog.json) we created in previous weeks again and switch up the analysis a bit. This time, let's find out which words that Beatrice and Benedick use exclusively are the most common.

So, write a script to load the json file, collate all the words that each character speaks, and then take out out all the words that appear in both Beatrice's and Benedick's lines.

A good place to start is the tokenization part of the code in the [Week10 lesson's NLTK example](https://github.com/scholarslab/CodeLab/blob/master/Week10/lesson.md#example-nltk).

```python
import json
import nltk # useful for the word frequency part, but not strictly necessary.

with open("MAAN_dialog.json","r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

# Collate the dialog lines for each role 
for line in dialog:
    if line["role"] == "BEATRICE":
        bea+=" "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben+=" "+line["dialog"]

# Optional: add some code to remove punctuation marks because they don't matter to us
# Searching for "replace punctuation with whitespace python" is probably a good idea here.

# Tokenize (split into separate words) each dialog collection
# For this exercise, we don't care about stopwords
bea_tokens = bea.split()
ben_tokens = ben.split()

bea_unique_words = []
ben_unique_words = []

# Here's where most of your code should go. Figure out a way to add words from bea_tokens to bea_unique_words only if they don't also appear in ben_tokens.


# Now, figure out which are the most frequent. You can do this yourself or just take it from the nltk example.
```
### Part III
There's no part III. Enjoy this photo of Fat Dog.

![fatdog](assets/fatdog.jpg)