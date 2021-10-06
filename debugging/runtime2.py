# Find the first pair of numbers in a list that add up to the target
# Input: A list of numbers and a target number
# Output: A pair of numbers from that list that add up to the target
def sum_pair(numbers, target):
    i = 0    
    while i < len(numbers):
        j = i
        while j < len(numbers):
            # Do the two numbers at indices i and j add up to the target?
            if numbers[i]+numbers[j] == target:
                # return them as a tuple
                return (numbers[i],numbers[j])
    return(None)

input1 = [1,5,6,3]
print(sum_pair(input1,8))
print(sum_pair(input1,10))