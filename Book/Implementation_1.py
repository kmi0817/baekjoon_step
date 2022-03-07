starting_point = input()
col = starting_point[0]
row = int(starting_point[1])

ways = 8

if col < "c" or col > "f" :
    print(col)
    ways -= 2
if row < 3 or row > 6 :
    print(row)
    ways -= 2

print(ways)