import json

with open("1519-0.txt", mode="r") as infile:
    text = infile.read()

dialog = [] # now a list, because we want to keep track of all the lines

for line in text.split("\n\n"):
    name = line.split("\n")[0]
    if not name.isupper() or not name.endswith("."):
        continue
    # Up to this point, it's more or less the same as the Week05 assignment

    line_dict = {} # create a new dictionary to keep track of the dialog line 
    line_dict["role"] = name[:-1] #[:-1] omits the ending period in the name
    line_dict["dialog"] = " ".join(line.split("\n")[1:]) #we split the dialog line on new line characters ("\n")
    # take all the text lines after the first line (which we know now is the role name)
    # then join them on spaces (we could join on new lines if we wanted to retain them)
    
    dialog.append(line_dict) #add our line dictionary to the list of dialogs
    
with open("MAAN_dialog.txt", mode="w") as outfile:
        outfile.write(json.dumps(dialog)) #dump the dialog into json, write it to the file