m = int(input())
n = int(input())

primes = []
for num in range(m, n+1) :
    if num != 1 :
        is_prime = True
        for i in range(2, num) :
            if num % i == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(num)
print(sum(primes))
print(primes[0])