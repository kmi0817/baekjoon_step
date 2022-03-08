# more refined solution
start = input()
col = ord(start[0]) - ord("a") + 1 # reduce 2 lines to 1 line
row = int(start[1])

steps = [ (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2) ]
cnt = 0
for step in steps :
    c = col + step[0]
    r = row + step[1]

    if c in range(1, 9) and r in range(1, 9) :
        print(c, r)
        cnt += 1

print(cnt)

# my solution
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