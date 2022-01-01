alphabets = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

string = input()

minimum_time = 0
for char in string :
    for index, chunk in enumerate(alphabets) :
        if char in chunk :
            minimum_time += (index + 2)

print(minimum_time)
