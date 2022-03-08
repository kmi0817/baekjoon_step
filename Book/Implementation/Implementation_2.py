N, M = map(int, input().split())
x, y, d = map(int, input().split())
steps = [(x, y)] # track the character's step

maps = []
for _ in range(N) :
    maps.append(list(map(int, input().split())))

# ordering: north, east, north, west
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn_cnt = 0
while True :
    # turn left
    d -= 1
    xx = x + dx[d%4]
    yy = y + dy[d%4]

    # there's a way available
    if maps[xx][yy] == 0 and (xx, yy) not in steps :
        steps.append((xx, yy))
        x, y = xx, yy
        turn_cnt = 0
        continue
    else :
        turn_cnt += 1
    
    # when it turns 4 times
    if turn_cnt == 4 :
        xx = x - dx[d%4]
        yy = y - dy[d%4]
        # check if back_step is available
        if maps[xx][yy] == 0 :
            x, y = xx, yy
            turn_cnt = 0
        else :
            break
    
print(len(steps))