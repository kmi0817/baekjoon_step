array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i, n in enumerate(array) :
    if i == 0 : continue # skip index 0 because it starts sorting with index 1

    for j in range(i) :
        if array[j] > array[i] :
            array.insert(j, array.pop(i))
            break

print(array)