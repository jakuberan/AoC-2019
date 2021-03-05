# Define path
data_path = "data/day06"
#data_path = "data/day06_test"
#data_path = "data/day06_test2"

# Dictionary of orbits
orbits = {'COM': []}

# Save orbits to dictionary
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    line = x.strip().split(')')
    if line[0] not in orbits.keys(): orbits[line[0]] = []
    orbits[line[0]].append(line[1])
    
# Obtain orbit levels
parents = ['COM']
levels = {parents[0]: 0}
while len(parents) > 0:
    parent = parents.pop(0)
    if parent in orbits.keys():
        for planet in orbits[parent]:
            levels[planet] = levels[parent] + 1
            parents.append(planet)

print("Direct and indirect orbits: " + str(sum(levels.values())))

# Obtain inverse orbits
orbits_inv = {}
for parent in orbits:
    for planet in orbits[parent]:
        orbits_inv[planet] = parent
        
# Find planet in the intersection
nexty = 'YOU'
nexts = 'SAN'
yous = ['YOU']
sans = ['SAN']
while (nexty not in sans) and (nexts not in yous):
    # Find new parents and update lists
    if nexty != 'COM':
       nexty = orbits_inv[nexty]
       yous.append(nexty)
    if nexts != 'COM':
        nexts = orbits_inv[nexts]
        sans.append(nexts)
if nexty in sans: 
    inter = nexty
else:
    inter = nexts

# Calculate path lenght
path_len = sans.index(inter) + yous.index(inter) - 2
print("Minimum number of orbital transfers: " + str(path_len))
