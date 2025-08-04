# Returns True if the list is sorted
# Returns False if the list is not sorted
def is_sorted(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] > numbers[i+1]:
            return(False)
    return(True)

print("This should be True: ", is_sorted([1,4,6,7,8,9]))
print("This should be False: ", is_sorted([3,6,2,5,7]))