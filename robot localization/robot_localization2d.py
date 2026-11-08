
world_2D = [
    ['H', 'L', 'L'],
    ['L', 'H', 'L'],
    ['L', 'L', 'H']
]

rows = len(world_2D)
cols = len(world_2D[0])
p2D = [[1/(rows*cols) for _ in range(cols)] for _ in range(rows)]

p_hit = 0.7
p_miss = 0.2
p_exact = 0.8
p_overshoot = 0.1

def sense2D(p, world, measurement, p_hit, p_miss):
    q = []
    s = 0.0
    for i in range(len(world)):
        row = []
        for j in range(len(world[0])):
            hit = (measurement == world[i][j])
            val = p[i][j] * (p_hit if hit else p_miss)
            row.append(val)
            s += val
        q.append(row)
    for i in range(len(q)):
        for j in range(len(q[0])):
            q[i][j] /= s
    return q

def move2D(p, motion, p_exact, p_overshoot):
    nrows, ncols = len(p), len(p[0])
    dy, dx = motion
    p_undershoot = 1 - p_exact - p_overshoot
    q = [[0.0 for _ in range(ncols)] for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            q[i][j] = (
                p[(i-dy) % nrows][(j-dx) % ncols] * p_exact +
                p[(i-dy-1) % nrows][(j-dx-1) % ncols] * p_overshoot +
                p[(i-dy+1) % nrows][(j-dx+1) % ncols] * p_undershoot
            )
    return q



print("=== 2D Localization ===")
p2D = sense2D(p2D, world_2D, 'H', p_hit, p_miss)
print("After Sense 1 (2D):")
for row in p2D:
    print([round(x,3) for x in row])

p2D = move2D(p2D, (1, 1), p_exact, p_overshoot)  
print("After Move 1 (2D):")
for row in p2D:
    print([round(x,3) for x in row])