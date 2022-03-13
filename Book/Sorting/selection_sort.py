# selection sort

# my pythonic way solution
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i, n in enumerate(array) :
    m = min(array[i:])
    j = array.index(m)

    array[i], array[j] = m, n # replace

print(array)

# more common way solution
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    min_index = -1
    min = 9999
    for j in range(i+1, len(array)) :
        if array[j] < min :
            min = array[j]
            min_index = j

    array[i], array[min_index] = min, array[i]

print(array)