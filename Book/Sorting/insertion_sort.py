# my solution
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i, n in enumerate(array) :
    if i == 0 : continue # skip index 0 because it starts sorting with index 1

    for j in range(i) :
        if array[j] > array[i] :
            array.insert(j, array.pop(i))
            break

print(array)

# the book's solution
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    for j in range(i, 0, -1) :
        if array[j] < array[j-1] :
            # array[j] is originally array[i]
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break