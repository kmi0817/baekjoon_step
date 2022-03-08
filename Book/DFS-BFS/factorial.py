# normal function
def factorial(n) :
    result = 1
    for num in range(1, n+1) :
        result *= num
    return result

# recursive function
def recursive_factorial(n) :
    if n == 1 :
        return 1
    
    return n * recursive_factorial(n-1)

print("normal function:", factorial(5))
print("recursive function:", recursive_factorial(5))
