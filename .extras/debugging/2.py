def pig_latin(word):
    return word[1:] + word[0].lower() + "ay"

def repeat(word, number):
    return (word+" ")*number

s = "praxis codelab code lab"
l = s.split(" ")
print(repeat(pig_latin(l[0]),10) + " ".join(l[1:]))