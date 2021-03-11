# Define path
data_path = "data/day02"
#data_path = "data/day02_test"
from src.day05_supp import run_program

# Read data
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    data_in = [int(c) for c in x.split(',')]

# Restore the gravity assist program
data_in[1] = 12
data_in[2] = 2

# Apply transformations
out = None
pos = 0
program = data_in.copy()
while out != 'end':
    out_temp = out
    program, pos, out = run_program(program, pos, None)
        
print("Position 0 value: " + str(program[0]))
