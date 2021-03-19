def rotate_coords(x, y, orient):
    '''
    Rotates coordinates based on program outputs
    '''
    
    if orient == 0: y -= 1
    elif orient == 90: x += 1
    elif orient == 180: y += 1
    elif orient == 270: x -= 1
    
    return x, y
