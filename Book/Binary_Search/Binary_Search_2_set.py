import sys

n = int(input())
data_n = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
data_m = list(map(int, sys.stdin.readline().rstrip().split()))

for target in data_m :
    if target in data_n :
        print("yes", end=" ")
    else :
        print("no", end=" ")