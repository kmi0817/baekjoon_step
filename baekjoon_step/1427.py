number = input()

ns = [ int(n) for n in number ]
ns.sort()

for n in ns :
    print(n, end="")