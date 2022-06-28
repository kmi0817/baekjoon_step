s = input()

# zeros = s.count("0")
# ones = s.count("1")

distributions = []

initial = s[0]
count = 0
for c in s :
    if initial == c :
        count += 1
    else :
        distributions.append(count)
        count = 1
    initial = c
distributions.append(count)

answer = len(distributions) // 2
print(answer)