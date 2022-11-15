# review (2022-11-15)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True) # 리스트 내림차순 정렬
max1, max2 = data[0], data[1]

x = max1 * k + max2 # 반복되는 수열

answer = (m // (k+1)) * x + (m % (k+1)) * max1
print(answer)

# review (2022-05-09)
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)  # 내림차순 정렬

first, second = numbers[0], numbers[1]  # 가장 큰 수 2개만 뽑아냄

# m = 8, k = 3이라고 가정
first_cnt = k * (m // k) # 가장 큰 수의 카운트 횟수 ex) 가장 큰 수는 3 * (8 // 3) = 6번 더해진다
second_cnt = m % k # 두 번째로 큰 수의 카운트 횟수 ex) 두 번째로 큰 수는 8 % 3 = 2번 더해진다

answer = (first * first_cnt) + (second * second_cnt)

print(answer)

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