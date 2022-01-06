try :
    N = int(input())

    if N >= 1 and N <= 100 :
        for i in range(1, N+1) :
            print("*" * i)
except :
    print("문제가 발생했습니다.")