try :
    a, b = input().split()
    A = int(a)
    B = int(b)

    if A in range(-10000, 10001) and B in range(-10000, 10001) :
        if A > B :
            print(">")
        elif A < B :
            print("<")
        else :
            print("==")
    else :
        print("수의 범위가 맞지 않습니다")
except :
    print("정수를 입력하시오")