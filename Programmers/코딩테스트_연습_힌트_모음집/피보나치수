def fibo(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        l, r = 0, 1
        for i in range(n-1) :
            l, r = r, (l + r) % 1234567
            
        return r
    
def solution(n):
    answer = fibo(n)
    return answer