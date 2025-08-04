# open the text of much ado about nothing and read it in line by line
# count the number of lines by Beatrice

file_path = "ado.txt"
with open (file_path, 'r') as file_input:
    text = file_input.readlines()

benedick_lines = []
counter = 0
for line in text:
    if line.startswith('BENEDICK'):
        line_counter = 1
        while text[counter + line_counter] != '\n':
            benedick_lines.append(text[counter + line_counter])
            line_counter = line_counter + 1
    counter = counter + 1
print(benedick_lines)