moduler_set = set()
for i in range(10) :
    n = int(input())

    if n > -1 and n <= 1000 :
        moduler_set.add(n % 42)

print(len(moduler_set))
