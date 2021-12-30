def check_and_make_int(num) :
    number = int(num)
    if number >= -1000000 and number <= 1000000 :
        return number
    else :
        exit()

N = int(input())
if N < 1 or N > 1000000 :
    exit()

numbers = list(map(check_and_make_int, input().split()))
if len(numbers) == N :
    smallest = min(numbers)
    largest = max(numbers)
    print(smallest, largest)
else :
    print("입력한 정수의 개수가 " + str(N) + "과 동일하지 않습니다.")