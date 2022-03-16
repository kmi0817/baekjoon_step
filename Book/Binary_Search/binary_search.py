def binary_search(array, target) :
    start, end = 0, len(array) - 1
    
    while start <= end :
        middle = int((start + end ) / 2)

        if array[middle] < target :
            start = middle + 1
        elif array[middle] > target :
            end = middle - 1
        else :
            return middle + 1

    
    return "원소가 존재하지 않습니다"

n, target = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, target))