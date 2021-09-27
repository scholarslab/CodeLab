# Produce a simple program to accept a single word as text input and then print
#  out a pig latin translation.

# Request word & store as variable "bacon"
pig = input("Gimme a word to translate to pig latin:")

# For "pig", remove character at position[0], suffix with that character,
# suffix with "ay"

print(pig[1:]+pig[0] + "ay")
