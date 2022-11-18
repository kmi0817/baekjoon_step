a, b, v = map(int, input().split())
if b < 1 or a <= b or v < a or v > 1000000000 :
    print("range error")
    exit()

n = 0
while v > (a - b) * n + a :
    n += 1
print(n+1)