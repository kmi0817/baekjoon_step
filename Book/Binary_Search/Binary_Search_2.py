import sys

def binary_search(array, target) :
    start, end = 0, len(array) - 1

    ret = "no"
    while start <= end :
        middle = (start + end) // 2
        
        if array[middle] == target :
            ret = "yes"
            break
        elif array[middle] < target :
            start = middle + 1
        else :
            end = middle - 1

    return ret

n = int(input())
data_n = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
data_m = list(map(int, sys.stdin.readline().rstrip().split()))

data_n.sort()
for num in data_m :
    print(binary_search(data_n, num), end=" ")