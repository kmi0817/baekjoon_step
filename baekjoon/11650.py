import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n) :
    x, y = map(int, input().split())
    li.append((x, y))

for tu in sorted(li) :
    print(tu[0], tu[1])