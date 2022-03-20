from re import sub


n, m = map(int, input().split())
array = list(map(int, input().split()))

total_sum = -1
results = [x for x in range(max(array))]

left = 0
right = len(results)-1
while left <= right :
    middle = (left + right) // 2
    # print("middle", middle)
    subtracted_array = list(map(lambda x: x - results[middle] if x > results[middle] else 0, array)) # subtract results[middle] only if element is bigger than that
    total_sum = sum(subtracted_array)
    # print(subtracted_array)
    # print(total_sum)
    if total_sum == m :
        break

    elif total_sum > m :
        left = middle + 1
    else :
        right = middle - 1

print(left, right)
print(results[middle])