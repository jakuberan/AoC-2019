def addperm(x, l):
    '''
    Performs permutations
    '''
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    '''
    Returns all permutations of a list
    '''
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]