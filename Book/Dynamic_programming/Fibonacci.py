# Dynamic Programming
def dynamic_fibo(n) :
    if n <= 2 :
        return 1

    if array[n] != 0 :
        return array[n]
    else :
        array[n] = dynamic_fibo(n-1) + dynamic_fibo(n-2)
        return array[n]


# O(2^N)
def fibo(n) :
    if n <=2 :
        return 1

    return fibo(n-1) + fibo(n-2)

print(fibo(11))

array = [0 for _ in range(100)]
print(dynamic_fibo(99))