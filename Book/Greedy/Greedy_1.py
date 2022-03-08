# better solution
N, M, K = map(int, input().split())
Ns = list(map(int, input().split()))
Ns.sort(reverse=True)

sum_result = ( M // (K+1) ) * (Ns[0] * K + Ns[1]) # temp_sum = Ns[0] * K + Ns[1]
sum_result += ( M % (K+1) ) * Ns[0]

print(sum_result)

# basic solution ( * It might cause Time Limit )
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