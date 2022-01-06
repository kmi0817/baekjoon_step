try :
    N = int(input())

    for i in range(1, 10) :
        print(N, "*", i, "=", N * i)
        #print(f"{N} * {i} = ", N * i)

except :
    print("입력이 잘못되었습니다.")
