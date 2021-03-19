# Import libraries
from src.day05_supp import run_program

# Define path
data_path = "data/day09"
#data_path = "data/day09_test"
#data_path = "data/day09_test2"
#data_path = "data/day09_test3"

# Program input
part = 2
if part == 1: out = 1
else: out = 2

# Read data
f = open(data_path, "r")
for x in f:
    data_in = {i: int(c) for i, c in enumerate(x.split(','))}

# Apply transformations
out_temp = []
pos = 0
base = 0
program = data_in.copy()
while out != 'end':
    program, pos, out, base = run_program(
        program, pos, out, wo_base = False, base = base
        )
    out_temp.append(out)

print("Boost code:" + str(out_temp))
