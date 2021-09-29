# Create a function that will filter evens from a list of numbers

define filter_evens list: 
    even_numbers=()
    for number in list: 
        if num / 2 == 0: 
            even_numbers.add(num)
    return even_numbers
nums = [0,-2,3,14]
print(filter_evens nums )