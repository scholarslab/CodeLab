import nltk
# given a text file, print the first 100 text characters of it
def read_file(path_to_text):
    # take a file path and return the raw text from it
    with open(path_to_text, 'r') as fin:
        raw_text = fin.read()
    return raw_text


def split_text(raw_text):
    # takes a text and splits it into a series of tokens (words in text
    # analysis lingo)
    tokens = raw_text.split(' ')
    return tokens


def does_something_interesting(tokens):
    # takes a list of tokens and creates a frequency dispersion plot
    words_to_chart = ['he', 'she', 'the', 'said',  'boat']
    nltk.Text(tokens).dispersion_plot(words_to_chart)


text_path = 'woolf.txt'
print(text_path)
raw_text = read_file(text_path)
print(raw_text[0:15])
tokens = split_text(raw_text)
print(tokens[0:15])
does_something_interesting(tokens)