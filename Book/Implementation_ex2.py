# I failed to solve it so I check the book's solution
# I thought I needed to use Mathematics...
N = int(input())

solutions = 0

for h in range(N+1) :
    for m in range(60) :
        for s in range(60) :
            if "3" in str(h) + str(m) + str(s) :
                solutions += 1

print(solutions)