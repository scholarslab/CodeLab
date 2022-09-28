with open("1519-0.txt",mode="r") as infile:
    text = infile.read()

names = [] # list of names
lines = [] # list of number of lines. Indexes match the names in "names"
lengths = [] # list of total lengths. Indexes match the names in "names"

for line in text.split("\n\n"):  
    name = line.split("\n")[0] #Each dialog role is all caps and ends with a period.
    # Split off the text before the first new line and check to see if it's all uppercase and ends with a period.
    if not name.isupper() or not name.endswith("."):
        # if it isn't, it's not a line of dialog, so skip it.
        continue
    if name in names: # Check to see if the name is already in our names list
        i = names.index(name) # find the index of the name in the names/lines lists
        lines[i] += 1 # add one to the element in lines at index i
        lengths[i] += len(line)-(len(name)+1) # add the length of the line to lengths
    else: # If name isn't already in our names list...
        names.append(name) # add the name to the list
        lines.append(1) # append 1 to the lines list (indicating 1 line)
        lengths.append(len(line)-(len(name)+1)) # append the length of the line to the lengths list
        

with open("MAAN_lines.txt",mode="w") as outfile:
    for index in range(len(names)):
        outfile.write(names[index]+" has "+str(lines[index])+" lines totalling length "+str(
            lengths[index])+" characters\n")

# This is inaccurate for the same reasons the assignment 2 script is inaccurate
# and will further catch some extra lines (like part of the Guttenberg license statement at the end)
# But it's, well, good enough.
