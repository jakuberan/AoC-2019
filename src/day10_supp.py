def rays_2D(width, height):
    '''
    Prepares a list of rays for given dimensions in 2D from [0, 0]
    '''
    
    # Space to keep track of fields and output lists
    space = [[True for c in range(width)] for c in range(height)]
    rays = []
    
    # Populate rays
    for h in range(height):
        for w in range(width):
            if h + w > 0:
                if space[h][w]:
                    # Start adding a new ray
                    h_ray = h
                    w_ray = w
                    rays.append([h_ray, w_ray])
                    
                    # Remove other directions from possibilities
                    while h_ray < height and w_ray < width:
                        space[h_ray][w_ray] = False
                        h_ray += h
                        w_ray += w
                        
    # Add rays from the backward direction
    rays_new = []
    for ray in rays:
        if ray[0] * ray[1] > 0:
            rays_new.append([ray[0], -ray[1]])
    rays = [*rays, *rays_new]
                    
    # Return the list of rays (half plane)
    return rays
