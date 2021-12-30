A = int(input())
B = int(input())
C = int(input())

if A in range(100, 1000) and B in range(100, 1000) and C in range(100, 1000) :
    res = A * B * C

    for i in range(10) :
        print(str(res).count(str(i)))