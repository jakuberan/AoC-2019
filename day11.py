# Import libraries
from src.day05_supp import run_program
from src.day11_supp import rotate_coords

# Define path
data_path = "data/day11"
#data_path = "data/day11_test"

# Part of the problem
part = 2

# Read data
f = open(data_path, "r")
for x in f:
    data_in = {i: int(c) for i, c in enumerate(x.split(','))}

# Create board
dim = 85
board = [[0] * dim for _ in range(dim)]

# Initial settings based on problem part
if part == 1:
    posx   = int(0.85 * dim)
    posy   = int(0.75 * dim)
else:
    posx   = 1
    posy   = 1
    board[posy][posx] = 1

# Simulate robot moves
paint  = set()
orient = 0
program = data_in.copy()
pos = 0
base = 0
while True:
    col = board[posy][posx]
    paint.add((posx, posy))
    program, pos, new_col, base = run_program(
        program, pos, col, wo_base = False, base = base
        )
    # Paint or end
    if new_col == 'end': break
    else: 
        board[posy][posx] = new_col
        program, pos, rot, base = run_program(
            program, pos, col, wo_base = False, base = base
            )
        orient = (orient + (180 * rot - 90)) % 360
        posx, posy = rotate_coords(posx, posy, orient)

# Number of painted fields
print('Painted panels: ' + str(len(paint)))

# Output final picture
for t in range(dim):
    out = ''
    for w in range(dim):
        out += str(board[t][w])
    print(out)
    