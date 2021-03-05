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
    # Convert to int and append
    data_in = [int(c) for c in x.split(',')]

# Apply transofrmations
i = 0
while i < len(data_in):
    
    # Translate instruction
    instr = data_in[i]
    oper  = instr % 100
    instr = instr - oper
    mode1 = instr % 1000
    mode2 = (instr - mode1) % 10000
    
    # Check operation
    assert oper in [1, 2, 3, 4, 5, 6, 7, 8, 99], "operation not recognized"
    if oper == 99:
        break
    
    # Obtain data and do operation
    if oper in [1, 2, 5, 6, 7, 8]:
        # Apply modes
        if mode1 > 0:
            num_1 = data_in[i + 1]
        else:
            num_1 = data_in[data_in[i + 1]]
        if mode2 > 0:
            num_2 = data_in[i + 2]
        else:
            num_2 = data_in[data_in[i + 2]]
        if oper in [1, 2, 7, 8]:
            if oper == 1:
                to_store = num_1 + num_2
            elif oper == 2:
                to_store = num_1 * num_2
            elif (oper == 7)*(num_1 < num_2) or (oper == 8)*(num_1 == num_2):
                to_store = 1
            else:
                to_store = 0
            data_in[data_in[i + 3]] = to_store
            i += 4
        else:
            if (oper == 5)*(num_1 != 0) or (oper == 6)*(num_1 == 0):
                i = num_2
            else:
                i += 3
    else:
        if oper == 3:
            data_in[data_in[i + 1]] = memory
        else:
            if mode1 > 0:
                print(data_in[i + 1])
            else:
                print(data_in[data_in[i + 1]])
        i += 2
