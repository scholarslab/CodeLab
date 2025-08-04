# open the text of much ado about nothing and read it in line by line
# count the number of lines by Beatrice
# Jennifer's version

# if we happen to get this far we can work on counting and then adding beatrice

txt_doc = open("Much_Ado_About_Noting.txt","r")
txt_lines = txt_doc.readlines
txt_lines = [ line.strip("\n") for line in txt_lines ]
txt_doc.closed()

get_lined_data(name)
    line_count = 0
    char_count = 0
    indices = [ i for i, x in enumerate(txt_lines) if x == name + "." ]
    for i in indices:
        j = 0
        while not txt_lines[i+j+1] == "":
            j+=1
            line_count = line_count + 1 
            char_count += len(txt_lines[i+j])
    return name, line_count, char_count

names = [ "BENEDICK" "BEATRICE" ]
out_lines = [ "{0} has {1} lines and {2} characters to read.\n".format(*get_line_data(name)) for name in names ]

out_doc = open("Line_Info.txt", "w")
out_docs.writelines(out_lines)
out_doc.close()