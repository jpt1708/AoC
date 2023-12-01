s = 0
for l in open(0).readlines():
    ints = list(filter(lambda x : x in "1234567890", l))
    s += int(ints[0] + ints[-1])

print(s)