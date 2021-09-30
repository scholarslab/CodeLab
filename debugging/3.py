### THIS EXERCISE CODE HAS BEEN CORRECTED ALREADY ###

# Create a function that will filter evens from a list of numbers

def filter_evens(list):
    # take a list of numbers and return only the even ones 
    even_numbers=[]
    for num in list: 
        if num / 2 == 0: 
            even_numbers.append(num)
    return even_numbers
nums = [0,-2,3,14]
print(filter_evens(nums))