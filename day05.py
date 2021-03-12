# Import libraries
from src.day05_supp import run_program

# Define path
data_path = "data/day05"
#data_path = "data/day05_test"
#data_path = "data/day05_test2"

# Program input
part = 2
if part == 1: memory = 1
else: memory = 5

# Read data
f = open(data_path, "r")
for x in f:
    data_in = [int(c) for c in x.split(',')]

# Apply transformations
out = None
pos = 0
program = data_in.copy()
while out != 'end':
    out_temp = out
    program, pos, out = run_program(program, pos, memory)
        
print(out_temp)
