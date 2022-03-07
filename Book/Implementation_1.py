starting_point = input()

cols = "abcdefgh"
col = cols.index(starting_point[0]) + 1 # a
row = int(starting_point[1]) # 1

ways = [ ['l', 'l', 'u'], ['l', 'l', 'd'], ['r', 'r', 'u'], ['r', 'r', 'd'],
            ['u', 'u', 'l'], ['u', 'u', 'r'], ['d', 'd', 'l'], ['d', 'd', 'r'] ]

cnt = 0
for way in ways :
    c, r = col, row
    for d in way :
        if d == 'l' : c -= 1
        elif d == 'r' : c += 1
        elif d == 'u' : r -= 1
        elif d == 'd' : r += 1
    if c >= 1 and c <= 8 and r >= 1 and r <= 8:
        cnt += 1
print(cnt)