maxcubes = {"red": 12, "green": 13, "blue": 14}
sol = 0

for line in open(0).readlines():
    l, r = line.split(':')
    gameid = int(l.split(' ')[1])
    hands = r.split(';')
    for h in hands:
        possible = True
        numcolors = h.split(',')
        for nc in numcolors:
            amt, clr = nc.split()
            amt = int(amt)
            if amt > maxcubes[clr]:
                possible = False
                break
        if not possible:
            break
    if possible:
        sol += gameid

print(sol)
