with open("1519-0.txt",mode="r") as infile:
    text = infile.read()
    # Instead of reading the file line by line (text lines, not dialog lines), we want to read it in all at once.
    # This is because each text line is associated with other lines (multiple lines form a single dialog line), and so that we can perform string operations like split on it.
    # Once we read the file into text, we don't need it open anymore

# Set all our variables to zero
ben_lines = 0 
ben_len = 0
bea_lines = 0
bea_len = 0

for line in text.split("\n\n"):
    # We can split on two newline characters because each line of dialog is separated by an empty text line 
    # This isn't strictly correct because of stage directions, but it's good enough for this purpose
    if line.startswith("BENEDICK."):
        ben_lines+=1
        ben_len += len(line)-9 #9 is the length of "BENEDICK." and, again, it's a close enough aproximation
    elif line.startswith("BEATRICE."):
        bea_lines += 1
        bea_len += len(line)-9 #9 is also the length of "BEATRICE."

with open("MAAN_lines.txt", mode="w") as outfile:
    outfile.write("Benedick has "+str(ben_lines)+" lines totalling length "+str(ben_len)+" characters\n") #\n is the special new line character
    outfile.write("Beatrice has "+str(bea_lines) +
                  " lines totalling length "+str(bea_len))
