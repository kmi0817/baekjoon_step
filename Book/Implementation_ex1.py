N = int(input())
plans = input().split()
x, y = 1, 1

for plan in plans :
    if plan == "L" and y - 1 > 0 :
        y -= 1
    elif plan == "R" and y + 1 <= N :
        y += 1
    elif plan == "U" and x - 1 > 0 :
        x -= 1
    elif plan == "D" and x + 1 <= N :
        x += 1

print(x, y)