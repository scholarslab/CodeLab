# count from 1 to 15 and say fizz if the number is divisible by 3, otherwise print the current number.

counter = 1
while counter < 16:
    if counter % 3 == 0:
        print('fizz')
    else:
        print(counter)
    counter = counter + 1