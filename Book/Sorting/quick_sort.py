array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def sorting(arr, start, end) :
    if start >= end :
        return

    pivot = start
    i, j = start + 1, end

    while i <= j :
        while arr[pivot] >= arr[i] and i <= end :
            i += 1

        while arr[pivot] <= arr[j] and j >= start :
            j -= 1

        if i > j :
            arr[pivot], arr[j] = arr[j], arr[pivot]
        else :
            arr[i], arr[j] = arr[j], arr[i]

    sorting(arr, start, j-1) # left
    sorting(arr, j+1, end) # right


sorting(array, 0, len(array)-1)
print(array)