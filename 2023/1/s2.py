s = 0
for l in open(0).readlines():
    first = '-'
    last = '-'
    for i in range(len(l)):
        if l[i] in "123456789":
            if first == '-':
                first = l[i]
            last = l[i]
            continue
        num = 'x'
        if l[i:i+3] == "one":
            num = '1'
        if l[i:i+3] == "two":
            num = '2'
        if l[i:i+3] == "six":
            num = '6'
        if l[i:i+4] == "four":
            num = '4'
        if l[i:i+4] == "nine":
            num = '9'
        if l[i:i+4] == "five":
            num = '5'
        if l[i:i+5] == "three":
            num = '3'
        if l[i:i+5] == "seven":
            num = '7'
        if l[i:i+5] == "eight":
            num = '8'
        if num == 'x':
            continue
        if first == '-':
            first = num
        last = num

    s += int(first + last)
    print(first,last)



print(s)