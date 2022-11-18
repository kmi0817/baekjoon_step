n = int(input())
p = list(map(int, input().split()))

# 앞사람의 인출 시간이 짧을수록 총 인출 시간이 단축된다.
# 즉, 인출 시간이 오름차순 정렬되어 있다면 총 인출 시간의 최솟값을 구할 수 있다.
p.sort() # p 오름차순 정렬

answer = 0
accumulation = 0
for pi in p :
    accumulation += pi # i번째 사람이 인출하는 데 걸리는 시간
    answer += accumulation # 모든 사람의 누적 인출 시간

print(answer)