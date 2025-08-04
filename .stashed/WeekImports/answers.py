# Answer for Week08 Assignment 0.A

import random # usually, a good idea to keep imports at the top

def is_sorted(nums):
    i = 1 # 1, because we want to start by comparing nums[1] and nums[0] 
    while i < len(nums):
        if nums[i]<nums[i-1]:
            return False
            # Only one number has to be out of place for it to be not sorted.
            # The return breaks out of the loop.
        i+=1
    return True
    # if we cycle through the entire list without any numbers out of place, then it's sorted.

def random_sort(nums):
    while not is_sorted(nums): # the while conditional evaluates a boolean True or False, so that's what we need to return
        random.shuffle(nums)  # this will sort the numbers *in place*, so the original list will be reordered.
    return nums 

print(random_sort([7, 5, 1000, 3, 1, 4, 7, 8]))
