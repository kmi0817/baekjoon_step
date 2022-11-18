n = int(input())
cnt = 0
nums = map(int, input().split())
for num in nums :
    if num != 1 :
        is_prime = True
        for i in range(2, num) :
            if num % i == 0 :
                is_prime = False
                break
        if is_prime :
            cnt += 1
    
print(cnt)