n = int(input())
ropes = []
for _ in range(n) :
    ropes.append(int(input()))

ropes.sort() # 오름차순 정렬

# 각 로프를 사용했을 때 들어올릴 수 있는 물체의 중량
each_max = [x * (len(ropes) - i) for i, x in enumerate(ropes) ]
# Ex) ropes == [4, 5, 6, 7]일 때, each_max == [4*4, 5*3, 6*2, 7*1]
# 중량 4는 4개의 로프가 들어올릴 수 있으므로, each_max[0] = 16
# 중량 5는 5개의 로프가 들어올릴 수 있으므로, each_max[1] = 15

answer = max(each_max)
print(answer)