def mark_position(out, x, y):
    '''
    Mark the actual position and return updated wire
    '''
    dist = abs(x) + abs(y)
    if dist in out: 
        out[dist][0].append(x) 
        out[dist][1].append(y)
    else: 
        out[dist] = [[x], [y]]
        
    return out

def mark_wire(commands):
    '''
    Saves all positions visited by a wire
    '''
    posx = 0
    posy = 0
    out = {0: [[posx], [posy]]}
    
    for c in commands:
        direction = c[0]
        steps = int(c[1:])
    
        if direction == 'U':
            for _ in range(steps):
                posy += 1
                out = mark_position(out, posx, posy)
        elif direction == 'D':
            for _ in range(steps):
                posy -= 1
                out = mark_position(out, posx, posy)
        elif direction == 'R':
            for _ in range(steps):
                posx += 1
                out = mark_position(out, posx, posy)
        elif direction == 'L':
            for _ in range(steps):
                posx -= 1
                out = mark_position(out, posx, posy)
    
    return out

def wire_intersect(wire1, wire2, output = 'single'):
    '''
    Finds intersection between two wires (closest to the origin)
    '''
    out = []
    # Walk through the distances
    for d in range(1, max(wire1.keys())):
        if d in wire2.keys():
            inter_x = set(wire1[d][0]).intersection(set(wire2[d][0]))
            for posx in inter_x:
                posy1 = [wire1[d][1][i] for i, x in enumerate(wire1[d][0]) 
                         if x == posx]
                posy2 = [wire2[d][1][i] for i, x in enumerate(wire2[d][0]) 
                         if x == posx]
                inter_y = set(posy1).intersection(set(posy2))
                if len(inter_y) > 0:
                    if output == 'single': return str(d)
                    else: 
                        for y in inter_y:
                            out.append([posx, y])

    return out

def get_distances(commands, intersections):
    '''
    Get distnaces of origin to intersections
    '''
    posx = 0
    posy = 0
    dist = 0
    distances = [0] * len(intersections)
    
    for c in commands:
        direction = c[0]
        steps = int(c[1:])
    
        if direction == 'U':
            for _ in range(steps):
                dist += 1
                posy += 1
                if [posx, posy] in intersections:
                    distances[intersections.index([posx, posy])] = dist
        elif direction == 'D':
            for _ in range(steps):
                dist += 1
                posy -= 1
                if [posx, posy] in intersections:
                    distances[intersections.index([posx, posy])] = dist
        elif direction == 'R':
            for _ in range(steps):
                dist += 1
                posx += 1
                if [posx, posy] in intersections:
                    distances[intersections.index([posx, posy])] = dist
        elif direction == 'L':
            for _ in range(steps):
                dist += 1
                posx -= 1
                if [posx, posy] in intersections:
                    distances[intersections.index([posx, posy])] = dist
    
    return distances
        