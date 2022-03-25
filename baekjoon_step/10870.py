def fibo(n) :
    left, right = 0, 1
    cnt = 2
    result = 0
    while cnt <= n :
        result = left + right
        left, right = right, result
        cnt += 1
    
    return result

n = int(input())
print(fibo(n))