number = input()

ns = [ int(n) for n in number ]
ns.sort(reverse=True)

for n in ns :
    print(n, end="")