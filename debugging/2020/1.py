# NOTE: FOR THESE YOU ARE NOT TRYING TO CHANGE THE UNDERLYING PROCESS OF THE CODE

# Produce a simple program to accept a single word as text input and then print
#  out a pig latin translation.

# Request word & store as variable "bacon"
bacon = input("Gimme a word to tarrrrrrnslate to pig latin. Please: ")

# For "bacon", remove character at position[0], suffix with that character,
# suffix with "ay"
# Could do more lines to remove, assign, suffix, suffix but let's see if we can do this more concisely
# It's called string slicing!


print(bacon[1:]+bacon[0] + "ay")
