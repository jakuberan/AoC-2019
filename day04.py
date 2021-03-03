# Import libraries
# import numpy as np

# Define path
low  = 156218
high = 652527
count = 0
part1 = False

for num in range(low, high):
    num_str = str(num)
    incr_count = 0
    same_count = []
    
    # Check number properties
    for i in range(5):
        if num_str[i] > num_str[i + 1]: break
        else: incr_count += 1
        if num_str[i] == num_str[i + 1]:
            if len(same_count) == 0:
                same_count.append(2)
            elif num_str[i - 1] == num_str[i]:
                same_count[len(same_count) - 1] += 1
            else:
                same_count.append(2)
                

    # If satisfied, increase counter
    if incr_count == 5:
        if (part1 and len(same_count) > 0) or (2 in same_count): 
            count += 1
    
print("There are {} numbers satisfying the properties".format(count))
    