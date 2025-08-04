# Create a function that will take a name and generate a greeting for you.

def filter_evens(list):  
    even_numbers=[]
    for num in list: 
        if num % 2 == 0: 
            even_numbers.append(num)
    return even_numbers
nums = [0,-2,3,14]
print(filter_evens(nums))