# 2022-05-09
n, m = map(int, input().split())

smallest_card = []  # 각 행마다 가장 작은 값이 저장될 리스트
for _ in range(n):
    smallest_card.append(min(list(map(int, input().split()))))
    # 입력받은 한 행 (문자열)을 리스트로 전환한 후 최소 값을 반환하는 min() 함수 사용

print(max(smallest_card)) # 각 행에서 가장 작은 값들을 모은 리스트에서 가장 큰 값을 출력

# 2022-03-08
N, M = map(int, input().split())

_max = -1
for row in range(N) :
    m = list(map(int, input().split()))

    _max = max(_max, min(m)) # find bigger mininum
    # if _max < min(m) :
        # _max = min(m)

print(_max)