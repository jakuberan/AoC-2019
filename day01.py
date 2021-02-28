# Define path
data_path = "data/day01"

# Read line-by-line
fuel_total_1 = 0
fuel_total_2 = 0
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    fuel = int(int(x) / 3) - 2
    fuel_total_1 += fuel
    while fuel > 0:
        fuel_total_2 += fuel
        fuel = int(fuel / 3) - 2
    
print("Total fuel needed (part 1): " + str(fuel_total_1))
print("Total fuel needed (part 2): " + str(fuel_total_2)) 
