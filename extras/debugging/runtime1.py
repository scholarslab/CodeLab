# Find the highest point
# Input: a matrix of height values,
#        representing a topographic map
# Output: the highest point in the map
def find_peak(map):
    # Starting coordinates
    x = 0
    y = 0
    # floor height
    peak = 0
    while y < len(map):
        while x < len(map[y]):
            if map[x][y] > peak:
                peak = map[x][y]
            x+=1
        y+=1
    return(peak)

# A topographic map
map = [[5,3,1,3,4],
       [1,3,3,5,4],
       [3,2,4,5,6],
       [6,4,1,7,4],
       [3,4,4,5,3]]
print(find_peak(map))