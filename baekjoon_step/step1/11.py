try :
    x = int(input())
    y = input()

    last = x * int(y[2])
    print(last)

    middle = x * int(y[1])
    print(middle)

    first = x * int(y[0])
    print(first)

    result = x * int(y)
    print(result)
except :
    print("정수를 입력하세요")