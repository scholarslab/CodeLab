# fizzbuzzattemptsLV
# Example output: "1 2 fizz 4 buzz fizz 7"
# fizz for numbers divisible by three
# buzz for numbers divisible by five


stored_num = int(input("Enter a number: "))
counter = 0
while counter < stored_num:
    counter += 1
    if counter == 0:
        continue
    if counter % 3 == 0:
        print("fizz")
        continue
    if counter % 5 == 0:
        print("buzz")
        continue
    print(counter)