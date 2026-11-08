
world = ['H', 'L', 'L', 'H', 'L', 'H', 'L', 'L']

p = [1/len(world)] * len(world)

p_hit = 0.7
p_miss = 0.2
p_exact = 0.8
p_overshoot = 0.1


def sense(p, world, measurement, p_hit, p_miss):
    q = []
    for i in range(len(p)):
        hit = (measurement == world[i])
        q.append(p[i] * (p_hit if hit else p_miss))
    s = sum(q)
    q = [x / s for x in q]
    return q


def move(p, U, p_exact, p_overshoot):
    n = len(p)
    p_undershoot = 1 - p_exact - p_overshoot
    q = [0.0] * n
    for i in range(n):
        q[i] = (p[(i-U) % n] * p_exact +
                p[(i-U-1) % n] * p_overshoot +
                p[(i-U+1) % n] * p_undershoot)
    return q


p = sense(p, world, 'H', p_hit, p_miss)
print("After Sense 1:", [round(x, 3) for x in p])

p = move(p, 2, p_exact, p_overshoot)
print("After Move 1:", [round(x, 3) for x in p])

p = sense(p, world, 'L', p_hit, p_miss)
print("After Sense 2:", [round(x, 3) for x in p])

p = move(p, 2, p_exact, p_overshoot)
print("After Move 2:", [round(x, 3) for x in p])