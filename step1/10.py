try :
    abc_list = input().split(" ")
    A = int(abc_list[0])
    B = int(abc_list[1])
    C = int(abc_list[2])

    # if A >= 2 and A <=10000 and B >= 2 and B <=10000 and C >= 2 and C <=10000 :
    if A in range(2, 10001) and B in range(2, 10001) and C in range(2, 10001):
        print((A+B)%C)
        print(((A%C) + (B%C)) % C)
        print((A*B)%C)
        print(((A%C) * (B%C)) % C)
    else :
        print("범위가 올바르지 않습니다.")

except :
    print("정수입력")