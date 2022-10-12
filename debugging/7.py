# count from 1 to the input number and say fizz if the number is divisible by 3, otherwise print the current number.

counter = 0
n = input("Enter number:")
while counter < n:
    if counter % 5 == 0:
        print('buzz')
    elif counter % 3 == 0:
        print('fizz')
    else:
        print(counter)
    counter += 1