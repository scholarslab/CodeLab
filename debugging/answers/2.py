# Produce a simple program to accept a single word as text input and then print
#  out a pig latin translation.

# Request word & store as variable "bacon"
piglatin=input("Which word do you want to translate?\n")

# For "pig", remove character at position[0], suffix with that character,
# suffix with "ay"

print(piglatin[1:]+piglatin[0]+"ay")
