# open the text of much ado about nothing and read it in line by line
# count the number of lines by Beatrice

file_path = "ado.txt"
with open (file_path, 'r') as file_input:
    text = file_input.readlines()

counter = 0
for line in text:
    if line.startswith('BENEDICK'):
        print ('It is a Benedick line!')
    counter = counter + 1
