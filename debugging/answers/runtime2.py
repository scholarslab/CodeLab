# Find the first pair of numbers in a list that add up to the target
# Input: A list of numbers and a target number
# Output: A pair of numbers from that list that add up to the target

def sum_pair(numbers, target):
    i = 0
    while i < len(numbers)-1:
        j = i+1
        while j < len(numbers):
            if numbers[i]+numbers[j] == target:
                return (numbers[i],numbers[j])
            j+=1
        i+=1
    return(None)

input1 = [1,5,6,3]
print(sum_pair(input1,8))
print(sum_pair(input1,10))