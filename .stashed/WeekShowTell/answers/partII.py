import json
import nltk  # useful for the word frequency part, but not strictly necessary.
import string

with open("MAAN_dialog.json", "r") as infile:
    dialog = json.loads(infile.read())

bea = ""
ben = ""

# Collate the dialog lines for each role
for line in dialog:
    if line["role"] == "BEATRICE":
        bea += " "+line["dialog"]
    elif line["role"] == "BENEDICK":
        ben += " "+line["dialog"]

# Optional: add some code to remove punctuation marks because they don't matter to us
# Searching for "replace punctuation with whitespace python" is probably a good idea here.

# map punctuation to space
translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
bea = bea.translate(translator)
ben = ben.translate(translator)

# Tokenize (split into separate words) each dialog collection
# For this exercise, we don't care about stopwords
bea_tokens = bea.split()
ben_tokens = ben.split()

bea_unique_words = []
ben_unique_words = []

# Loop through the bea and ben tokens and only add them
# to the unique list if they don't appear in the other character's token list 
for word in bea_tokens:
    if word not in ben_tokens:
        bea_unique_words.append(word)

for word in ben_tokens:
    if word not in bea_tokens:
        ben_unique_words.append(word)

# Load into NLTK and plot frequencies.
# Don't forget to run `pipenv install matplotlib` for the plots
bea_freq = nltk.FreqDist(bea_unique_words)
ben_freq = nltk.FreqDist(ben_unique_words)
bea_freq.plot(20, cumulative=False)
ben_freq.plot(20, cumulative=False)
