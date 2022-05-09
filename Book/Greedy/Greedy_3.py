# 2022-05-09
n, k = map(int, input().split())

answer = 0
while n > 1:
    if n % k != 0:
        n -= 1
        answer += 1

    else:
        n //= k
        answer += 1

print(answer)

# 2022-03-08 minus -1 or divide by K until N becomes 1

N, K = map(int, input().split())

cnt = 0
while N != 1 :
    if N % K == 0 :
        N /= K
    else :
        N -= 1
    cnt += 1

print(cnt)