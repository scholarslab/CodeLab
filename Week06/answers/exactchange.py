DENOMINATIONS = [100,20,10,5,1,.25,.1,.05,.01]

# Input is the cost and payment, output is a list of denominations (bills, coins) that constitute change
def change(cost, payment):
    #change is the total we want to return
    change_owed = payment - cost
    # We need to return change, so let's set up an empty list to hold those
    list_of_change = []
    # If we owe change...
    if change_owed > 0:
        # keep looping as long as we owe more than the smallest denomination...
        while change_owed >= DENOMINATIONS[-1]:
            # Go down the list of denominations...
            for denomination in DENOMINATIONS:
                # ... until we hit a denomination that is smaller or equal to the amount owed
                # This will be the largest denomination that "fits" into the change 
                if denomination <= change_owed:
                    # Add the denomination to the list of change to return and...
                    list_of_change.append(denomination)
                    # ... subtract the denomination amount from the amount owed
                    change_owed -= denomination
                    # break out of the for look to go through the list of denomination so we start again at the top
                    break
        #return the change
        return list_of_change
    # We don't need to return change
    elif change_owed == 0:
        return []
    # Otherwise, there's not enough payment!
    else:
        print("Hey there, what are you trying to pull?")
        return None

# Test cases
print(change(5,2.55))
print(change(2.55,5))
print(change(5,5))
print(change(0,5))