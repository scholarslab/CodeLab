# open the text of much ado about nothing and read it in line by line

file_path = "ado.txt"
with open (file_path, 'r') as file_input:
    text = file_input.read()

print(text)