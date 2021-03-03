# Define path
data_path = "data/day02"
#data_path = "data/day02_test"

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
        data = data_in.copy()
        data[1] = noun
        data[2] = verb
        
        # Apply transofrmations
        i = 0
        while i < len(data):
            
            # Assing and check operation
            oper  = data[i]
            if oper not in [1, 2]: break
            
            # Obtain data and do operation
            num_1 = data[data[i + 1]]
            num_2 = data[data[i + 2]]
            if oper == 1:
                data[data[i + 3]] = num_1 + num_2
            else:
                data[data[i + 3]] = num_1 * num_2
        
            # Increment
            i += 4
        
        # Check the output
        if oper == 99 and data[0] == goal: found = True
        if found: break
    if found: break
        
    
print("Output: " + str(100 * noun + verb))
