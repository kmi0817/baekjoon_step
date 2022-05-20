# 곱하기 혹은 더하기
s = input()

answer = 1
for n in s :
    if n != "0" :
        answer *= int(n)

print(answer)