try :
    n = int(input())

    if n >= 1 and n <= 10000 :
        sum = 0
        for i in range(1, n+1) :
            sum += i
        print(sum)
    else :
        print("n의 범위가 잘못되었습니다.")

except :
    print("입력이 잘못되었습니다.")
