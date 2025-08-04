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


text_path = 'woolf.txt'
raw_text = read_file(text_path)
print(raw_text[0:20])
tokens = split_text(raw_text)
print(tokens[0:20])