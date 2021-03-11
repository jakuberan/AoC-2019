# Define path
data_path = "data/day08"

# Parameters
wide = 25
tall = 6
pixels = wide * tall
layers = []
layers_stats = []

# read input data
f = open(data_path, "r")
for x in f:
    # Convert to int and append
    line = x.strip()

# Produce layers and their stats
minzero_ln = 0
minzero = pixels
for ln in range(int(len(line) / pixels)):
    layers.append(line[(ln * pixels):((ln + 1) * pixels)])
    layers_stats.append([
        layers[ln].count('0'), 
        layers[ln].count('1'), 
        layers[ln].count('2')
        ])
    if minzero > layers_stats[ln][0]: 
        minzero_ln = ln
        minzero = layers_stats[ln][0]
        
# Report stats on layer with minimal number of zoros
print('#1 x #2 in layer with least #0: ' + 
      str(layers_stats[minzero_ln][1] * layers_stats[minzero_ln][2]))

# Output image template
img_out = [ [3] * wide for _ in range(tall)]

# Scan through the pixels and save the first visible one
for i in range(len(layers[0])):
    pix_out = '2'
    ln = 0
    while pix_out == '2':
        pix_out = layers[ln][i]
        ln += 1
    img_out[int(i / wide)][i % wide] = pix_out
    
# Output final picture
for t in range(len(img_out)):
    out = ''
    for w in range(len(img_out[t])):
        out += img_out[t][w]
    print(out)
    