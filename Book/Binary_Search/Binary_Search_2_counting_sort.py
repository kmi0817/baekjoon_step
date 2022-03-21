import sys

n = int(input())
data_n = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
data_m = list(map(int, sys.stdin.readline().rstrip().split()))

counting = [0 for _ in range(max(data_n) + 1)]
for num in data_n :
    counting[num] += 1

for target in data_m :
    if counting[target] != 0 :
        print("yes", end=" ")
    else :
        print("no", end=" ")