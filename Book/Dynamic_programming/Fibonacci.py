# loop (bottom-up)
n = 11 # try to find f(11), the 11th fibonacci value
cnt = 1
result = 0
first, second = 1, 1
while cnt <= n - 2: # subtract 2 from n because f(1), f(2) is already included
    result = first + second
    print(f"first: {first}, second: {second}, result: {result}")
    first, second = second, result
    cnt += 1

print(result)

# Dynamic Programming (top-down)
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