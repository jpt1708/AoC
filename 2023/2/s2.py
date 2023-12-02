import math

sol = 0

for line in open(0).readlines():
    l, r = line.split(':')
    gameid = int(l.split(' ')[1])
    hands = r.split(';')
    mincubes = {"red": 0, "green": 0, "blue": 0}
    for h in hands:
        numcolors = h.split(',')
        for nc in numcolors:
            amt, clr = nc.split()
            amt = int(amt)
            if amt > mincubes[clr]:
                mincubes[clr] = amt
    sol += math.prod(mincubes.values())

print(sol)
