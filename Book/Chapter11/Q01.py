from audioop import reverse
from collections import deque

n = int(input())
graph = deque(list(map(int, input().split())))

graph.sort(reverse=True) # 공포도 내림차순 정렬

group = 0