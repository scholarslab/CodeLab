def adds_up(nums, target):
    pairs = [] # initialize an empty list to hold the return values
    i = 0 # counter to keep track of the index of the first number
    while i < len(nums)-1: # loop to the end
        j = i+1
        while j < len(nums):
            if nums[i]+nums[j] == target:
                pairs.append([nums[i],nums[j]])
            j += 1
        i += 1
    return pairs


print(adds_up([1, 7, 5, 3, 4, 2], 7))
print(adds_up([1, 7, 0, 9, -2, 2], 7))