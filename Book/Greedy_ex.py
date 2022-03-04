N = int(input())

min_cnt = N // 500
N %= 500

min_cnt += N // 100
N %= 100

min_cnt += N // 50
N %= 50

min_cnt += N // 10

print(f'최소 개수: {min_cnt}')

# more refined solution
N = int(input())

coins = [500, 100, 50, 10]
min_cnt = 0
for coin in coins :
    min_cnt += N // coin
    N %= coin
print(f'최소 개수: {min_cnt}')