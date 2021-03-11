# Import libraries
from src.day03_supp import mark_wire, wire_intersect

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

print("Closest intersection is " + wire_intersect(wire1, wire2))
