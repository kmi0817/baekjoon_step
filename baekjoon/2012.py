n = int(input())
data = []
for _ in range(n) :
    data.append(int(input()))

data.sort()

unhappy = [abs(x - (i+1)) for i, x in enumerate(data) ]

answer = sum(unhappy)
print(answer)