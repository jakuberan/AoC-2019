# Define path
data_path = "data/day02"
#data_path = "data/day02_test"
from src.day05_supp import run_program

# Read data
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    data_in = [int(c) for c in x.split(',')]

# Parameters
found = False
goal = 19690720

# Search the sapce of nouns and verbs
for noun in range(100):
    for verb in range(100):
        
        # Restore the gravity assist program
        program = data_in.copy()
        data_in[1] = noun
        data_in[2] = verb
        
        # Apply transformations
        out = None
        pos = 0
        program = data_in.copy()
        while out != 'end':
            out_temp = out
            program, pos, out = run_program(program, pos, None)
           
        # Check the output
        if program[0] == goal: 
            found = True
            break
    if found: break
        
    
print("Output: " + str(100 * noun + verb))
