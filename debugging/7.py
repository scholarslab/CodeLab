# count from 1 to the input number and say fizz if the number is divisible by 3, otherwise print the current number.

counter = input("Enter number: ")
while counter < 16:
    if counter % 5 == 0:
        print('buzz')
    elif counter % 3 == 0:
        print('fizz')
    else:
        print(counter)
    counter = counter + 1