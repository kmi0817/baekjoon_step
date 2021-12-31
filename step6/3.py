N = int(input())
if N < 0 or N > 1000 :
    exit()

cnt = 0
for n in range(1, N+1) :
    if n in range(1, 100) :
        cnt += 1

    if n in range(100, 1000) :
        str_n = str(n)
        a, b, c = int(str_n[0]), int(str_n[1]), int(str_n[2])
        if a - b == b - c :
            cnt += 1

print(cnt)