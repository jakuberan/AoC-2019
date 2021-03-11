# Import libraries
from src.day03_supp import mark_wire, wire_intersect, get_distances

# Define path
data_path = "data/day03"
#data_path = "data/day03_test"
#data_path = "data/day03_test2"

# Read data
f = open(data_path, "r")
commands = []
for x in f:
    commands.append(x.split(','))
    
# Get wires
wire1 = mark_wire(commands[0])
wire2 = mark_wire(commands[1])

# Find all intersections
intersections = wire_intersect(wire1, wire2, output = 'all')

# Get distances
dist1 = get_distances(commands[0], intersections)
dist2 = get_distances(commands[1], intersections)

# Find minimum distance
print(min([dist1[i] + dist2[i] for i in range(len(dist1))]))
