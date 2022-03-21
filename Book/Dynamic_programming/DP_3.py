n = int(input())
ks = list(map(int, input().split()))

profits = []
for i, k in enumerate(ks) :
    for t in ks[i+2:] :
        profits.append(k + t)

print(max(profits))