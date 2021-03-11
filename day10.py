# Import libraries
from math import atan2, pi
from src.day10_supp import rays_2D

# Define path
data_path = "data/day10"
#data_path = "data/day10_test"
#data_path = "data/day10_test2"

# Parameters
space = []
aster_cnt = 0

# Save space
f = open(data_path, "r")
for x in f:
    # Add to spacemap and count asteroids
    line = [c for c in x.strip()]
    space.append(line)
    aster_cnt += line.count('#')
    
# Save space parameters
width  = len(space[0])
height = len(space)

# Obtain rays (half plane)
rays = rays_2D(width, height)

# Mark the number of asteroids possible to see
space_num = [[0 if c == '.' else aster_cnt - 1 for c in line] for line in space]
        
# Scan through the space and note obstacles from both directions
for h in range(height):
    for w in range(width):
        if space_num[h][w] > 0:
            # Scan through all eligible rays
            for ray in rays:
                blocked = False
                ray_h = h + ray[0]
                ray_w = w + ray[1]
                while ray_h < height and ray_w < width and ray_w >= 0:
                    # Check the status of inspected field
                    if space_num[ray_h][ray_w] > 0:
                        if blocked:
                            space_num[h][w] -= 1
                            space_num[ray_h][ray_w] -= 1
                        else:
                            blocked = True
                    ray_h += ray[0]
                    ray_w += ray[1]

# Obtain maximum number
astr_max = 0
for h in range(height):
    for w in range(width):
        if space_num[h][w] > astr_max:
            astr_max = space_num[h][w]
            h_best = h
            w_best = w

print('Best palce [{}, {}] sees {} asteroids'.format(w_best, h_best, astr_max))

# Generate rays coverring the whole plane
rays_new = []
for ray in rays:
        rays_new.append([-ray[0], -ray[1]])
rays = [*rays, *rays_new]

# Calculate degrees for each ray -- to order them
rays_deg = {}
for ray in rays:
    ray_atan2 = atan2(ray[1], ray[0])
    if ray_atan2 >=0:
        rays_deg[ray_atan2] = [ray[0], ray[1]]
    else:
       rays_deg[2 * pi + ray_atan2] = [ray[0], ray[1]]

# Ordered rays
rays_ord = [rays_deg[deg] for deg in sorted(rays_deg.keys())]

# Scan using the rays and remove the asteroids
cnt   = 0
limit = 200
while cnt < limit:
    ray = rays_ord.pop(0) 
    h_ray = h_best - ray[0]
    w_ray = w_best + ray[1]
    while w_ray < width and w_ray >= 0 and h_ray < height and h_ray >= 0:
        if space[h_ray][w_ray] == '#':
            space[h_ray][w_ray] = '.'
            cnt += 1
            ray.append(ray)
            break
        else:
            h_ray -= ray[0]
            w_ray += ray[1]

print(str(limit) + "th asteroid vaporized was " + str(100*w_ray + h_ray))
