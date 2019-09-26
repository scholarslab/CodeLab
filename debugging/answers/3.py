# takes a word and series of words and turns it into pig lattin.

def piglatin(word):
    if " " in word:
        x = word.split(" ")[0]
        x2 = word.split(" ")[1:]
        x = x[1:]+x[0].lower()+"ay"
        x = x + " " + " ".join(x2)
    elif ", " in word:
        x=word.split(", ")[0]
        x2 = word.split(", ")[1:]
        x = x[1:] + x[0].lower() + "ay"
        x = x + ", " + " ".join(x2)
    elif "-" in word:
        x=word.split("-")[0]
        x2 = word.split("-")[1:]
        x = x[1:] + x[0].lower() + "ay"
        x = x + " " + "-".join(x2)
    else:     
        x = word
        x = x[1:] + x[0].lower() + "ay"
    
    return x

print (piglatin(input("Enter input: Translate ")))