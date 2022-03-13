# selection sort

# my pythonic way solution
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i, n in enumerate(array) :
    m = min(array[i:])
    j = array.index(m)

    array[i], array[j] = m, n # replace

print(array)