n = int(input())
ns = list(map(int, input().split()))

m = int(input())
ms = list(map(int, input().split()))

for x in ms :
    if x in ns :
        print(1)
    else :
        print(0)