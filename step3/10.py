try :
    N = int(input())

    if N >= 1 and N <= 100 :
        for astr, blank in enumerate(range(N-1, -1, -1), 1) :
            print(" " * blank, end="")
            print("*" * astr)
    else :
        print("N은 1 이상 100 이하의 정수입니다.")
except :
    print("문제가 발생했습니다.")