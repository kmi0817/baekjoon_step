def fibo(n, left, right) :
    if n <= 1 :
        print(right)
        return

    fibo(n-1, right, left+right)

n = int(input())
fibo(n, 0, 1)