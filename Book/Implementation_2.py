N, M = map(int, input().split())
x, y, d = map(int, input().split())
steps = [(x, y)] # track the character's step

maps = []
for _ in range(N) :
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True :
    is_way = False
    for _ in range(4) :
        d -= 1
        xx = x + dx[d%4]
        yy = y + dy[d%4]

        if maps[xx][yy] == 0 and (xx, yy) not in steps :
            is_way = True
            steps.append((xx, yy))
            x, y = xx, yy
            break

    if is_way == False :
        break

print(len(steps))