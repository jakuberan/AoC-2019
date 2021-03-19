# Import libraries
from src.day05_supp import run_program
from src.day07_supp import perm

# Define path
data_path = "data/day07"
#data_path = "data/day07_test"
#data_path = "data/day07_test2"
#data_path = "data/day07_test3"

# Read data
f = open(data_path, "r")
for x in f:
    data_in = {i: int(c) for i, c in enumerate(x.split(','))}

# Get permutations
perms = perm([i for i in range(5)])

# Search for the best permutation
max_so_far = 0
for permut in perms:
    
    # Obtain create initial programs
    prgs = [data_in.copy() for _ in range(5)]
    pos  = [0] * 5
    
    # Initial amplifier phase settings
    for num in range(5):
        out = None
        while out != 'in':
            prgs[num], pos[num], out = run_program(
                prgs[num], pos[num], permut[num]
                )
    
    # Run with subsequent inputs from previous amplifiers
    out = 0
    for num in range(5):
        prgs[num], pos[num], out = run_program(prgs[num], pos[num], out)
    max_so_far = max(max_so_far, out)
        
print("Last amplifier biggest output: " + str(max_so_far))
