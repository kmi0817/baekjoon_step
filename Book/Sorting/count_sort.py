array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [ 0 for _ in range(len(array))]
for element in array :
    count[element] += 1

for num, cnt in enumerate(count) :
    for i in range(cnt) :
        print(num, end=" ")