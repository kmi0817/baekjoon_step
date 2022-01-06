try :
    n, x = input().split()
    N = int(n)
    X = int(x)

    if N in range(1, 10001) and X in range(1, 10001) :
        temp_list = input().split()
        for e in temp_list :
            element = int(e)
            if element < X :
                print(element, end=" ")
        
    else :
        print("수의 범위를 확인하세요.")
except :
    print("문제가 발생했습니다.")