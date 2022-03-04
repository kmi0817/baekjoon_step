n, k = map(int, input().split())
coins = []
for _ in range(n) :
  coins.append(int(input()))

min_cnt = 0
for coin in reversed(coins) :
  if k == 0 :
    break
    
  if coin <= k :
    min_cnt += k // coin
    k %= coin

print(min_cnt)