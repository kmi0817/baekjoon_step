import sys

n = int(input())
data = []
for _ in range(n) :
    data.append(int(sys.stdin.readline()))

data.sort()

# List Comprehension 대신 아래 코드도 가능
# answer = 0
# for i, x in enumerate(data) :
#   answer += abs(x - (i+1))

unhappy = [abs(x - (i+1)) for i, x in enumerate(data) ]
answer = sum(unhappy)

print(answer)