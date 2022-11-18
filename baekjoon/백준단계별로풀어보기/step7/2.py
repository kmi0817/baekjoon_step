N = int(input())
if N < 1 or N > 100 :
    exit()

numbers = input()
sum_result = 0
for n in numbers :
    sum_result += int(n)

print(sum_result)