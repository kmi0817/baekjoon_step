def d(n) :
    str_n = str(n)

    result = n
    for digit in str_n :
        result += int(digit)
    return result

numbers = set(x for x in range(1, 10001))
phibo = set()
for n in numbers :
    phibo.add(d(n))

self_number = list(numbers - phibo)
for i in sorted(self_number) :
    print(i)