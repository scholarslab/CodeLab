# Answer for Week08 Assignment 0.A

import random

def is_sorted(nums):
    i = 1 #
    while i < len(nums):
        if nums[i]<nums[i-1]:
            return False
        i+=1
    return True

def random_sort(nums):
    while not is_sorted(nums):
        random.shuffle(nums)
    return nums

print(random_sort([7, 5, 1000, 3, 1, 4, 7, 8]))