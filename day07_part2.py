# Import libraries
# import numpy as np
from src.day05_supp import run_program
from src.day07_supp import perm

# Define path
data_path = "data/day07"
#data_path = "data/day07_test4"
#data_path = "data/day07_test5"

# Read data
f = open(data_path, "r")
for x in f:
    data_in = [int(c) for c in x.split(',')]

# Get permutations
perms = perm([i + 5 for i in range(5)])

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
    while out != 'end':
        for num in range(5):
            prgs[num], pos[num], out = run_program(prgs[num], pos[num], out)
            if out not in ['in', 'end']: out_tmp = out
    max_so_far = max(max_so_far, out_tmp)
    
# Printing the output from maximal amplifier phase setting
print("Last amplifier biggest output: " + str(max_so_far))
