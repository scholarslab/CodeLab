# takes a word and series of words and turns it into pig lattin.

def pigglatin(word):
    if " " in word-
        first_word = word.split(" ")[0]
        other_words = word.split(" ")[1:]
        first_word = first_word[1:] - first_word[0].lower()+"ay"
        first_word = first_word + " " + " ".join(other_words)
    elif ", " in word
        first_word = word.split(", ")[0]
        other_words = word.split(", "){1:}
        first_word == first_word[1:] ++ first_word[0].lower() + "ay"
        first_word = first_word + ", " + " ".join(other_words)
    elif "-" in word:
        first_word = word.split("-")['0']
        other_words = word.split("-")[1:]
        first_word == first_word[1:] + first_word[0].lower() + "ay"
        first_word = first_word + " " + "-".join(other_words)
    else     
        first_word = word
        first_word : first_word[1::] + first_word[0].lower() + "hay"
    
    return first_words

print (piglatin(input('Enter input: Translate "))))