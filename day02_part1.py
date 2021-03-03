# Define path
data_path = "data/day02"
#data_path = "data/day02_test"

# Read data
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    data_in = [int(c) for c in x.split(',')]

# Restore the gravity assist program
data_in[1] = 12
data_in[2] = 2

# Apply transofrmations
i = 0
while i < len(data_in):
    
    # Assing and check operation
    oper  = data_in[i]
    assert oper in [1, 2, 99], "operation not recognized"
    if oper == 99:
        break
    
    # Obtain data and do operation
    num_1 = data_in[data_in[i + 1]]
    num_2 = data_in[data_in[i + 2]]
    if oper == 1:
        data_in[data_in[i + 3]] = num_1 + num_2
    else:
        data_in[data_in[i + 3]] = num_1 * num_2

    # Increment
    i += 4
    
print("Position 0 value: " + str(data_in[0]))
