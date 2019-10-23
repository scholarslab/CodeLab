with open("1519-0.txt",mode="r") as infile:
    text = infile.read()

dialog = {} # dictionary to keep track of lines and lengths

for line in text.split("\n\n"):  
    name = line.split("\n")[0] #Each dialog role is all caps and ends with a period.
    # Split off the text before the first new line and check to see if it's all uppercase and ends with a period.
    if not name.isupper() or not name.endswith("."):
        # if it isn't, it's not a line of dialog, so skip it.
        continue
    # Check to see if the name is already in our dictionary
    if name not in dialog:
        # if not, initialize it to 0
        dialog[name] = (0, 0)
    # Increment the first element (lines) by 1
    # Increment the second element (length) by the length of the dialog minus the length of the name, +1 for the period at the end
    dialog[name] = (dialog[name][0]+1, dialog[name][1]+len(line)-(len(name)+1))

with open("MAAN_lines.txt",mode="w") as outfile:
    for role in dialog:
        outfile.write(role+" has "+str(dialog[role][0])+" lines totalling length "+str(
            dialog[role][1])+" characters\n")

# This is inaccurate for the same reasons the assignment 2 script is inaccurate
# and will further catch some extra lines (like part of the Guttenberg license statement at the end)
# But it's, well, good enough.