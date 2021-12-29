try :
    T = int(input())

    ab_sum = list()
    for i in range(T) :
        temp_a, temp_b = input().split()
        a = int(temp_a)
        b = int(temp_b)
        if a > 0 and b < 10 :
            ab_sum.append(a+b)
        else :
            exit(1)
            
    for index, result in enumerate(ab_sum, 1) :
        print("Case #" + str(index) + ": " + str(result))

except :
    print("입력이 잘못되었습니다.")
