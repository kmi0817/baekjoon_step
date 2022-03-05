N, M, K = map(int, input().split())
Ns = list(map(int, input().split()))
Ns.sort(reverse=True)

sum_result = 0
while M > 0 :
    for k in range(K) :
        if M == 0 : break

        sum_result += Ns[0]
        M -= 1
    
    if M == 0 : break
    
    sum_result += Ns[1]
    M -= 1

print(sum_result)