n = 9
numbers = list()
for i in range(n) :
    num = int(input())
    if num < 100 :
        numbers.append(num)
    else :
        print("100보다 작은 자연수를 입력해야 합니다.")
        exit()

print(max(numbers))
print(numbers.index(max(numbers)) + 1)