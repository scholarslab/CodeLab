# pig latinize

vowel = ["a","e","i","o","u"]
consonant = ("b","c","d","f","g","h","j","k","l","m","n","p","w","r","s","t","v","w","x","y","z")
ay = "ay"
yay = "yay"

#why does the input variable not work in the function. i.e. program only works if the function placeholder is differnt from imput variable 

def pig_latinize(user_word):
    user_word=user_word.lower()
    first_letter = user_word[0]
    second_letter = user_word[1]    
    
    if first_letter in vowel
        return user_word[0:]+yay

    elseif first_letter in consonant and second_letter in consonant:
        return user_word[2:]+user_word[0:2]+ay
        
    else:
        return user_word[1:]+user_word[0]+ay

users_word = input("Enter a word to translate to Pig Latin?: ")
output = pig_latinize(user_word)

print(output.title())
# alternatively, you can also use print(output)
