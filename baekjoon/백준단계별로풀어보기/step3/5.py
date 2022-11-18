try :
    N = int(input())

    if N >= 1 and N <= 100000 :
        for i in range(1, N+1) :
            print(i)
    else :
        print("N은 100,000 이하의 자연수입니다.")
except :
    print("입력이 잘못되었습니다.")