n = int(input())

kg = [5, 3]

answer = 0
if n % 5 == 0 :
    answer = n // 5
    n = 0
elif n % 3 == 0 :
    answer = n // 3
    n = 0
else :
    for x in kg :
        answer += n // x
        n %= x

if n != 0 :
    print(-1)
else :
    print(answer)