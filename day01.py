# Define path
data_path = "data/day01"

# Read line-by-line
list_of_sums = []
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    list_of_sums.append(int(x))
